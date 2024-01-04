from channel.adapter.presenter.device.device_delete_presenter import (
    DeviceDeletePresenter
)
from tests.channel.factories import DeviceDeleteOutDtoFactory
from tests.channel.adapter.presenter.device.device_delete_view_impl import (
    DeviceDeleteViewImpl
)


def test_prepare_success_view():
    view = DeviceDeleteViewImpl()
    target = DeviceDeletePresenter(view)
    device = DeviceDeleteOutDtoFactory.build()
    target.prepare_success_view(device)

    assert view.device_delete_out_dto == device


def test_prepare_fail_view():
    view = DeviceDeleteViewImpl()
    target = DeviceDeletePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
