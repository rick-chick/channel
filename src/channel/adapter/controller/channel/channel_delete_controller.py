from channel.adapter.gateway.channel import (
    ChannelDeleteGateway,
    UserSession,
    ChannelRepository
)
from channel.adapter.presenter.channel.channel_delete_presenter import ChannelDeletePresenter
from channel.adapter.presenter.channel.channel_delete_view import ChannelDeleteView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.channel import ChannelDeleteInteractor
from channel.usecase.models import (
    ChannelDeleteInDto,
    ChannelDeleteOutDto
)
from channel.adapter.controller.input_parser import InputParser


class ChannelDeleteController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        channel_repository: ChannelRepository,
        channel_delete_view: ChannelDeleteView,
        channel_delete_input_parser: InputParser,
    ):
        self.gateway = ChannelDeleteGateway(
            channel_repository=channel_repository,
            user_session=user_session,
        )

        self.parser = channel_delete_input_parser
        self.view = channel_delete_view
        presenter = ChannelDeletePresenter(self.view)

        self.channel_delete_interactor = ChannelDeleteInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: ChannelDeleteInDto
    ) -> ChannelDeleteOutDto:
        out_dto = self.channel_delete_interactor.delete(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
