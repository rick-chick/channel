from channel.usecase.models import UserSessionDsDto
from channel.adapter.gateway.user.user_session import UserSession

from tests.channel.factories import UserSessionDsDtoFactory

from typing import Optional


class UserSessionImpl(UserSession):

    load_called: bool = False

    def load(self) -> Optional[UserSessionDsDto]:
        self.load_called = True
        return UserSessionDsDtoFactory.build()

    def save(self, user_session_ds_dto: UserSessionDsDto):
        self.save_in = user_session_ds_dto
