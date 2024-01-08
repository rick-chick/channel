from abc import ABC, abstractmethod
from channel.usecase.models import ChannelUpdateOutDto


class ChannelUpdateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, channel: ChannelUpdateOutDto) -> ChannelUpdateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
