from pytest import raises


def test_fail():
    with raises(SystemExit):
        import channel.driver.handler.cli.user_token.cli_user_token_refresh_handler
