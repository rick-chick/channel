from channel.adapter.presenter.user.user_create_view import (
    UserCreateView
)

from channel.usecase.models import UserCreateOutDto
from typing import List


class UserCreateViewImpl(UserCreateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_create_out_dto: UserCreateOutDto):
        self.user_create_out_dto = user_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_create_out_dto)
