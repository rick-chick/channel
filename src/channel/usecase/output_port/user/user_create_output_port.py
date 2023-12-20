from abc import ABC, abstractmethod
from channel.usecase.models import UserCreateOutDto


class UserCreateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(
        self, user_create_out_dto: UserCreateOutDto
    ) -> UserCreateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
