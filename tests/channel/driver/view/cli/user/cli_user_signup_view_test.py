from channel.driver.view.cli.user.cli_user_signup_view import CliUserSignupView
from tests.channel.factories import UserSignupOutDtoFactory


def test_success():
    target = CliUserSignupView()
    target.add_result(UserSignupOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliUserSignupView()
    target.add_exception(Exception())
    target.render()
