from channel.driver.view.flask.record.flask_record_create_view import FlaskRecordCreateView
from tests.channel.factories import RecordCreateOutDtoFactory


def test_success():
    target = FlaskRecordCreateView()
    target.add_result(RecordCreateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskRecordCreateView()
    target.add_exception(Exception())
    assert target.render() is not None
