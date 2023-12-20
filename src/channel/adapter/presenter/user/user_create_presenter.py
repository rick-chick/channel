from channel.usecase.output_port.user import UserCreateOututPort
from channel.usecase.models import UserCreateOutDto
from channel.adapter.presenter.user.user_create_view import UserCreateView


class UserCreatePresenter(UserCreateOututPort):

    def __init__(
        self,
        user_create_view: UserCreateView
    ):
        self.user_create_view = user_create_view

    def prepare_success_view(
        self, user_create_out_dto: UserCreateOutDto
    ):
        self.user_create_view.add_result(user_create_out_dto)
        return user_create_out_dto

    def prepare_fail_view(self, exception: Exception):
        self.user_create_view.add_exception(exception)
