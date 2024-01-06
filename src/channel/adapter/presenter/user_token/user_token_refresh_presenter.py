from channel.usecase.output_port.user_token import UserTokenRefreshOututPort
from channel.usecase.models import UserTokenRefreshOutDto
from channel.adapter.presenter.user_token.user_token_refresh_view import UserTokenRefreshView


class UserTokenRefreshPresenter(UserTokenRefreshOututPort):

    def __init__(
        self,
        user_token_refresh_view: UserTokenRefreshView
    ):
        self.user_token_refresh_view = user_token_refresh_view

    def prepare_success_view(
        self, user_token_refresh_out_dto: UserTokenRefreshOutDto
    ):
        self.user_token_refresh_view.add_result(user_token_refresh_out_dto)
        return user_token_refresh_out_dto

    def prepare_fail_view(self, exception: Exception):
        self.user_token_refresh_view.add_exception(exception)
