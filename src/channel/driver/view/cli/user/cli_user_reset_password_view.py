from typing import Any
from channel.adapter.presenter.user.user_reset_password_view import UserResetPasswordView
from channel.usecase.models import UserResetPasswordOutDto


class CliUserResetPasswordView(UserResetPasswordView):

    def __init__(self):
        self.exceptions = []
        self.user: Any = None

    def add_result(self, user_reset_password_out_dto: UserResetPasswordOutDto):
        self.user = user_reset_password_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user)
