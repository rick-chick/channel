from channel.usecase.models import (
    UserCreateOutDsDto,
    UserCreateInDsDto,
    UserUpdateInDsDto,
    UserDeleteOutDsDto,
    UserDeleteInDsDto,
    UserListInDsDto,
    UserListOutDsDto,
    UserOutDsDto,
    UserUpdateOutDsDto
)

from abc import ABC, abstractmethod
from typing import Optional, List


class UserRepository(ABC):

    @abstractmethod
    def exists_by_id(self, id: int) -> bool:
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[UserOutDsDto]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[UserOutDsDto]:
        pass

    @abstractmethod
    def list(self, ds_dto: UserListInDsDto) -> List[UserListOutDsDto]:
        pass

    @abstractmethod
    def create(self, ds_dto: UserCreateInDsDto) -> UserCreateOutDsDto:
        pass

    @abstractmethod
    def update(self, ds_dto: UserUpdateInDsDto) -> Optional[UserUpdateOutDsDto]:
        pass

    @abstractmethod
    def delete(self, ds_dto: UserDeleteInDsDto) -> List[UserDeleteOutDsDto]:
        pass
