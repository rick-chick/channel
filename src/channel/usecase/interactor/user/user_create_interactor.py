from uuid import uuid4
from channel.usecase.input_port.user import UserCreateInputPort
from channel.usecase.repository.user import UserCreateRepository
from channel.usecase.output_port.user import UserCreateOututPort

from channel.usecase.models import (
    UserCreateInDto,
    UserCreateOutDto,
    UserCreateInDsDto,
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UserExistsException,
    UnauthorizedException
)

from channel.entity.models import User

from pydantic import ValidationError


class UserCreateInteractor(UserCreateInputPort):

    def __init__(
            self,
            gateway: UserCreateRepository,
            presenter: UserCreateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def create(
            self, user_dto: UserCreateInDto) -> UserCreateOutDto:

        try:

            user = User(
                id=str(uuid4()),
                **user_dto.model_dump(),
            )
            user.hash_password()

            session_user_ds_dto = self.gateway.load_session_user()

            # ログインユーザの確認
            if not session_user_ds_dto:
                raise UnauthorizedException

            # ユーザの重複チェック
            if (self.gateway.exists_user_by_email(user.email)):
                raise UserExistsException

            user_ds_dto = UserCreateInDsDto(
                **user.model_dump(),
                created_by=session_user_ds_dto.id,
                updated_by=session_user_ds_dto.id,
            )

            user_res_ds_dto = self.gateway.create(user_ds_dto)

            user_out_dto = UserCreateOutDto(
                **user_res_ds_dto.model_dump())

            self.presenter.prepare_success_view(
                user_out_dto)

            return user_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
