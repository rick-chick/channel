from abc import ABC, abstractmethod
from channel.usecase.models import ChannelListOutDto


class ChannelListOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, channel: ChannelListOutDto) -> ChannelListOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
