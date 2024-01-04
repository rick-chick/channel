from pytest import raises


def test_fail():
    with raises(SystemExit):
        import channel.driver.handler.cli.device.cli_device_delete_handler
