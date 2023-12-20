from channel.adapter.presenter.channel import (
    ChannelCreatePresenter)
from tests.channel.factories import ChannelCreateOutDtoFactory
from tests.channel.adapter.presenter.channel.channel_create_view_impl import ChannelCreateViewImpl


def test_prepare_success_view():
    view = ChannelCreateViewImpl()
    target = ChannelCreatePresenter(view)
    channel = ChannelCreateOutDtoFactory.build()

    target.prepare_success_view(channel)

    assert view.channel_create_out_dto == channel


def test_prepare_fail_view():
    view = ChannelCreateViewImpl()
    target = ChannelCreatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
