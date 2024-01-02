from channel.adapter.presenter.device import (
    DeviceListPresenter)
from channel.usecase.models import DeviceListOutDto
from tests.channel.adapter.presenter.device.device_list_view_impl import DeviceListViewImpl


def test_prepare_success_view():
    view = DeviceListViewImpl()
    target = DeviceListPresenter(view)
    device = DeviceListOutDto()
    target.prepare_success_view(device)

    assert view.device_list_out_dto == device


def test_prepare_fail_view():
    view = DeviceListViewImpl()
    target = DeviceListPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
