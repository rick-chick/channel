from abc import abstractmethod
from channel.usecase.models import UserResetPasswordOutDto
from channel.adapter.presenter.renderer import Renderer
from typing import Optional


class UserResetPasswordView(Renderer):

    @abstractmethod
    def add_result(self, user_reset_password_out_dto: UserResetPasswordOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
