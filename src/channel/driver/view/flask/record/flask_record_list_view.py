from typing import Any
from channel.adapter.presenter.record.record_list_view import RecordListView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import RecordListOutDto


class FlaskRecordListView(RecordListView):

    def __init__(self):
        self.exceptions = []
        self.record: Any = None

    def add_result(self, record_list_out_dto: RecordListOutDto):
        self.record = record_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.record, self.exceptions).json()
