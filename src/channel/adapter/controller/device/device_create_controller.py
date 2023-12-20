from typing import Any

from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.device import (
    DeviceCreateGateway,
    DeviceRepository,
    UserSession,
)
from channel.adapter.presenter.device import DeviceCreatePresenter
from channel.adapter.presenter.device.device_create_view import DeviceCreateView
from channel.usecase.interactor.device import DeviceCreateInteractor
from channel.usecase.models import DeviceCreateOutDto


class DeviceCreateController(Handler):

    def __init__(
        self,
            input_parser: InputParser,
            user_session: UserSession,
            device_repository: DeviceRepository,
            device_view: DeviceCreateView,
    ):
        gateway = DeviceCreateGateway(
            device_repository=device_repository,
            user_session=user_session,
        )

        self.view = device_view
        presenter = DeviceCreatePresenter(device_view)

        self.device_create_interactor = DeviceCreateInteractor(
            gateway=gateway,
            presenter=presenter
        )

        self.input_parser = input_parser

    def handle(
        self,
        dto: Any
    ) -> DeviceCreateOutDto:
        out_dto = self.device_create_interactor.create(
            self.input_parser.parse(dto)
        )
        self.view.render()
        return out_dto
