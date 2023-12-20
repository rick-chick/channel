from channel.adapter.controller.user.user_authenticate_controller import (
    UserAuthenticateController,
)
from channel.entity.models import User
from tests.channel.adapter.controller.user.user_authenticate_input_parser_impl import (
    UserAuthenticateInputParserImpl,
)
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.presenter.user.user_authenticate_view_impl import (
    UserAuthenticateViewImpl,
)
from tests.channel.factories import UserAuthenticateInDtoFactory, UserOutDsDtoFactory


def test_success():

    user = User(
        password='hogehuga',
        **UserOutDsDtoFactory.build().model_dump()
    )
    user.hash_password()

    user_repository = UserRepositoryImpl()
    user_repository.find_by_email_out = UserOutDsDtoFactory.build(
        password_hash=user.password_hash
    )

    input_parser = UserAuthenticateInputParserImpl()
    input_parser.parse_out = UserAuthenticateInDtoFactory.build(
        password=user.password
    )
    target = UserAuthenticateController(
        user_authenticate_input_parser=input_parser,
        user_session=UserSessionImpl(),
        user_repository=user_repository,
        user_authenticate_view=UserAuthenticateViewImpl()
    )

    target.handle(
        UserAuthenticateInDtoFactory.build(
            password=user.password
        )
    )
