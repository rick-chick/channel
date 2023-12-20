from channel.driver.view.flask.user.flask_user_update_view import FlaskUserUpdateView
from tests.channel.factories import UserUpdateOutDtoFactory


def test_success():
    target = FlaskUserUpdateView()
    target.add_result(UserUpdateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskUserUpdateView()
    target.add_exception(Exception())
    assert target.render() is not None
