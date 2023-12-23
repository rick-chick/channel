from abc import ABC, abstractmethod
from channel.usecase.models import (
        RecordListInDto, RecordListOutDto)


class RecordListInputPort(ABC):

    @abstractmethod
    def list(self, record_dto: RecordListInDto) -> RecordListOutDto:
        pass
