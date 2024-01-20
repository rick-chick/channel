from datetime import datetime
from channel.usecase.input_port.user import UserSignupInputPort
from channel.usecase.repository.user import UserSignupRepository
from channel.usecase.output_port.user import UserSignupOututPort

from channel.usecase.models import (
    MailSendInDsDto,
    SignupCreateInDsDto,
    SignupDeleteInDsDto,
    UserSignupInDto,
    UserSignupOutDto,
)
from channel.usecase.exception import (
    BusinessException,
    UserExistsException,
    ValidationException
)

from pydantic import ValidationError
import hashlib


class UserSignupInteractor(UserSignupInputPort):

    def __init__(
            self,
            gateway: UserSignupRepository,
            presenter: UserSignupOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def signup(
        self,
        user_dto: UserSignupInDto
    ) -> UserSignupOutDto:

        try:

            # 存在チェック
            if self.gateway.exists_user_by_email(user_dto.email):
                raise UserExistsException

            # Token生成
            current_time = str(datetime.now())
            token = hashlib.sha256(
                hashlib.sha256(
                    current_time.encode()
                ).digest()
            ).hexdigest()
            url = self.gateway.password_reset_url(token)

            # Send Mail
            send_mail_ds_dto = self.gateway.send_mail(
                MailSendInDsDto(
                    title='ChannelService サインアップの確認メール',
                    body=(
                        "ChannelServiceへのサインアップを受け付けいたしました。\n"
                        "アカウントを有効にするためには、以下のリンクをクリックして確認手続きを完了してください。\n"
                        "もしこのメールが誤って届いた場合、無視していただいて構いません。\n"
                        f"アカウントの確認リンク: {url}]\n"
                        "アカウントが正常に確認されると、ChannelService の利用が可能になります。\n"
                        "ご登録いただきありがとうございます！\n"
                        "ChannelService サポート チーム"
                    ),
                    user_to=user_dto.email,
                )
            )
            if send_mail_ds_dto.success:
                # Delete Signup
                self.gateway.delete_signup(
                    SignupDeleteInDsDto(
                        **user_dto.model_dump(),
                    )
                )
                # Create Signup
                self.gateway.create_signup(
                    SignupCreateInDsDto(
                        **user_dto.model_dump(),
                        token=token,
                    )
                )

            user_out_dto = UserSignupOutDto(
                **user_dto.model_dump(),
                success=True
            )

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
