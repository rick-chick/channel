from channel.adapter.gateway.channel import (
    ChannelUpdateGateway,
    UserSession,
    ChannelRepository
)
from channel.adapter.presenter.channel.channel_update_presenter import ChannelUpdatePresenter
from channel.adapter.presenter.channel.channel_update_view import ChannelUpdateView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.channel import ChannelUpdateInteractor
from channel.usecase.models import (
    ChannelUpdateInDto,
    ChannelUpdateOutDto
)
from channel.adapter.controller.input_parser import InputParser


class ChannelUpdateController(Handler):

    def __init__(
        self,
            user_session: UserSession,
            channel_repository: ChannelRepository,
            channel_update_view: ChannelUpdateView,
            channel_update_input_parser: InputParser,
    ):
        self.gateway = ChannelUpdateGateway(
            channel_repository=channel_repository,
            user_session=user_session,
        )

        self.parser = channel_update_input_parser
        self.view = channel_update_view
        presenter = ChannelUpdatePresenter(self.view)

        self.channel_update_interactor = ChannelUpdateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: ChannelUpdateInDto
    ) -> ChannelUpdateOutDto:
        out_dto = self.channel_update_interactor.update(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
