from channel.adapter.controller.user.user_create_controller import (
    UserCreateController
)
from tests.channel.adapter.gateway.user.user_session_impl import (
    UserSessionImpl
)
from tests.channel.adapter.gateway.user.user_repository_impl import (
    UserRepositoryImpl
)
from tests.channel.adapter.presenter.user.user_create_view_impl import (
    UserCreateViewImpl
)
from tests.channel.factories import UserCreateInDtoFactory
from tests.channel.adapter.controller.user.user_create_input_parser_impl import (
    UserCreateInputParserImpl
)


def test_success():
    target = UserCreateController(
        user_create_input_parser=UserCreateInputParserImpl(),
        user_session=UserSessionImpl(),
        user_repository=UserRepositoryImpl(),
        user_create_view=UserCreateViewImpl()
    )
    target.handle(UserCreateInDtoFactory.build())
