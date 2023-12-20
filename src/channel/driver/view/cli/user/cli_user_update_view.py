from channel.adapter.presenter.user.user_update_view import UserUpdateView
from channel.usecase.models import UserUpdateOutDto


class CliUserUpdateView(UserUpdateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, user_update_out_dto: UserUpdateOutDto):
        self.user = user_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user)
