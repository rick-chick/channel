from channel.adapter.controller.user_token.user_token_authenticate_controller import UserTokenAuthenticateController
from channel.entity.models import User
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.user_token.user_token_repository_impl import UserTokenRepositoryImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.presenter.user_token.user_token_authenticate_view_impl import UserTokenAuthenticateViewImpl
from tests.channel.factories import (
    UserTokenAuthenticateInDtoFactory,
    UserOutDsDtoFactory
)
from tests.channel.adapter.controller.user_token.user_token_authenticate_input_parser_impl import UserTokenAuthenticateInputParserImpl


def test_success():
    user_repository = UserRepositoryImpl()
    usr_out_ds_dto = UserOutDsDtoFactory.build()

    # ユーザ作ってトークンを得る
    user = User(**usr_out_ds_dto.model_dump())
    token = user.create_jwt()

    # ユーザトークンからIDを得たとして、そのIDからユーザを得る
    user_repository.find_user_by_id_out = usr_out_ds_dto

    # ユーザがセッションに保存されることを確認する用
    user_session = UserSessionImpl()


    # トークン認証用の入力
    input_parser = UserTokenAuthenticateInputParserImpl()
    input_parser.parse_out = UserTokenAuthenticateInDtoFactory.build(
        token=token
    )

    target = UserTokenAuthenticateController(
        input_parser=input_parser,
        user_session=user_session,
        user_repository=user_repository,
        user_token_authenticate_view=UserTokenAuthenticateViewImpl()
    )

    target.handle(None)

    assert user_session.save_in.id == user.id
