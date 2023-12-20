from channel.driver.view.cli.user.cli_user_authenticate_view import CliUserAuthenticateView
from tests.channel.factories import UserAuthenticateOutDtoFactory


def test_success():
    target = CliUserAuthenticateView()
    target.add_result(UserAuthenticateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserAuthenticateView()
    target.add_exception(Exception())
    target.render()
