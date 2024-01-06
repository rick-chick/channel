from typing import Any
from channel.adapter.presenter.user_token.user_token_refresh_view import UserTokenRefreshView
from channel.usecase.models import UserTokenRefreshOutDto


class CliUserTokenRefreshView(UserTokenRefreshView):

    def __init__(self):
        self.exceptions = []
        self.user_token: Any = None

    def add_result(self, user_token_refresh_out_dto: UserTokenRefreshOutDto):
        self.user_token = user_token_refresh_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user_token)
