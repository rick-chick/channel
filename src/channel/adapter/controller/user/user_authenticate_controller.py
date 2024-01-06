from typing import Any

from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.user_token.user_token_repository import UserTokenRepository
from channel.adapter.gateway.user import (
    UserAuthenticateGateway,
    UserRepository,
    UserSession,
)
from channel.adapter.presenter.user.user_authenticate_presenter import (
    UserAuthenticatePresenter,
)
from channel.adapter.presenter.user.user_authenticate_view import UserAuthenticateView
from channel.usecase.interactor.user import UserAuthenticateInteractor
from channel.usecase.models import UserAuthenticateOutDto


class UserAuthenticateController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        user_repository: UserRepository,
        user_authenticate_view: UserAuthenticateView,
        user_authenticate_input_parser: InputParser
    ):
        self.gateway = UserAuthenticateGateway(
            user_repository=user_repository,
            user_session=user_session
        )

        self.parser = user_authenticate_input_parser
        self.view = user_authenticate_view
        presenter = UserAuthenticatePresenter(self.view)

        self.user_authenticate_interactor = UserAuthenticateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: Any
    ) -> UserAuthenticateOutDto:
        out_dto = self.user_authenticate_interactor.authenticate(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
