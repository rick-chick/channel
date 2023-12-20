from channel.usecase.output_port.user import UserAuthenticateOututPort
from channel.usecase.models import UserAuthenticateOutDto
from channel.adapter.presenter.user.user_authenticate_view import UserAuthenticateView


class UserAuthenticatePresenter(UserAuthenticateOututPort):

    def __init__(
        self,
        user_authenticate_view: UserAuthenticateView
    ):
        self.user_authenticate_view = user_authenticate_view

    def prepare_success_view(self, user: UserAuthenticateOutDto) -> UserAuthenticateOutDto:
        self.user_authenticate_view.add_result(user)
        return user

    def prepare_fail_view(self, exception: Exception):
        self.user_authenticate_view.add_exception(exception)
