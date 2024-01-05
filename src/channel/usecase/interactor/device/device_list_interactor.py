from channel.usecase.input_port.device import DeviceListInputPort
from channel.usecase.repository.device import DeviceListRepository
from channel.usecase.models import (
    ChannelListInDsDto,
    DeviceListChannelDataOutDto,
    DeviceListDataOutDto,
    DeviceListInDsDto
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
from typing import List, Optional


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

            # 変換
            values = []
            for ds_dto in device_out_ds_dtos:
                if ds_dto.id not in channel_map:
                    continue

                channels = []
                for channel in channel_map[ds_dto.id]:
                    channels.append(
                        DeviceListChannelDataOutDto(
                            **channel.model_dump()
                        )
                    )

                values.append(
                    DeviceListDataOutDto(
                        id=ds_dto.id,
                        channels=channels,
                        api_key=ds_dto.api_key
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
