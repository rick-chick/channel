from abc import ABC, abstractmethod

from channel.usecase.models import UserUpdateInDto, UserUpdateOutDto


class UserUpdateInputPort(ABC):

    @abstractmethod
    def update(self, user_dto: UserUpdateInDto) -> UserUpdateOutDto:
        pass
