from channel.usecase.output_port.user_token import UserTokenAuthenticateOututPort
from channel.usecase.models import UserTokenAuthenticateOutDto
from channel.adapter.presenter.user_token.user_token_authenticate_view import (
    UserTokenAuthenticateView
)


class UserTokenAuthenticatePresenter(UserTokenAuthenticateOututPort):

    def __init__(
        self,
        user_token_authenticate_view: UserTokenAuthenticateView
    ):
        self.user_token_authenticate_view = user_token_authenticate_view

    def prepare_success_view(self, user_token: UserTokenAuthenticateOutDto):
        self.user_token_authenticate_view.add_result(user_token)

    def prepare_fail_view(self, exception: Exception):
        self.user_token_authenticate_view.add_exception(exception)
