from channel.usecase.input_port.channel import ChannelUpdateInputPort
from channel.usecase.repository.channel import ChannelUpdateRepository
from channel.usecase.models import (
    ChannelUpdateInDsDto
)
from channel.usecase.output_port.channel import ChannelUpdateOututPort

from channel.usecase.models import (
    ChannelUpdateInDto,
    ChannelUpdateOutDto
)
from channel.usecase.exception import (
    BusinessException,
    ChannelNotFoundException,
    ValidationException,
    UnauthorizedException
)
from channel.entity.models import Channel

from pydantic import ValidationError


class ChannelUpdateInteractor(ChannelUpdateInputPort):

    def __init__(
            self,
            gateway: ChannelUpdateRepository,
            presenter: ChannelUpdateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def update(
            self, channel_dto: ChannelUpdateInDto) -> ChannelUpdateOutDto:

        try:

            # 現在のChannelの取得
            channel_ds_dto = self.gateway.find_channel_by_id(channel_dto.id)
            if not channel_ds_dto:
                raise ChannelNotFoundException

            # ユーザの確認
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            # None以外のフィールドをマージする
            channel = Channel.model_validate({
                **channel_ds_dto.model_dump(),
                **channel_dto.model_dump(exclude_none=True)
            })

            # 更新
            channel_res_ds_dto = self.gateway.update(
                ChannelUpdateInDsDto(
                    **channel.model_dump(),
                    updated_by=session_user_ds_dto.id,
                )
            )
            if not channel_res_ds_dto:
                raise ChannelNotFoundException

            # 出力データ構築
            channel_out_dto = ChannelUpdateOutDto(
                **channel_res_ds_dto.model_dump()
            )

            self.presenter.prepare_success_view(channel_out_dto)

            return channel_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
