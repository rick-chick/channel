from channel.adapter.presenter.user.user_signup_view import (
    UserSignupView
)

from channel.usecase.models import UserSignupOutDto
from typing import List


class UserSignupViewImpl(UserSignupView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_signup_out_dto: UserSignupOutDto):
        self.user_signup_out_dto = user_signup_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_signup_out_dto)
