from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from channel.adapter.gateway.device import (
    DeviceListGateway,
    UserSession,
    DeviceRepository
)
from channel.adapter.presenter.device.device_list_presenter import DeviceListPresenter
from channel.adapter.presenter.device.device_list_view import DeviceListView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.device import DeviceListInteractor
from channel.usecase.models import (
    DeviceListInDto,
    DeviceListOutDto
)
from channel.adapter.controller.input_parser import InputParser


class DeviceListController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        device_repository: DeviceRepository,
        channel_repository: ChannelRepository,
        device_list_view: DeviceListView,
        device_list_input_parser: InputParser,
    ):
        self.gateway = DeviceListGateway(
            device_repository=device_repository,
            channel_repository=channel_repository,
            user_session=user_session,
        )

        self.parser = device_list_input_parser
        self.view = device_list_view
        presenter = DeviceListPresenter(self.view)

        self.device_list_interactor = DeviceListInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: DeviceListInDto
    ) -> DeviceListOutDto:
        out_dto = self.device_list_interactor.list(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
