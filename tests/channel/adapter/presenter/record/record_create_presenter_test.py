from channel.adapter.presenter.record.record_create_presenter import (
    RecordCreatePresenter
)
from channel.usecase.models import RecordCreateOutDto
from tests.channel.factories import RecordCreateOutDtoFactory
from tests.channel.adapter.presenter.record.record_create_view_impl import (
    RecordCreateViewImpl
)


def test_prepare_success_view():
    view = RecordCreateViewImpl()
    target = RecordCreatePresenter(view)
    record = RecordCreateOutDtoFactory.build()
    target.prepare_success_view(record)

    assert view.record_create_out_dto == record


def test_prepare_fail_view():
    view = RecordCreateViewImpl()
    target = RecordCreatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
