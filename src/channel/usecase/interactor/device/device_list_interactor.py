from datetime import datetime
from channel.usecase.input_port.device import DeviceListInputPort
from channel.usecase.repository.device import DeviceListRepository
from channel.usecase.models import (
    ChannelListInDsDto,
    DeviceListChannelDataOutDto,
    DeviceListDataOutDto,
    DeviceListInDsDto,
    RecordOutDsDto
)
from channel.usecase.output_port.device import DeviceListOututPort

from channel.usecase.models import (
    DeviceListInDto,
    DeviceListOutDto
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthorizedException
)
from channel.entity.models import Device

from pydantic import ValidationError
from typing import Dict, List, Optional


class DeviceListInteractor(DeviceListInputPort):

    def __init__(
            self,
            gateway: DeviceListRepository,
            presenter: DeviceListOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def list(
            self, device_dto: DeviceListInDto) -> DeviceListOutDto:

        try:

            # ユーザの確認
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            # Device検索
            device_out_ds_dtos = self.gateway.list(
                DeviceListInDsDto(
                    user_id=session_user_ds_dto.id
                )
            )

            # Channel検索
            channels = self.gateway.list_channel(
                ChannelListInDsDto(
                    device_ids=[device.id for device in device_out_ds_dtos]
                )
            )

            # DeviceIdでChannelリストを引けるようにする
            channel_map = {}
            for device in device_out_ds_dtos:
                channel_map[device.id] = []
            for channel in channels:
                if channel.device_id in channel_map:
                    channel_map[channel.device_id].append(channel)

            # 最新のレコードを取得する
            latest_records: Dict[int, RecordOutDsDto] = {}
            for device_id in channel_map:
                for channel in channel_map[device_id]:
                    record: Optional[RecordOutDsDto] = self.gateway.find_latest_record_by_channel_id(
                        channel.id)
                    if record:
                        latest_records[channel.id] = record

            # 変換
            values = []
            for ds_dto in device_out_ds_dtos:
                if ds_dto.id not in channel_map:
                    continue

                # Deviceの最終更新日時を取得する
                latest_time = None
                for channel in channel_map[ds_dto.id]:
                    if not channel.id in latest_records:
                        continue
                    if not latest_time:
                        latest_time = latest_records[channel.id].time
                        break
                    if latest_time and latest_time < latest_records[channel.id].time:
                        latest_time = latest_records[channel.id].time

                # Deviceの最終更新日時に一致しないレコードを無視する
                for channel in channel_map[ds_dto.id]:
                    if not channel.id in latest_records:
                        continue
                    if latest_time == latest_records[channel.id].time:
                        continue
                    del latest_records[channel.id]

                # Channelの変換
                channels = []
                for channel in channel_map[ds_dto.id]:

                    record_value: Optional[float] = None
                    if channel.id in latest_records:
                        record_value = latest_records[channel.id].value

                    channels.append(
                        DeviceListChannelDataOutDto(
                            **channel.model_dump(),
                            record=record_value
                        )
                    )

                values.append(
                    DeviceListDataOutDto(
                        id=ds_dto.id,
                        channels=channels,
                        api_key=ds_dto.api_key,
                        latest_time=latest_time,
                    )
                )

            out_dto = DeviceListOutDto(
                values=values,
            )

            self.presenter.prepare_success_view(out_dto)

            return out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
