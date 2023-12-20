from abc import ABC, abstractmethod
from channel.usecase.models import UserTokenAuthenticateOutDto


class UserTokenAuthenticateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user_token: UserTokenAuthenticateOutDto) -> UserTokenAuthenticateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, error: Exception):
        pass
