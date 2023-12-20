from typing import Any

from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.adapter.gateway.user.user_repository import UserRepository
from channel.adapter.gateway.user_token import UserSession, UserTokenAuthenticateGateway
from channel.adapter.presenter.user_token.user_token_authenticate_presenter import (
    UserTokenAuthenticatePresenter,
)
from channel.adapter.presenter.user_token.user_token_authenticate_view import (
    UserTokenAuthenticateView,
)
from channel.usecase.interactor.user_token import UserTokenAuthenticateInteractor
from channel.usecase.models import UserTokenAuthenticateOutDto


class UserTokenAuthenticateController(Handler):

    def __init__(
        self,
        user_session: UserSession,
        user_repository: UserRepository,
        user_token_authenticate_view: UserTokenAuthenticateView,
        input_parser: InputParser
    ):
        self.gateway = UserTokenAuthenticateGateway(
            user_session=user_session,
            user_repository=user_repository,
        )

        self.input_parser = input_parser
        self.view = user_token_authenticate_view
        presenter = UserTokenAuthenticatePresenter(self.view)

        self.user_token_authenticate_interactor = UserTokenAuthenticateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(self, dto: Any) -> UserTokenAuthenticateOutDto:
        out_dto = self.user_token_authenticate_interactor.authenticate(
            self.input_parser.parse(dto)
        )
        self.view.render()
        return out_dto
