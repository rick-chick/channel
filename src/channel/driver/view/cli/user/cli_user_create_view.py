from channel.adapter.presenter.user.user_create_view import UserCreateView
from channel.usecase.models import UserCreateOutDto


class CliUserCreateView(UserCreateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, user_craete_out_dto: UserCreateOutDto):
        self.user = user_craete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.user)
