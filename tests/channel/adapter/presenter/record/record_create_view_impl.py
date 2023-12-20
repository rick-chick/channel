from channel.adapter.presenter.record.record_create_view import RecordCreateView
from channel.usecase.models import RecordCreateOutDto


class RecordCreateViewImpl(RecordCreateView):

    record_create_out_dto: RecordCreateOutDto

    def __init__(self):
        self.exceptions  = []

    def add_result(self, record_create_out_dto: RecordCreateOutDto):
        self.record_create_out_dto = record_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.record_create_out_dto)
