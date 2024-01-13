from datetime import datetime, timedelta
from typing import Optional
from channel.entity.models import User
from channel.usecase.input_port.user import UserResetPasswordInputPort
from channel.usecase.repository.user import UserResetPasswordRepository
from channel.usecase.output_port.user import UserResetPasswordOututPort

from channel.usecase.models import (
    SignupGetOutDsDto,
    UserCreateInDsDto,
    UserCreateInDto,
    UserOutDsDto,
    UserResetPasswordInDto,
    UserResetPasswordOutDto,
    UserUpdateInDsDto,
    UserUpdateInDto,
)
from channel.usecase.exception import (
    BusinessException,
    InvalidSignupTokenException,
    ValidationException)

from pydantic import ValidationError
from uuid import uuid4


class UserResetPasswordInteractor(UserResetPasswordInputPort):

    def __init__(
            self,
            gateway: UserResetPasswordRepository,
            presenter: UserResetPasswordOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def reset_password(
        self, user_dto: UserResetPasswordInDto
    ) -> UserResetPasswordOutDto:

        try:

            signup: Optional[SignupGetOutDsDto]
            signup = self.gateway.find_signup_by_token(
                user_dto.token
            )

            # サインアップトークンチェック
            # トークン発行から10分まで有効とする
            if not signup:
                raise InvalidSignupTokenException
            if datetime.now() - signup.created_at > timedelta(minutes=10):
                raise InvalidSignupTokenException

            # ユーザの存在チェック
            user_ds_dto: Optional[UserOutDsDto]
            user_ds_dto = self.gateway.find_user_by_email(
                signup.email
            )

            # 戻り値
            user_out_dto = UserResetPasswordOutDto(
                success=False
            )

            # ユーザ存在しない場合登録
            if not user_ds_dto:

                # passwordのハッシュ化
                user = User(
                    id=str(uuid4()),
                    email=signup.email,
                    password=user_dto.password,
                )
                user.hash_password()

                self.gateway.create_user(
                    UserCreateInDsDto(
                        ** user.model_dump(),
                        created_by='system',
                        updated_by='system',
                    )
                )
                user_out_dto.success = True

            # ユーザ存在する場合パスワード更新
            else:

                # passwordのハッシュ化
                user = User(
                    id=user_ds_dto.id,
                    email=signup.email,
                    password=user_dto.password,
                )
                user.hash_password()

                self.gateway.update_user(
                    UserUpdateInDsDto(
                        ** user.model_dump(),
                        updated_by='system',
                    )
                )
                user_out_dto.success = True

            # 成功処理
            self.presenter.prepare_success_view(
                user_out_dto
            )

            return user_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
