from channel.adapter.presenter.user.user_authenticate_view import (
    UserAuthenticateView
)

from channel.usecase.models import UserAuthenticateOutDto
from typing import List


class UserAuthenticateViewImpl(UserAuthenticateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_authenticate_out_dto: UserAuthenticateOutDto):
        self.user_authenticate_out_dto = user_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_authenticate_out_dto)
