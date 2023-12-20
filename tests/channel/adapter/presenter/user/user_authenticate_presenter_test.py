from channel.adapter.presenter.user.user_authenticate_presenter import (
    UserAuthenticatePresenter
)
from tests.channel.factories import UserAuthenticateOutDtoFactory
from tests.channel.adapter.presenter.user.user_authenticate_view_impl import (
    UserAuthenticateViewImpl
)


def test_prepare_success_view():
    view = UserAuthenticateViewImpl()
    target = UserAuthenticatePresenter(view)
    user = UserAuthenticateOutDtoFactory.build()
    target.prepare_success_view(user)

    view.user_authenticate_out_dto == user


def test_prepare_fail_view():
    view = UserAuthenticateViewImpl()
    target = UserAuthenticatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
