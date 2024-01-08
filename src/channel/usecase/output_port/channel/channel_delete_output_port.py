from abc import ABC, abstractmethod
from channel.usecase.models import ChannelDeleteOutDto

from typing import List


class ChannelDeleteOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, channel_dto: ChannelDeleteOutDto) -> ChannelDeleteOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
