from channel.adapter.presenter.record.record_create_view import RecordCreateView
from channel.usecase.output_port.record import RecordCreateOututPort
from channel.usecase.models import RecordCreateOutDto


class RecordCreatePresenter(RecordCreateOututPort):

    def __init__(
        self,
        record_create_view: RecordCreateView
    ):
        self.record_create_view = record_create_view

    def prepare_success_view(self, record: RecordCreateOutDto) -> RecordCreateOutDto:
        self.record_create_view.add_result(record)
        return record

    def prepare_fail_view(self, exception: Exception):
        self.record_create_view.add_exception(exception)
