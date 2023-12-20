from channel.driver.view.flask.user_token.flask_user_token_authenticate_view import FlaskUserTokenAuthenticateView
from tests.channel.factories import UserTokenAuthenticateOutDtoFactory


def test_success():
    target = FlaskUserTokenAuthenticateView()
    target.add_result(UserTokenAuthenticateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskUserTokenAuthenticateView()
    target.add_exception(Exception())
    assert target.render() is not None
