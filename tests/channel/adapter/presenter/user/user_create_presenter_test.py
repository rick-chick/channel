from channel.adapter.presenter.user.user_create_presenter import (
    UserCreatePresenter
)
from tests.channel.factories import UserCreateOutDtoFactory
from tests.channel.adapter.presenter.user.user_create_view_impl import (
    UserCreateViewImpl
)


def test_prepare_success_view():
    view = UserCreateViewImpl()
    target = UserCreatePresenter(view)
    user = UserCreateOutDtoFactory.build()
    target.prepare_success_view(user)

    view.user_create_out_dto == user


def test_prepare_fail_view():
    view = UserCreateViewImpl()
    target = UserCreatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
