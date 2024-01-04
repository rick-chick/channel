from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from channel.adapter.gateway.device import (
    DeviceDeleteGateway,
    UserSession,
    DeviceRepository
)
from channel.adapter.gateway.record.record_repository import RecordRepository
from channel.adapter.presenter.device.device_delete_presenter import DeviceDeletePresenter
from channel.adapter.presenter.device.device_delete_view import DeviceDeleteView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.device import DeviceDeleteInteractor
from channel.usecase.models import (
    DeviceDeleteInDto,
    DeviceDeleteOutDto
)
from channel.adapter.controller.input_parser import InputParser


class DeviceDeleteController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        device_repository: DeviceRepository,
        channel_repository: ChannelRepository,
        record_repository: RecordRepository,
        device_delete_view: DeviceDeleteView,
        device_delete_input_parser: InputParser,
    ):
        self.gateway = DeviceDeleteGateway(
            device_repository=device_repository,
            channel_repository=channel_repository,
            record_repository=record_repository,
            user_session=user_session,
        )

        self.parser = device_delete_input_parser
        self.view = device_delete_view
        presenter = DeviceDeletePresenter(self.view)

        self.device_delete_interactor = DeviceDeleteInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: DeviceDeleteInDto
    ) -> DeviceDeleteOutDto:
        out_dto = self.device_delete_interactor.delete(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
