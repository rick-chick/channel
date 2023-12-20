from abc import abstractmethod
from channel.usecase.models import UserUpdateOutDto
from channel.adapter.presenter.renderer import Renderer


class UserUpdateView(Renderer):

    @abstractmethod
    def add_result(self, user_update_out_dto: UserUpdateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
