from channel.usecase.output_port.record import RecordListOututPort
from channel.usecase.models import RecordListOutDto
from channel.adapter.presenter.record.record_list_view import RecordListView


class RecordListPresenter(RecordListOututPort):

    def __init__(
        self,
        record_list_view: RecordListView
    ):
        self.record_list_view = record_list_view

    def prepare_success_view(
        self, record: RecordListOutDto
    ):
        self.record_list_view.add_result(record)
        return record

    def prepare_fail_view(self, exception: Exception):
        self.record_list_view.add_exception(exception)
