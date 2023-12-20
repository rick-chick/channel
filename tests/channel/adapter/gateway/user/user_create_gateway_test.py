from channel.adapter.gateway.user import UserCreateGateway
from tests.channel.adapter.gateway.user.user_repository_impl import (
    UserRepositoryImpl,
)
from tests.channel.adapter.gateway.user.user_session_impl import (
    UserSessionImpl,
)
from tests.channel.factories import (
    UserCreateInDsDtoFactory,
)


def test_create_success():

    user_repository = UserRepositoryImpl()
    target = UserCreateGateway(
        user_repository=user_repository,
        user_session=UserSessionImpl(),
    )

    in_dto = UserCreateInDsDtoFactory.build()

    target.create(in_dto)
    assert user_repository.create_in == in_dto


def test_exists_user_by_email():

    user_repository = UserRepositoryImpl()
    target = UserCreateGateway(
        user_repository=user_repository,
        user_session=UserSessionImpl(),
    )
    email = 'email@test.com'
    target.exists_user_by_email(email)
    assert user_repository.exists_by_email_in == email


def test_load_session_user():
    user_session = UserSessionImpl()
    target = UserCreateGateway(
        user_repository=UserRepositoryImpl(),
        user_session=user_session,
    )
    target.load_session_user()
    assert user_session.load_called
