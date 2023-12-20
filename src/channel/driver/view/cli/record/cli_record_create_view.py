from channel.adapter.presenter.record.record_create_view import RecordCreateView
from channel.usecase.models import RecordCreateOutDto


class CliRecordCreateView(RecordCreateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, record_create_out_dto: RecordCreateOutDto):
        self.record = record_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.record)
