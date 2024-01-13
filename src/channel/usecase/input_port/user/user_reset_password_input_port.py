from abc import ABC, abstractmethod
from channel.usecase.models import (
        UserResetPasswordInDto, UserResetPasswordOutDto)


class UserResetPasswordInputPort(ABC):

    @abstractmethod
    def reset_password(self, user_dto: UserResetPasswordInDto) -> UserResetPasswordOutDto:
        pass
