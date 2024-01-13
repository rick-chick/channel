from channel.adapter.presenter.user.user_reset_password_view import (
    UserResetPasswordView
)

from channel.usecase.models import UserResetPasswordOutDto
from typing import List


class UserResetPasswordViewImpl(UserResetPasswordView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_reset_password_out_dto: UserResetPasswordOutDto):
        self.user_reset_password_out_dto = user_reset_password_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_reset_password_out_dto)
