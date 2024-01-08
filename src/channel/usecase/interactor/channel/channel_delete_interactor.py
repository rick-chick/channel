from channel.usecase.input_port.channel import ChannelDeleteInputPort
from channel.usecase.repository.channel import ChannelDeleteRepository
from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDto,
)
from channel.usecase.output_port.channel import ChannelDeleteOututPort

from channel.usecase.models import ChannelDeleteInDto
from channel.usecase.exception import (
    BusinessException, ValidationException, UnauthorizedException)

from pydantic import ValidationError


class ChannelDeleteInteractor(ChannelDeleteInputPort):

    def __init__(
        self,
        gateway: ChannelDeleteRepository,
        presenter: ChannelDeleteOututPort
    ):
        self.gateway = gateway
        self.presenter = presenter

    def delete(
        self,
        channel_dto: ChannelDeleteInDto
    ) -> ChannelDeleteOutDto:

        try:
            if not channel_dto:
                return ChannelDeleteOutDto()

            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            channel_ds_dtos = self.gateway.delete(
                ChannelDeleteInDsDto(
                    **channel_dto.model_dump()
                )
            )

            result = ChannelDeleteOutDto(
                ids=[
                    channel.id for channel in channel_ds_dtos
                    if channel.id is not None
                ]
            )

            self.presenter.prepare_success_view(result)

            return result

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
