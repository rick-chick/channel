from typing import Any
from channel.driver.view.cli.channel.cli_channel_list_view import CliChannelListView
from tests.channel.factories import ChannelListOutDtoFactory


def test_success():
    target = CliChannelListView()
    target.add_result(ChannelListOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliChannelListView()
    target.add_exception(Exception())
    target.render()
