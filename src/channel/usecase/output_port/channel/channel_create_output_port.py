from abc import ABC, abstractmethod
from channel.usecase.models import ChannelCreateOutDto


class ChannelCreateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, channel: ChannelCreateOutDto) -> ChannelCreateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
