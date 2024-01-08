from abc import ABC, abstractmethod
from channel.usecase.models import (ChannelDeleteInDto, ChannelDeleteOutDto)

from typing import List


class ChannelDeleteInputPort(ABC):

    @abstractmethod
    def delete(
        self,
        channel_dto: ChannelDeleteInDto
    ) -> ChannelDeleteOutDto:
        pass
