from channel.adapter.presenter.user_token import (
    UserTokenRefreshPresenter)
from tests.channel.factories import UserTokenRefreshOutDtoFactory
from tests.channel.adapter.presenter.user_token.user_token_refresh_view_impl import (
    UserTokenRefreshViewImpl
)


def test_prepare_success_view():
    view = UserTokenRefreshViewImpl()
    target = UserTokenRefreshPresenter(view)
    user_token = UserTokenRefreshOutDtoFactory.build()
    target.prepare_success_view(user_token)

    assert view.user_token_refresh_out_dto == user_token


def test_prepare_fail_view():
    view = UserTokenRefreshViewImpl()
    target = UserTokenRefreshPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
