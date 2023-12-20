from typing import Any
from channel.adapter.presenter.user_token.user_token_authenticate_view import UserTokenAuthenticateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import UserTokenAuthenticateOutDto


class FlaskUserTokenAuthenticateView(UserTokenAuthenticateView):

    def __init__(self):
        self.exceptions = []
        self.user_token: Any = None

    def add_result(self, user_token_create_out_dto: UserTokenAuthenticateOutDto):
        self.user_token = user_token_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.user_token, self.exceptions).json()
