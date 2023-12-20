from channel.adapter.presenter.device.device_authenticate_presenter import DeviceAuthenticatePresenter
from tests.channel.factories import DeviceAuthenticateOutDtoFactory
from tests.channel.adapter.presenter.device.device_authenticate_view_impl import (
  DeviceAuthenticateViewImpl
)


def test_prepare_success_view():
    view = DeviceAuthenticateViewImpl()
    target = DeviceAuthenticatePresenter(view)
    device = DeviceAuthenticateOutDtoFactory.build()
    target.prepare_success_view(device)

    assert view.device_authenticate_out_dto == device

def test_prepare_fail_view():
    view = DeviceAuthenticateViewImpl()
    target = DeviceAuthenticatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
