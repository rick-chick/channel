from channel.adapter.presenter.user.user_signup_presenter import (
    UserSignupPresenter
)
from tests.channel.factories import UserSignupOutDtoFactory
from tests.channel.adapter.presenter.user.user_signup_view_impl import (
    UserSignupViewImpl
)


def test_prepare_success_view():
    view = UserSignupViewImpl()
    target = UserSignupPresenter(view)
    user = UserSignupOutDtoFactory.build()
    target.prepare_success_view(user)

    assert view.user_signup_out_dto == user


def test_prepare_fail_view():
    view = UserSignupViewImpl()
    target = UserSignupPresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
