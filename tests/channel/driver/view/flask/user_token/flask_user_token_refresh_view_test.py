from channel.driver.view.flask.user_token.flask_user_token_refresh_view import FlaskUserTokenRefreshView
from tests.channel.factories import UserTokenRefreshOutDtoFactory


def test_success():
    target = FlaskUserTokenRefreshView()
    target.add_result(UserTokenRefreshOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskUserTokenRefreshView()
    target.add_exception(Exception())
    assert target.render() is not None
