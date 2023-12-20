from abc import ABC, abstractmethod
from channel.usecase.models import (
    UserCreateInDto, UserCreateOutDto)


class UserCreateInputPort(ABC):

    @abstractmethod
    def create(self, user_dto: UserCreateInDto) -> UserCreateOutDto:
        pass
