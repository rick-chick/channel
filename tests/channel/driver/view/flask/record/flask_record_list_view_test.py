from channel.driver.view.flask.record.flask_record_list_view import FlaskRecordListView
from tests.channel.factories import RecordListOutDtoFactory


def test_success():
    target = FlaskRecordListView()
    target.add_result(RecordListOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskRecordListView()
    target.add_exception(Exception())
    assert target.render() is not None
