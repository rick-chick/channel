from channel.driver.view.cli.user.cli_user_reset_password_view import CliUserResetPasswordView
from tests.channel.factories import UserResetPasswordOutDtoFactory


def test_success():
    target = CliUserResetPasswordView()
    target.add_result(UserResetPasswordOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserResetPasswordView()
    target.add_exception(Exception())
    target.render()
