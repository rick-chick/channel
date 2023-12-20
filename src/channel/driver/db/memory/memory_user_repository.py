from channel.usecase.models import (
    UserSessionDsDto
)
from channel.adapter.gateway.user.user_session import (
    UserSession
)

from typing import Dict, Any, Optional


class MemoryUserRepository(UserSession):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def load(self) -> Optional[UserSessionDsDto]:
        if not 'user' in self.memory:
            return None
        return self.memory['user']

    def save(self, user_session_ds_dto: UserSessionDsDto):
        if self.memory:
            self.memory['user'] = user_session_ds_dto
