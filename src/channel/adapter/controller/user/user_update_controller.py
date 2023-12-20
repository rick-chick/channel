from channel.adapter.gateway.user import (
    UserUpdateGateway,
    UserSession,
    UserRepository
)
from channel.adapter.presenter.user.user_update_presenter import UserUpdatePresenter
from channel.adapter.presenter.user.user_update_view import UserUpdateView
from channel.adapter.controller.handler import Handler
from channel.usecase.interactor.user import UserUpdateInteractor
from channel.usecase.models import (
    UserUpdateInDto,
    UserUpdateOutDto
)
from channel.adapter.controller.input_parser import InputParser


class UserUpdateController(Handler):

    def __init__(
        self,
            user_session: UserSession,
            user_repository: UserRepository,
        user_update_view: UserUpdateView,
        user_update_input_parser: InputParser,
    ):
        self.gateway = UserUpdateGateway(
            user_repository=user_repository,
            user_session=user_session,
        )

        self.parser = user_update_input_parser
        self.view = user_update_view
        presenter = UserUpdatePresenter(self.view)

        self.user_update_interactor = UserUpdateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: UserUpdateInDto
    ) -> UserUpdateOutDto:
        out_dto = self.user_update_interactor.update(
          self.parser.parse(dto)
        )
        self.view.render()
        return out_dto
