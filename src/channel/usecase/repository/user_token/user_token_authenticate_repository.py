from abc import ABC
from channel.usecase.models import (
    UserOutDsDto,
    UserSessionDsDto
)

from typing import Optional


class UserTokenAuthenticateRepository(ABC):

    def find_user_by_id(self, id: str) -> Optional[UserOutDsDto]:
        pass

    def save_user_session(self, user_ds_dto: UserSessionDsDto):
        pass
