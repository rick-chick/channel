from channel.driver.view.cli.user.cli_user_update_view import CliUserUpdateView
from tests.channel.factories import UserUpdateOutDtoFactory


def test_success():
    target = CliUserUpdateView()
    target.add_result(UserUpdateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserUpdateView()
    target.add_exception(Exception())
    target.render()
