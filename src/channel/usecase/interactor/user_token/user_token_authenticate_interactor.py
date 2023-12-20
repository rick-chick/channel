from channel.usecase.input_port.user_token import UserTokenAuthenticateInputPort
from channel.usecase.repository.user_token import UserTokenAuthenticateRepository
from channel.usecase.output_port.user_token import UserTokenAuthenticateOututPort

from channel.usecase.models import (
    UserTokenAuthenticateInDto,
    UserTokenAuthenticateOutDto,
    UserSessionDsDto
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthenticateException
)

from channel.entity.models import UserToken

from pydantic import ValidationError


class UserTokenAuthenticateInteractor(UserTokenAuthenticateInputPort):

    def __init__(
            self,
            gateway: UserTokenAuthenticateRepository,
            presenter: UserTokenAuthenticateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def authenticate(
            self, user_token_dto: UserTokenAuthenticateInDto) -> UserTokenAuthenticateOutDto:

        try:

            user_token = UserToken(**user_token_dto.model_dump())

            # decode token
            if not user_token.is_authenticated():
                raise UnauthenticateException

            # find user
            uer_out_ds_dto = self.gateway.find_user_by_id(user_token.id)

            if not uer_out_ds_dto:
                raise UnauthenticateException

            # save user session
            user_session_load_ds_dto = UserSessionDsDto(
                **uer_out_ds_dto.model_dump()
            )
            self.gateway.save_user_session(user_session_load_ds_dto)

            user_token_out_dto = UserTokenAuthenticateOutDto(
                **user_token.model_dump())

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
