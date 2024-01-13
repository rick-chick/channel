from pytest import raises


def test_fail():
    with raises(SystemExit):
        import channel.driver.handler.cli.user.cli_user_reset_password_handler
