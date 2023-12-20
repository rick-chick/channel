from pydantic import ValidationError

from channel.entity.models import User
from channel.usecase.exception import (
    BusinessException,
    UnauthorizedException,
    UserNotFoundException,
    ValidationException,
)
from channel.usecase.input_port.user import UserUpdateInputPort
from channel.usecase.models import UserUpdateInDsDto
from channel.usecase.models import UserUpdateInDto, UserUpdateOutDto
from channel.usecase.output_port.user import UserUpdateOututPort
from channel.usecase.repository.user.user_update_repository import UserUpdateRepository


class UserUpdateInteractor(UserUpdateInputPort):

    def __init__(
            self,
            gateway: UserUpdateRepository,
            presenter: UserUpdateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def update(
            self, user_dto: UserUpdateInDto) -> UserUpdateOutDto:

        try:

            # ログインチェック
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            # ユーザの存在チェック
            if not self.gateway.exists_user_by_id(user_dto.id):
                raise UserNotFoundException

            user = User(**user_dto.model_dump())
            
            # パスワードが設定されている場合、ハッシュ化する
            if user.password:
                user.hash_password()

            # 更新する
            user_ds_dto = UserUpdateInDsDto(
                **user.model_dump(),
                updated_by=session_user_ds_dto.id,
            )
            user_res_ds_dto = self.gateway.update(user_ds_dto)

            user_out_dto = UserUpdateOutDto(**user_res_ds_dto.model_dump())

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
