from channel.usecase.input_port.device import DeviceListInputPort
from channel.usecase.repository.device import DeviceListRepository
from channel.usecase.models import (
    ChannelListInDsDto,
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
from typing import Optional


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

            # TODO: Channel検索

            # 変換
            out_dto = DeviceListOutDto()
            if device_out_ds_dtos:
                out_dto = DeviceListOutDto(
                    values=[
                        DeviceListDataOutDto(
                            id=ds_dto.id,
                            # TODO:
                            channel_ids=[],
                            channel_names=[]
                        )
                        for ds_dto in device_out_ds_dtos
                    ]
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
