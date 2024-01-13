from channel.driver.view.flask.user.flask_user_reset_password_view import FlaskUserResetPasswordView
from tests.channel.factories import UserResetPasswordOutDtoFactory


def test_success():
    target = FlaskUserResetPasswordView()
    target.add_result(UserResetPasswordOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskUserResetPasswordView()
    target.add_exception(Exception())
    assert target.render() is not None
