from channel.driver.view.cli.record.cli_record_list_view import CliRecordListView
from tests.channel.factories import RecordListOutDtoFactory


def test_success():
    target = CliRecordListView()
    target.add_result(RecordListOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliRecordListView()
    target.add_exception(Exception())
    target.render()
