from abc import ABC, abstractmethod
from channel.usecase.models import (
        RecordCreateInDto, RecordCreateOutDto)


class RecordCreateInputPort(ABC):

    @abstractmethod
    def create(self, record_dto: RecordCreateInDto) -> RecordCreateOutDto:
        pass
