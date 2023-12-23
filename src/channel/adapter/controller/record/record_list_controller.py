from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from channel.adapter.gateway.record import (
    RecordListGateway,
    UserSession,
    RecordRepository
)
from channel.adapter.presenter.record.record_list_presenter import RecordListPresenter
from channel.adapter.presenter.record.record_list_view import RecordListView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.record import RecordListInteractor
from channel.usecase.models import (
    RecordListInDto,
    RecordListOutDto
)
from channel.adapter.controller.input_parser import InputParser


class RecordListController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        record_repository: RecordRepository,
        channel_repository: ChannelRepository,
        record_list_view: RecordListView,
        record_list_input_parser: InputParser,
    ):
        self.gateway = RecordListGateway(
            record_repository=record_repository,
            channel_repository=channel_repository,
            user_session=user_session,
        )

        self.parser = record_list_input_parser
        self.view = record_list_view
        presenter = RecordListPresenter(self.view)

        self.record_list_interactor = RecordListInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: RecordListInDto
    ) -> RecordListOutDto:
        out_dto = self.record_list_interactor.list(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
