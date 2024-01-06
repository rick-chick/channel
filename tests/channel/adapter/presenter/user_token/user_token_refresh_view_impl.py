from channel.adapter.presenter.user_token.user_token_refresh_view import (
    UserTokenRefreshView
)

from channel.usecase.models import UserTokenRefreshOutDto
from typing import List


class UserTokenRefreshViewImpl(UserTokenRefreshView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_token_refresh_out_dto: UserTokenRefreshOutDto):
        self.user_token_refresh_out_dto = user_token_refresh_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_token_refresh_out_dto)
