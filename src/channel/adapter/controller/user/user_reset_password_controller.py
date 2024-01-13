from channel.adapter.controller.user.user_create_controller import UserCreateController
from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.adapter.gateway.user import (
    UserResetPasswordGateway,
    UserSession,
    UserRepository
)
from channel.adapter.presenter.user.user_reset_password_presenter import UserResetPasswordPresenter
from channel.adapter.presenter.user.user_reset_password_view import UserResetPasswordView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.user import UserResetPasswordInteractor
from channel.usecase.models import (
    UserResetPasswordInDto,
    UserResetPasswordOutDto
)
from channel.adapter.controller.input_parser import InputParser


class UserResetPasswordController(Handler):

    def __init__(
        self,
        user_repository: UserRepository,
        signup_repository: SignupRepository,
        user_reset_password_view: UserResetPasswordView,
        user_reset_password_input_parser: InputParser,
    ):
        self.gateway = UserResetPasswordGateway(
            user_repository=user_repository,
            signup_repository=signup_repository,
        )

        self.parser = user_reset_password_input_parser
        self.view = user_reset_password_view
        presenter = UserResetPasswordPresenter(self.view)

        self.user_reset_password_interactor = UserResetPasswordInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: UserResetPasswordInDto
    ) -> UserResetPasswordOutDto:
        out_dto = self.user_reset_password_interactor.reset_password(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
