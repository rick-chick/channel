from channel.driver.view.cli.record.cli_record_create_view import CliRecordCreateView
from tests.channel.factories import RecordCreateOutDtoFactory


def test_success():
    target = CliRecordCreateView()
    target.add_result(RecordCreateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliRecordCreateView()
    target.add_exception(Exception())
    target.render()
