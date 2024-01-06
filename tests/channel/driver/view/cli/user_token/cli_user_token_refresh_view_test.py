from channel.driver.view.cli.user_token.cli_user_token_refresh_view import CliUserTokenRefreshView
from tests.channel.factories import UserTokenRefreshOutDtoFactory


def test_success():
    target = CliUserTokenRefreshView()
    target.add_result(UserTokenRefreshOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserTokenRefreshView()
    target.add_exception(Exception())
    target.render()
