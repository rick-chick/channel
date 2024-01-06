from channel.usecase.input_port.user_token import UserTokenRefreshInputPort
from channel.usecase.repository.user_token import UserTokenRefreshRepository
from channel.usecase.output_port.user_token import UserTokenRefreshOututPort

from channel.usecase.models import (
    UserTokenCreateInDsDto,
    UserTokenDeleteInDsDto,
    UserTokenRefreshInDto,
    UserTokenRefreshOutDto,
)
from channel.usecase.exception import (
    BusinessException, UnauthenticateException, ValidationException)

from channel.entity.models import User, UserToken

from pydantic import ValidationError
from datetime import datetime, timedelta


class UserTokenRefreshInteractor(UserTokenRefreshInputPort):

    def __init__(
        self,
        gateway: UserTokenRefreshRepository,
        presenter: UserTokenRefreshOututPort
    ):
        self.gateway = gateway
        self.presenter = presenter

    def refresh(
        self,
        user_token_dto: UserTokenRefreshInDto
    ) -> UserTokenRefreshOutDto:

        try:

            user_token = UserToken(
                token=user_token_dto.refresh_token
            )

            # トークンが無効ならばエラー
            if not user_token.is_authenticated():
                raise UnauthenticateException

            # ユーザIDが得られなければエラー
            if not user_token.id:
                raise UnauthenticateException

            # ユーザの取得
            user_ds_dto = self.gateway.find_user_by_id(
                user_token.id
            )

            # ユーザがいなければエラー
            if not user_ds_dto:
                raise UnauthenticateException

            # リフレッシュトークンの存在チェック
            exist_token = self.gateway.exists_user_token_by_user_id_and_token(
                token=user_token_dto.refresh_token,
                user_id=user_token.id
            )

            if exist_token:
                raise UnauthenticateException

            # リフレッシュトークンを保存し、リフレッシュ済みとする
            user_token_ds_dto = UserTokenCreateInDsDto(
                token=user_token_dto.refresh_token,
                user_id=user_ds_dto.id,
                created_by=user_ds_dto.id,
                updated_by=user_ds_dto.id
            )
            self.gateway.create(user_token_ds_dto)

            # 過去のリフレッシュトークンを削除する
            self.gateway.delete_user_token(
                UserTokenDeleteInDsDto(
                    user_id=user_ds_dto.id,
                    date_before=datetime.now() - timedelta(days=10)
                )
            )

            # ユーザトークンの再作成
            user = User(
                ** user_ds_dto.model_dump()
            )
            user_token_out_dto = UserTokenRefreshOutDto(
                token=user.create_jwt(10),
                refresh_token=user.create_jwt(30),
            )

            self.presenter.prepare_success_view(
                user_token_out_dto)

            return user_token_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
