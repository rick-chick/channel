from channel.driver.view.cli.channel.cli_channel_delete_view import CliChannelDeleteView
from tests.channel.factories import ChannelDeleteOutDtoFactory


def test_success():
    target = CliChannelDeleteView()
    target.add_result(ChannelDeleteOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliChannelDeleteView()
    target.add_exception(Exception())
    target.render()
