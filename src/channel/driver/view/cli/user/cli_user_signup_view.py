from typing import Any
from channel.adapter.presenter.user.user_signup_view import UserSignupView
from channel.usecase.models import UserSignupOutDto


class CliUserSignupView(UserSignupView):

    def __init__(self):
        self.exceptions = []
        self.user: Any = None

    def add_result(self, user_signup_out_dto: UserSignupOutDto):
        self.user = user_signup_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user)
