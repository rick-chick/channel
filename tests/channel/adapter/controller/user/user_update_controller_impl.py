from channel.adapter.controller.user.user_update_controller import UserUpdateController
from tests.channel.adapter.controller.user.user_update_input_parser_impl import UserUpdateInputParserImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.presenter.user.user_update_view_impl import UserUpdateViewImpl

user_repository = UserRepositoryImpl()
user_repository.exists_user_by_id_out = True

user_update_controller_impl = UserUpdateController(
    user_session=UserSessionImpl(),
    user_repository=user_repository,
    user_update_view=UserUpdateViewImpl(),
    user_update_input_parser=UserUpdateInputParserImpl()
)
