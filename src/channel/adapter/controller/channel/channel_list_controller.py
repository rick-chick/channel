from channel.adapter.gateway.channel import (
    ChannelListGateway,
    UserSession,
    ChannelRepository
)
from channel.adapter.gateway.device.device_repository import DeviceRepository
from channel.adapter.presenter.channel.channel_list_presenter import ChannelListPresenter
from channel.adapter.presenter.channel.channel_list_view import ChannelListView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.channel import ChannelListInteractor
from channel.usecase.models import (
    ChannelListInDto,
    ChannelListOutDto
)
from channel.adapter.controller.input_parser import InputParser


class ChannelListController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        channel_repository: ChannelRepository,
        device_repository: DeviceRepository,
        channel_list_view: ChannelListView,
        channel_list_input_parser: InputParser,
    ):
        self.gateway = ChannelListGateway(
            channel_repository=channel_repository,
            device_repository=device_repository,
            user_session=user_session,
        )

        self.parser = channel_list_input_parser
        self.view = channel_list_view
        presenter = ChannelListPresenter(self.view)

        self.channel_list_interactor = ChannelListInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: ChannelListInDto
    ) -> ChannelListOutDto:
        out_dto = self.channel_list_interactor.list(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
