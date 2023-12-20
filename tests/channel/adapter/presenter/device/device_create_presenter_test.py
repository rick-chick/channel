from channel.adapter.presenter.device import (
    DeviceCreatePresenter)
from tests.channel.factories import DeviceCreateOutDtoFactory
from tests.channel.adapter.presenter.device.device_create_view_impl import (
    DeviceCreateViewImpl
)


def test_prepare_success_view():
    view = DeviceCreateViewImpl()
    target = DeviceCreatePresenter(view)
    device = DeviceCreateOutDtoFactory.build()
    target.prepare_success_view(device)

    assert view.device_create_out_dto == device



def test_prepare_fail_view():
    view = DeviceCreateViewImpl()
    target = DeviceCreatePresenter(view)

    target.prepare_fail_view(Exception())
    assert len(view.exceptions) > 0

