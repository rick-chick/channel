from channel.adapter.gateway.mail.mail_service import MailService
from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.adapter.gateway.user import (
    UserSignupGateway,
)
from channel.adapter.gateway.user.user_repository import UserRepository
from channel.adapter.presenter.user.user_signup_presenter import (
    UserSignupPresenter
)
from channel.adapter.presenter.user.user_signup_view import UserSignupView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.user import UserSignupInteractor
from channel.usecase.models import (
    UserSignupInDto,
    UserSignupOutDto
)
from channel.adapter.controller.input_parser import InputParser


class UserSignupController(Handler):

    def __init__(
        self,
        signup_repository: SignupRepository,
        mail_service: MailService,
        user_repository: UserRepository,
        user_signup_input_parser: InputParser,
        user_signup_view: UserSignupView,
        password_reset_url: str,
    ):
        self.gateway = UserSignupGateway(
            signup_repository=signup_repository,
            mail_service=mail_service,
            user_repository=user_repository,
            password_reset_url=password_reset_url,
        )

        self.parser = user_signup_input_parser
        self.view = user_signup_view
        presenter = UserSignupPresenter(self.view)

        self.user_signup_interactor = UserSignupInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: UserSignupInDto
    ) -> UserSignupOutDto:
        out_dto = self.user_signup_interactor.signup(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
