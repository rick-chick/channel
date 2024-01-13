from abc import ABC, abstractmethod
from channel.usecase.models import UserResetPasswordOutDto


class UserResetPasswordOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user: UserResetPasswordOutDto) -> UserResetPasswordOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
