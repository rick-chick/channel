from abc import abstractmethod
from channel.usecase.models import UserTokenAuthenticateOutDto
from channel.adapter.presenter.renderer import Renderer


class UserTokenAuthenticateView(Renderer):

    @abstractmethod
    def add_result(self, user_token_authenticate_out_dto: UserTokenAuthenticateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
