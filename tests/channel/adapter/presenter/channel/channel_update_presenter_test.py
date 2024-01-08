from channel.adapter.presenter.channel.channel_update_presenter import (
    ChannelUpdatePresenter
)
from tests.channel.factories import ChannelUpdateOutDtoFactory
from tests.channel.adapter.presenter.channel.channel_update_view_impl import (
    ChannelUpdateViewImpl
)


def test_prepare_success_view():
    view = ChannelUpdateViewImpl()
    target = ChannelUpdatePresenter(view)
    channel = ChannelUpdateOutDtoFactory.build()
    target.prepare_success_view(channel)

    assert view.channel_update_out_dto == channel


def test_prepare_fail_view():
    view = ChannelUpdateViewImpl()
    target = ChannelUpdatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
