from abc import ABC, abstractmethod
from channel.usecase.models import (
        ChannelUpdateInDto, ChannelUpdateOutDto)


class ChannelUpdateInputPort(ABC):

    @abstractmethod
    def update(self, channel_dto: ChannelUpdateInDto) -> ChannelUpdateOutDto:
        pass
