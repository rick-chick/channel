from channel.usecase.models import UserResetPasswordOutDto
from channel.adapter.presenter.user.user_reset_password_view import UserResetPasswordView
from channel.usecase.output_port.user.user_reset_password_output_port import UserResetPasswordOututPort


class UserResetPasswordPresenter(UserResetPasswordOututPort):

    def __init__(
        self,
        user_reset_password_view: UserResetPasswordView
    ):
        self.user_reset_password_view = user_reset_password_view

    def prepare_success_view(
        self, user: UserResetPasswordOutDto
    ) -> UserResetPasswordOutDto:
        self.user_reset_password_view.add_result(user)
        return user

    def prepare_fail_view(
        self,
        exception: Exception
    ):
        self.user_reset_password_view.add_exception(exception)
