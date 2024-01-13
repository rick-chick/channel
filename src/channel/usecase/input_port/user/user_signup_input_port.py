from abc import ABC, abstractmethod
from channel.usecase.models import (
        UserSignupInDto, UserSignupOutDto)


class UserSignupInputPort(ABC):

    @abstractmethod
    def signup(self, user_dto: UserSignupInDto) -> UserSignupOutDto:
        pass
