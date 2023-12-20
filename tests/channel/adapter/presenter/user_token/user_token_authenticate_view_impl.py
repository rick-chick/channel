from channel.adapter.presenter.user_token.user_token_authenticate_view import (
    UserTokenAuthenticateView
)

from channel.usecase.models import UserTokenAuthenticateOutDto
from typing import List


class UserTokenAuthenticateViewImpl(UserTokenAuthenticateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, user_token_authenticate_out_dto: UserTokenAuthenticateOutDto):
        self.user_token_authenticate_out_dto = user_token_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.user_token_authenticate_out_dto)
