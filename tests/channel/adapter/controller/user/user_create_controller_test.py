from tests.channel.factories import UserCreateInDtoFactory
from tests.channel.adapter.controller.user.user_create_controller_impl import user_create_controller_impl


def test_success():
    user_create_controller_impl.handle(UserCreateInDtoFactory.build())
