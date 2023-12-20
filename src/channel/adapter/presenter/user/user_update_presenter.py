from channel.usecase.output_port.user import UserUpdateOututPort
from channel.usecase.models import UserUpdateOutDto
from channel.adapter.presenter.user.user_update_view import UserUpdateView


class UserUpdatePresenter(UserUpdateOututPort):

    def __init__(
        self,
        user_update_view: UserUpdateView
    ):
        self.user_update_view = user_update_view

    def prepare_success_view(
        self, user_update_out_dto: UserUpdateOutDto
    ):
        self.user_update_view.add_result(user_update_out_dto)
        return user_update_out_dto

    def prepare_fail_view(self, exception: Exception):
        self.user_update_view.add_exception(exception)
