from abc import abstractmethod
from channel.usecase.models import UserTokenRefreshOutDto
from channel.adapter.presenter.renderer import Renderer
from typing import Optional


class UserTokenRefreshView(Renderer):

    @abstractmethod
    def add_result(self, user_token_refresh_out_dto: UserTokenRefreshOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
