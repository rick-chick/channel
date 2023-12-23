from channel.adapter.presenter.record import (
    RecordListPresenter
)
from record_list_view_impl import RecordListViewImpl
from tests.channel.factories import RecordListOutDtoFactory


def test_prepare_success_view():
    view = RecordListViewImpl()
    target = RecordListPresenter(view)
    record = RecordListOutDtoFactory.build()
    target.prepare_success_view(record)

    assert view.record_list_out_dto == record


def test_prepare_fail_view():
    view = RecordListViewImpl()
    target = RecordListPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
