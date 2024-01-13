from abc import abstractmethod
from channel.usecase.models import UserSignupOutDto
from channel.adapter.presenter.renderer import Renderer
from typing import Optional


class UserSignupView(Renderer):

    @abstractmethod
    def add_result(self, user_signup_out_dto: UserSignupOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
