from channel.adapter.gateway.user.user_repository import UserRepository
from channel.adapter.gateway.user_token import (
    UserTokenRefreshGateway,
    UserSession,
    UserTokenRepository
)
from channel.adapter.presenter.user_token.user_token_refresh_presenter import UserTokenRefreshPresenter
from channel.adapter.presenter.user_token.user_token_refresh_view import UserTokenRefreshView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.user_token import UserTokenRefreshInteractor
from channel.usecase.models import (
    UserTokenRefreshInDto,
    UserTokenRefreshOutDto
)
from channel.adapter.controller.input_parser import InputParser


class UserTokenRefreshController(Handler):

    def __init__(
        self,
        user_token_repository: UserTokenRepository,
        user_repository: UserRepository,
        user_token_refresh_view: UserTokenRefreshView,
        user_token_refresh_input_parser: InputParser,
    ):
        self.gateway = UserTokenRefreshGateway(
            user_token_repository=user_token_repository,
            user_repository=user_repository,
        )

        self.parser = user_token_refresh_input_parser
        self.view = user_token_refresh_view
        presenter = UserTokenRefreshPresenter(self.view)

        self.user_token_refresh_interactor = UserTokenRefreshInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: UserTokenRefreshInDto
    ) -> UserTokenRefreshOutDto:
        out_dto = self.user_token_refresh_interactor.refresh(
            self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
