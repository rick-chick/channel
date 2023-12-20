from abc import ABC, abstractmethod
from channel.usecase.models import RecordCreateOutDto


class RecordCreateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, record: RecordCreateOutDto) -> RecordCreateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
