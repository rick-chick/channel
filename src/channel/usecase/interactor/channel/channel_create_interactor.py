from typing import Optional

from pydantic import ValidationError

from channel.entity.models import Channel
from channel.usecase.exception import (
    BusinessException,
    UnauthenticateException,
    ValidationException,
)
from channel.usecase.input_port.channel import ChannelCreateInputPort
from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateInDto,
    ChannelCreateOutDto,
    UserSessionDsDto,
)
from channel.usecase.output_port.channel import ChannelCreateOututPort
from channel.usecase.repository.channel import ChannelCreateRepository


class ChannelCreateInteractor(ChannelCreateInputPort):

    def __init__(
            self,
            gateway: ChannelCreateRepository,
            presenter: ChannelCreateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def create(
            self, channel_dto: ChannelCreateInDto) -> ChannelCreateOutDto:

        try:

            channel = Channel(**channel_dto.model_dump())

            session_user_ds_dto: Optional[UserSessionDsDto] =\
                self.gateway.load_session_user()

            if not session_user_ds_dto:
                raise UnauthenticateException

            channel_ds_dto = ChannelCreateInDsDto(
                **channel.model_dump(),
                created_by=session_user_ds_dto.id,
                updated_by=session_user_ds_dto.id,
            )

            channel_res_ds_dto = self.gateway.create(channel_ds_dto)

            channel_out_dto = ChannelCreateOutDto(
                **channel_res_ds_dto.model_dump()
            )

            self.presenter.prepare_success_view(
                channel_out_dto)

            return channel_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
