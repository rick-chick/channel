from channel.driver.view.flask.user.flask_user_signup_view import FlaskUserSignupView
from tests.channel.factories import UserSignupOutDtoFactory


def test_success():
    target = FlaskUserSignupView()
    target.add_result(UserSignupOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskUserSignupView()
    target.add_exception(Exception())
    assert target.render() is not None
