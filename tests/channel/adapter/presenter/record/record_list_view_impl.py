from channel.adapter.presenter.record.record_list_view import (
    RecordListView
)

from channel.usecase.models import RecordListOutDto
from typing import List


class RecordListViewImpl(RecordListView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, record_list_out_dto: RecordListOutDto):
        self.record_list_out_dto = record_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.record_list_out_dto)
