from abc import ABC, abstractmethod
from channel.usecase.models import UserSignupOutDto


class UserSignupOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user: UserSignupOutDto) -> UserSignupOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
