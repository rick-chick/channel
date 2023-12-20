from abc import ABC, abstractmethod
from channel.usecase.models import (
        UserTokenAuthenticateInDto, UserTokenAuthenticateOutDto)


class UserTokenAuthenticateInputPort(ABC):

    @abstractmethod
    def authenticate(self, user_token_dto: UserTokenAuthenticateInDto) -> UserTokenAuthenticateOutDto:
        pass
