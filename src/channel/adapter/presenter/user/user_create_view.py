from abc import abstractmethod
from channel.usecase.models import UserCreateOutDto
from channel.adapter.presenter.renderer import Renderer


class UserCreateView(Renderer):

    @abstractmethod
    def add_result(self, user_create_out_dto: UserCreateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
