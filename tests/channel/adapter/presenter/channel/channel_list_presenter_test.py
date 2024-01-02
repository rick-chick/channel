from channel.adapter.presenter.channel import (
    ChannelListPresenter)
from channel.usecase.models import ChannelListOutDto
from tests.channel.adapter.presenter.channel.channel_list_view_impl import ChannelListViewImpl
from tests.channel.factories import ChannelListOutDtoFactory


def test_prepare_success_view():
    view = ChannelListViewImpl()
    target = ChannelListPresenter(view)
    channel = ChannelListOutDtoFactory.build()
    target.prepare_success_view(channel)

    assert view.channel_list_out_dto == channel


def test_prepare_fail_view():
    view = ChannelListViewImpl()
    target = ChannelListPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
