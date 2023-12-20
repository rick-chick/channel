from channel.driver.view.cli.user_token.cli_user_token_authenticate_view import CliUserTokenAuthenticateView
from tests.channel.factories import UserTokenAuthenticateOutDtoFactory


def test_success():
    target = CliUserTokenAuthenticateView()
    target.add_result(UserTokenAuthenticateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserTokenAuthenticateView()
    target.add_exception(Exception())
    target.render()
