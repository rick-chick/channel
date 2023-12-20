from typing import Any
from channel.adapter.presenter.user.user_update_view import UserUpdateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import UserUpdateOutDto


class FlaskUserUpdateView(UserUpdateView):

    def __init__(self):
        self.exceptions = []
        self.user: Any = None

    def add_result(self, user_update_out_dto: UserUpdateOutDto):
        self.user = user_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.user, self.exceptions).json()
