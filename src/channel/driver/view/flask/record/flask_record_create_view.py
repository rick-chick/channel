from typing import Any
from channel.adapter.presenter.record.record_create_view import RecordCreateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import RecordCreateOutDto


class FlaskRecordCreateView(RecordCreateView):

    def __init__(self):
        self.exceptions = []
        self.record: Any = None

    def add_result(self, record_create_out_dto: RecordCreateOutDto):
        self.record = record_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.record, self.exceptions).json()
