from abc import ABC, abstractmethod
from channel.usecase.models import (
        ChannelListInDto, ChannelListOutDto)


class ChannelListInputPort(ABC):

    @abstractmethod
    def list(self, channel_dto: ChannelListInDto) -> ChannelListOutDto:
        pass
