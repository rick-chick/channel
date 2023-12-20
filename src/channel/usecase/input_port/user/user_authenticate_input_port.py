from abc import ABC, abstractmethod
from channel.usecase.models import (
    UserAuthenticateInDto,
    UserAuthenticateOutDto,
)


class UserAuthenticateInputPort(ABC):

    @abstractmethod
    def authenticate(self, user_in_dto: UserAuthenticateInDto) -> UserAuthenticateOutDto:
        pass
