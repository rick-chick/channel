from channel.adapter.presenter.user.user_update_presenter import (
    UserUpdatePresenter
)
from tests.channel.factories import UserUpdateOutDtoFactory
from tests.channel.adapter.presenter.user.user_update_view_impl import (
    UserUpdateViewImpl
)


def test_prepare_success_view():
    view = UserUpdateViewImpl()
    target = UserUpdatePresenter(view)
    user = UserUpdateOutDtoFactory.build()
    target.prepare_success_view(user)

    view.user_update_out_dto == user


def test_prepare_fail_view():
    view = UserUpdateViewImpl()
    target = UserUpdatePresenter(view)
    target.prepare_fail_view(Exception())

    assert len(view.exceptions) > 0
