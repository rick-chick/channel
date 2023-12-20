from channel.adapter.presenter.user.user_authenticate_view import UserAuthenticateView
from channel.usecase.models import UserAuthenticateOutDto


class CliUserAuthenticateView(UserAuthenticateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, user_authenticate_out_dto: UserAuthenticateOutDto):
        self.user = user_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        if self.user:
            print(self.user)
