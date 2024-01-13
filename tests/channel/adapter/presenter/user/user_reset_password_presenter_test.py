from channel.adapter.presenter.user import (
    UserResetPasswordPresenter)
from tests.channel.factories import UserResetPasswordOutDtoFactory
from tests.channel.adapter.presenter.user.user_reset_password_view_impl import (
    UserResetPasswordViewImpl
)


def test_prepare_success_view():
    view = UserResetPasswordViewImpl()
    target = UserResetPasswordPresenter(view)
    user = UserResetPasswordOutDtoFactory.build()
    target.prepare_success_view(user)

    assert view.user_reset_password_out_dto == user


def test_prepare_fail_view():
    view = UserResetPasswordViewImpl()
    target = UserResetPasswordPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
