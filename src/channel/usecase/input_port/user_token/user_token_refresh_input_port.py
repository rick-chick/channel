from abc import ABC, abstractmethod
from channel.usecase.models import (
        UserTokenRefreshInDto, UserTokenRefreshOutDto)


class UserTokenRefreshInputPort(ABC):

    @abstractmethod
    def refresh(self, user_token_dto: UserTokenRefreshInDto) -> UserTokenRefreshOutDto:
        pass
