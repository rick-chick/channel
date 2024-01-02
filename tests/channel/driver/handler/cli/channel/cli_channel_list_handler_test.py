from pytest import raises


def test_fail():
    with raises(SystemExit):
        import channel.driver.handler.cli.channel.cli_channel_list_handler
