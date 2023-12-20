from abc import ABC, abstractmethod
from channel.usecase.models import UserAuthenticateOutDto


class UserAuthenticateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user: UserAuthenticateOutDto) -> UserAuthenticateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
