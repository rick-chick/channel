from pytest import raises


def test_fail():
    with raises(SystemExit):
        import channel.driver.handler.cli.record.cli_record_list_handler
