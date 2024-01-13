from typing import Any
from channel.adapter.presenter.user.user_reset_password_view import UserResetPasswordView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import UserResetPasswordOutDto


class FlaskUserResetPasswordView(UserResetPasswordView):

    def __init__(self):
        self.exceptions = []
        self.user: Any = None

    def add_result(self, user_reset_password_out_dto: UserResetPasswordOutDto):
        self.user = user_reset_password_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.user, self.exceptions).json()
