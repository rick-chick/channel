from abc import ABC, abstractmethod
from channel.usecase.models import RecordListOutDto


class RecordListOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, record: RecordListOutDto) -> RecordListOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
