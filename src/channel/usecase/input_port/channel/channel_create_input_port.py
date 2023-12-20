from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelCreateInDto, ChannelCreateOutDto)


class ChannelCreateInputPort(ABC):

    @abstractmethod
    def create(self, channel_dto: ChannelCreateInDto) -> ChannelCreateOutDto:
        pass
