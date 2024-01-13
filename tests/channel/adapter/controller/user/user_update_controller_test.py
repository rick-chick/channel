from tests.channel.adapter.controller.user.user_update_controller_impl import user_update_controller_impl
from tests.channel.factories import UserUpdateInDtoFactory


def test_success():
    user_update_controller_impl.handle(UserUpdateInDtoFactory.build())
