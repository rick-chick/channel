from typing import Any

from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.device.device_session import DeviceSession
from channel.adapter.gateway.record import (
    RecordCreateGateway,
    RecordRepository,
    UserSession,
)
from channel.adapter.presenter.record import RecordCreateView
from channel.adapter.presenter.record.record_create_presenter import (
    RecordCreatePresenter,
)
from channel.usecase.interactor.record import RecordCreateInteractor
from channel.usecase.models import RecordCreateOutDto


class RecordCreateController(Handler):

    def __init__(
        self,
            user_session: UserSession,
            record_repository: RecordRepository,
            device_session: DeviceSession,
            record_view: RecordCreateView,
            input_parser: InputParser
    ):

        self.input_parser = input_parser
        gateway = RecordCreateGateway(
            record_repository=record_repository,
            device_session=device_session,
            user_session=user_session,
        )
        self.view = record_view
        presenter = RecordCreatePresenter(record_view)

        self.record_create_interactor = RecordCreateInteractor(
            gateway=gateway,
            presenter=presenter
        )

    def handle(
        self,
        dto: Any
    ) -> RecordCreateOutDto:
        out_dto = self.record_create_interactor.create(
            self.input_parser.parse(dto)
        )
        self.view.render()
        return out_dto
