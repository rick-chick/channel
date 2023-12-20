from channel.driver.view.cli.user.cli_user_create_view import CliUserCreateView
from tests.channel.factories import UserCreateOutDtoFactory


def test_success():
    target = CliUserCreateView()
    target.add_result(UserCreateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserCreateView()
    target.add_exception(Exception())
    target.render()
