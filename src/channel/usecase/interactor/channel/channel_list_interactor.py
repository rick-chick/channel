from channel.usecase.input_port.channel import ChannelListInputPort
from channel.usecase.repository.channel import ChannelListRepository
from channel.usecase.models import (
    ChannelListInDsDto,
    DeviceListInDsDto
)
from channel.usecase.output_port.channel import ChannelListOututPort

from channel.usecase.models import (
    ChannelListInDto,
    ChannelListOutDto,
    ChannelListDataOutDto,
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthorizedException,
    UnauthenticateException
)
from channel.entity.models import Channel

from pydantic import ValidationError
from typing import Optional


class ChannelListInteractor(ChannelListInputPort):

    def __init__(
            self,
            gateway: ChannelListRepository,
            presenter: ChannelListOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def list(
            self, channel_dto: ChannelListInDto) -> ChannelListOutDto:

        try:

            # ユーザ認証チェック
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthenticateException

            # Device検索
            devices = self.gateway.list_device(
                DeviceListInDsDto(
                    user_id=session_user_ds_dto.id
                )
            )

            # Channel検索
            channel_out_ds_dtos = self.gateway.list(
                ChannelListInDsDto(
                    device_ids=[device.id for device in devices]
                )
            )

            # 変換
            out_dto = ChannelListOutDto(
                values=[
                    ChannelListDataOutDto(**ds_dto.model_dump())
                    for ds_dto in channel_out_ds_dtos
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
