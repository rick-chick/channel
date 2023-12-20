from abc import ABC, abstractmethod
from channel.usecase.models import UserUpdateOutDto


class UserUpdateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user: UserUpdateOutDto) -> UserUpdateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
