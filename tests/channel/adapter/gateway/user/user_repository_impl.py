from typing import List, Optional

from channel.adapter.gateway.user.user_repository import UserRepository
from channel.usecase.models import (
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserDeleteInDsDto,
    UserDeleteOutDsDto,
    UserListInDsDto,
    UserListOutDsDto,
    UserOutDsDto,
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
)
from tests.channel.factories import UserCreateOutDsDtoFactory, UserUpdateOutDsDtoFactory


class UserRepositoryImpl(UserRepository):

    create_in: Optional[UserCreateInDsDto] = None
    exists_by_email_in: Optional[str] = None
    exists_user_by_id_out: bool = True
    find_by_email_in: Optional[str] = None
    find_by_email_out: Optional[UserOutDsDto] = None
    find_user_by_id_out: Optional[UserOutDsDto]
    update_out: UserUpdateOutDsDto = UserUpdateOutDsDtoFactory.build()

    def exists_by_id(self, id: Optional[int]) -> bool:
        self.exists_user_by_id_in = id
        return self.exists_user_by_id_out

    def exists_by_email(self, email: str) -> bool:
        self.exists_by_email_in = email
        return False

    def find_by_id(self, id: str) -> Optional[UserOutDsDto]:
        self.find_user_by_id_in = id
        return self.find_user_by_id_out

    def find_by_email(self, email: str) -> Optional[UserOutDsDto]:
        self.find_by_email_in = email
        return self.find_by_email_out

    def list(self, ds_dto: UserListInDsDto) -> List[UserListOutDsDto]:
        self.list_in = ds_dto
        return []

    def create(self, ds_dto: UserCreateInDsDto) -> UserCreateOutDsDto:
        self.create_in = ds_dto
        return UserCreateOutDsDtoFactory.build()

    def update(self, ds_dto: UserUpdateInDsDto) -> UserUpdateOutDsDto:
        self.update_in = ds_dto
        return self.update_out

    def delete(self, ds_dto: UserDeleteInDsDto) -> List[UserDeleteOutDsDto]:
        self.delete_in = ds_dto
        return []
