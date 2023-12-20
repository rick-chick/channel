from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.device import DeviceRepository
from channel.adapter.gateway.device.device_authenticate_gateway import (
    DeviceAuthenticateGateway,
)
from channel.adapter.gateway.device.device_session import DeviceSession
from channel.adapter.presenter.device.device_authenticate_presenter import (
    DeviceAuthenticatePresenter,
)
from channel.adapter.presenter.device.device_authenticate_view import (
    DeviceAuthenticateView,
)
from channel.usecase.interactor.device import DeviceAuthenticateInteractor
from channel.usecase.models import DeviceAuthenticateInDto, DeviceAuthenticateOutDto


class DeviceAuthenticateController(Handler):

    def __init__(
        self,
        device_session: DeviceSession,
        device_repository: DeviceRepository,
        device_authenticate_view: DeviceAuthenticateView,
        device_authenticate_input_parser: InputParser,
    ):
        self.gateway = DeviceAuthenticateGateway(
            device_repository=device_repository,
            device_session=device_session,
        )

        self.parser = device_authenticate_input_parser
        self.view = device_authenticate_view
        presenter = DeviceAuthenticatePresenter(self.view)

        self.device_authenticate_interactor = DeviceAuthenticateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: DeviceAuthenticateInDto
    ) -> DeviceAuthenticateOutDto:
        out_dto = self.device_authenticate_interactor.authenticate(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
