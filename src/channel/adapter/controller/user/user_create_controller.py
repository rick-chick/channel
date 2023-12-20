from channel.adapter.gateway.user import (
    UserCreateGateway,
    UserSession,
    UserRepository
)
from channel.adapter.presenter.user.user_create_presenter import UserCreatePresenter
from channel.adapter.presenter.user.user_create_view import UserCreateView
from channel.adapter.controller.handler import Handler
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.interactor.user import UserCreateInteractor
from channel.usecase.models import (
    UserCreateInDto,
    UserCreateOutDto
)


class UserCreateController(Handler):

    def __init__(
        self,
        user_create_input_parser: InputParser,
        user_session: UserSession,
        user_repository: UserRepository,
        user_create_view: UserCreateView,
    ):
        self.gateway = UserCreateGateway(
            user_repository=user_repository,
            user_session=user_session,
        )

        self.input_parser = user_create_input_parser
        self.view = user_create_view
        presenter = UserCreatePresenter(self.view)

        self.user_create_interactor = UserCreateInteractor(
            gateway=self.gateway,
            presenter=presenter,
        )

    def handle(
        self,
        dto: UserCreateInDto
    ) -> UserCreateOutDto:
        out_dto = self.user_create_interactor.create(
            self.input_parser.parse(dto)
        )
        self.view.render()
        return out_dto
