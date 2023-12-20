from channel.adapter.presenter.user_token.user_token_authenticate_view import UserTokenAuthenticateView
from channel.usecase.models import UserTokenAuthenticateOutDto


class CliUserTokenAuthenticateView(UserTokenAuthenticateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, user_token_authenticate_out_dto: UserTokenAuthenticateOutDto):
        self.user_token = user_token_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user_token)
