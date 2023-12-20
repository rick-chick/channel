from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.channel import (
    ChannelCreateGateway, UserSession, ChannelRepository
)
from channel.adapter.presenter.channel import ChannelCreatePresenter
from channel.adapter.controller.handler import Handler
from channel.adapter.presenter.channel.channel_create_view import ChannelCreateView
from channel.usecase.interactor.channel import ChannelCreateInteractor
from channel.usecase.models import ChannelCreateOutDto


class ChannelCreateController(Handler):

    def __init__(
        self,
            user_session: UserSession,
            channel_repository: ChannelRepository,
            channel_view: ChannelCreateView,
            parser: InputParser,
    ):
        self.parser = parser
        gateway = ChannelCreateGateway(
            channel_repository=channel_repository,
            user_session=user_session,
        )
        self.view = channel_view
        self.presenter = ChannelCreatePresenter(channel_view)

        self.channel_create_interactor = ChannelCreateInteractor(
            gateway=gateway,
            presenter=self.presenter
        )

    def handle(
        self,
        dto: Any
    ) -> ChannelCreateOutDto:
        out_dto = self.channel_create_interactor.create(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
