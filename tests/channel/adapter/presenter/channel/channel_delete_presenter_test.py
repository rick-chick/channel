from channel.adapter.presenter.channel.channel_delete_presenter import (
    ChannelDeletePresenter
)
from tests.channel.factories import ChannelDeleteOutDtoFactory
from tests.channel.adapter.presenter.channel.channel_delete_view_impl import (
    ChannelDeleteViewImpl
)


def test_prepare_success_view():
    view = ChannelDeleteViewImpl()
    target = ChannelDeletePresenter(view)
    channel = ChannelDeleteOutDtoFactory.build()
    target.prepare_success_view(channel)

    assert view.channel_delete_out_dto == channel


def test_prepare_fail_view():
    view = ChannelDeleteViewImpl()
    target = ChannelDeletePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
