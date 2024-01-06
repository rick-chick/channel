from channel.usecase.input_port.user import UserAuthenticateInputPort
from channel.usecase.repository.user import UserAuthenticateRepository
from channel.usecase.output_port.user import UserAuthenticateOututPort

from channel.usecase.models import (
    UserTokenCreateInDsDto,
    UserAuthenticateInDto,
    UserAuthenticateOutDto,
    UserSessionDsDto,
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthenticateException
)

from channel.entity.models import User

from pydantic import ValidationError


class UserAuthenticateInteractor(UserAuthenticateInputPort):

    def __init__(
            self,
            gateway: UserAuthenticateRepository,
            presenter: UserAuthenticateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def authenticate(
        self, user_in_dto: UserAuthenticateInDto
    ) -> UserAuthenticateOutDto:

        try:

            user_res_ds_dto = self.gateway.find_user_by_email(
                user_in_dto.email
            )

            if not user_res_ds_dto:
                raise UnauthenticateException

            user = User(
                **user_res_ds_dto.model_dump(),
                password=user_in_dto.password
            )

            if not user.is_authenticated():
                raise UnauthenticateException

            self.gateway.save_user_session(UserSessionDsDto(
                **user.model_dump()
            ))

            user_out_dto = UserAuthenticateOutDto(
                token=user.create_jwt(10),
                refresh_token=user.create_jwt(30),
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
