from channel.adapter.presenter.user.user_update_view import (
    UserUpdateView
)

from channel.usecase.models import UserUpdateOutDto
from typing import List


class UserUpdateViewImpl(UserUpdateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_update_out_dto: UserUpdateOutDto):
        self.user_update_out_dto = user_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_update_out_dto)
        return self.user_update_out_dto
