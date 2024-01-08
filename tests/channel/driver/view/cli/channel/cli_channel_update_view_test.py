from channel.driver.view.cli.channel.cli_channel_update_view import CliChannelUpdateView
from tests.channel.factories import ChannelUpdateOutDtoFactory


def test_success():
    target = CliChannelUpdateView()
    target.add_result(ChannelUpdateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliChannelUpdateView()
    target.add_exception(Exception())
    target.render()
