from abc import ABC, abstractmethod
from channel.usecase.models import UserTokenRefreshOutDto


class UserTokenRefreshOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, user_token: UserTokenRefreshOutDto) -> UserTokenRefreshOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
