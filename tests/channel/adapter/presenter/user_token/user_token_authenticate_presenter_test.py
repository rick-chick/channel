from channel.adapter.presenter.user_token import (
    UserTokenAuthenticatePresenter)
from tests.channel.factories import UserTokenAuthenticateOutDtoFactory
from tests.channel.adapter.presenter.user_token.user_token_authenticate_view_impl import (
    UserTokenAuthenticateViewImpl
)


def test_prepare_success_view():
    view = UserTokenAuthenticateViewImpl()
    target = UserTokenAuthenticatePresenter(view)
    user_token = UserTokenAuthenticateOutDtoFactory.build()
    target.prepare_success_view(user_token)

    assert view.user_token_authenticate_out_dto == user_token


def test_prepare_fail_view():
    view = UserTokenAuthenticateViewImpl()
    target = UserTokenAuthenticatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
