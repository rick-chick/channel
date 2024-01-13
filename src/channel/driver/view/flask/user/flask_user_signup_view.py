from typing import Any
from channel.adapter.presenter.user.user_signup_view import UserSignupView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import UserSignupOutDto


class FlaskUserSignupView(UserSignupView):

    def __init__(self):
        self.exceptions = []
        self.user: Any = None

    def add_result(self, user_signup_out_dto: UserSignupOutDto):
        self.user = user_signup_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.user, self.exceptions).json()
