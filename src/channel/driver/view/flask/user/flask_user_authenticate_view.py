from typing import Any
from channel.adapter.presenter.user.user_authenticate_view import UserAuthenticateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import UserAuthenticateOutDto


class FlaskUserAuthenticateView(UserAuthenticateView):

    def __init__(self):
        self.exceptions = []
        self.user_token: Any = None

    def add_result(self, user_authenticate_out_dto: UserAuthenticateOutDto):
        self.user = user_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.user, self.exceptions).json()
