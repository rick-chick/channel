from abc import abstractmethod
from typing import Any
from channel.usecase.models import UserAuthenticateOutDto
from channel.adapter.presenter.renderer import Renderer


class UserAuthenticateView(Renderer):

    @abstractmethod
    def add_result(self, user_authenticate_out_dto: UserAuthenticateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self) -> Any:
        pass
