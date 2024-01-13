from channel.usecase.output_port.user import UserSignupOututPort
from channel.usecase.models import UserSignupOutDto
from channel.adapter.presenter.user.user_signup_view import UserSignupView


class UserSignupPresenter(UserSignupOututPort):

    def __init__(
        self,
        user_signup_view: UserSignupView
    ):
        self.user_signup_view = user_signup_view

    def prepare_success_view(
        self, user: UserSignupOutDto
    ) -> UserSignupOutDto:
        self.user_signup_view.add_result(user)
        return user

    def prepare_fail_view(
        self,
        exception: Exception
    ):
        self.user_signup_view.add_exception(exception)
