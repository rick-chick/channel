from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateInDto,
    ChannelCreateOutDsDto,
    ChannelCreateOutDto,
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    ChannelListInDsDto,
    ChannelListInDto,
    ChannelListOutDsDto,
    ChannelListOutDto,
    DeviceAuthenticateInDto,
    DeviceAuthenticateOutDto,
    DeviceCreateInDsDto,
    DeviceCreateInDto,
    DeviceCreateOutDsDto,
    DeviceCreateOutDto,
    DeviceDeleteInDto,
    DeviceDeleteOutDsDto,
    DeviceDeleteOutDto,
    DeviceListInDsDto,
    DeviceListInDto,
    DeviceListOutDsDto,
    DeviceListOutDto,
    DeviceOutDsDto,
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateInDto,
    RecordCreateOutDsDto,
    RecordCreateOutDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    RecordListDataOutDto,
    RecordListInDsDto,
    RecordListInDto,
    RecordListOutDsDto,
    RecordListOutDto,
    RecordOutDsDto,
    UserAuthenticateInDto,
    UserAuthenticateOutDsDto,
    UserAuthenticateOutDto,
    UserCreateInDsDto,
    UserCreateInDto,
    UserCreateOutDsDto,
    UserCreateOutDto,
    UserOutDsDto,
    UserSessionDsDto,
    UserTokenAuthenticateInDto,
    UserTokenAuthenticateOutDto,
    UserTokenCreateInDsDto,
    UserTokenCreateOutDsDto,
    UserTokenRefreshInDto,
    UserTokenRefreshOutDto,
    UserUpdateInDsDto,
    UserUpdateInDto,
    UserUpdateOutDsDto,
    UserUpdateOutDto,
)

faker = Faker(locale="ja_JP")

################################################
# User
################################################


class UserCreateInDsDtoFactory(ModelFactory[UserCreateInDsDto]):
    __model__ = UserCreateInDsDto

    @classmethod
    def id(cls) -> str:
        return cls.__faker__.isbn10()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()


class UserCreateOutDsDtoFactory(ModelFactory[UserCreateOutDsDto]):
    __model__ = UserCreateOutDsDto

    @classmethod
    def id(cls) -> str:
        return cls.__faker__.isbn10()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()


class UserCreateInDtoFactory(ModelFactory[UserCreateInDto]):
    __faker__ = faker
    __model__ = UserCreateInDto

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.name()

    @classmethod
    def password(cls) -> str:
        return cls.__faker__.password()


class UserCreateOutDtoFactory(ModelFactory[UserCreateOutDto]):
    __model__ = UserCreateOutDto


class UserUpdateInDsDtoFactory(ModelFactory[UserUpdateInDsDto]):
    __model__ = UserUpdateInDsDto

    @classmethod
    def id(cls) -> str:
        return cls.__faker__.isbn10()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()


class UserUpdateOutDsDtoFactory(ModelFactory[UserUpdateOutDsDto]):
    __model__ = UserUpdateOutDsDto

    @classmethod
    def id(cls) -> str:
        return cls.__faker__.isbn10()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()


class UserUpdateInDtoFactory(ModelFactory[UserUpdateInDto]):
    __faker__ = faker
    __model__ = UserUpdateInDto

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.name()

    @classmethod
    def password(cls) -> str:
        return cls.__faker__.password()


class UserUpdateOutDtoFactory(ModelFactory[UserUpdateOutDto]):
    __model__ = UserUpdateOutDto


class UserSessionDsDtoFactory(ModelFactory[UserSessionDsDto]):
    __model__ = UserSessionDsDto


class UserAuthenticateInDtoFactory(ModelFactory[UserAuthenticateInDto]):
    __model__ = UserAuthenticateInDto


class UserAuthenticateOutDtoFactory(ModelFactory[UserAuthenticateOutDto]):
    __model__ = UserAuthenticateOutDto


class UserAuthenticateOutDsDtoFactory(ModelFactory[UserAuthenticateOutDsDto]):
    __model__ = UserAuthenticateOutDsDto


class UserOutDsDtoFactory(ModelFactory[UserOutDsDto]):
    __model__ = UserOutDsDto

################################################
# UserToken
################################################


class UserTokenAuthenticateInDtoFactory(ModelFactory[UserTokenAuthenticateInDto]):
    __model__ = UserTokenAuthenticateInDto


class UserTokenAuthenticateOutDtoFactory(ModelFactory[UserTokenAuthenticateOutDto]):
    __model__ = UserTokenAuthenticateOutDto


class UserTokenRefreshInDtoFactory(ModelFactory[UserTokenRefreshInDto]):
    __model__ = UserTokenRefreshInDto


class UserTokenRefreshOutDtoFactory(ModelFactory[UserTokenRefreshOutDto]):
    __model__ = UserTokenRefreshOutDto


class UserTokenCreateInDsDtoFactory(ModelFactory[UserTokenCreateInDsDto]):
    __model__ = UserTokenCreateInDsDto


class UserTokenCreateOutDsDtoFactory(ModelFactory[UserTokenCreateOutDsDto]):
    __model__ = UserTokenCreateOutDsDto


#################################################
# Device
#################################################


class DeviceCreateInDsDtoFactory(ModelFactory[DeviceCreateInDsDto]):
    __model__ = DeviceCreateInDsDto


class DeviceCreateOutDsDtoFactory(ModelFactory[DeviceCreateOutDsDto]):
    __model__ = DeviceCreateOutDsDto


class DeviceCreateInDtoFactory(ModelFactory[DeviceCreateInDto]):
    __faker__ = faker
    __model__ = DeviceCreateInDto


class DeviceCreateOutDtoFactory(ModelFactory[DeviceCreateOutDto]):
    __model__ = DeviceCreateOutDto


class DeviceAuthenticateInDtoFactory(ModelFactory[DeviceAuthenticateInDto]):
    __model__ = DeviceAuthenticateInDto


class DeviceAuthenticateOutDtoFactory(ModelFactory[DeviceAuthenticateOutDto]):
    __model__ = DeviceAuthenticateOutDto


class DeviceOutDsDtoFactory(ModelFactory[DeviceOutDsDto]):
    __model__ = DeviceOutDsDto


class DeviceSessionDsDtoFactory(ModelFactory[DeviceSessionDsDto]):
    __model__ = DeviceSessionDsDto


class DeviceListOutDtoFactory(ModelFactory[DeviceListOutDto]):
    __model__ = DeviceListOutDto


class DeviceListInDsDtoFactory(ModelFactory[DeviceListInDsDto]):
    __model__ = DeviceListInDsDto


class DeviceListOutDsDtoFactory(ModelFactory[DeviceListOutDsDto]):
    __model__ = DeviceListOutDsDto


class DeviceListInDtoFactory(ModelFactory[DeviceListInDto]):
    __model__ = DeviceListInDto


class DeviceDeleteOutDtoFactory(ModelFactory[DeviceDeleteOutDto]):
    __model__ = DeviceDeleteOutDto


class DeviceDeleteInDtoFactory(ModelFactory[DeviceDeleteInDto]):
    __model__ = DeviceDeleteInDto


class DeviceDeleteOutDsDtoFactory(ModelFactory[DeviceDeleteOutDsDto]):
    __model__ = DeviceDeleteOutDsDto


#################################################
# Channel
#################################################

class ChannelCreateInDsDtoFactory(ModelFactory[ChannelCreateInDsDto]):
    __model__ = ChannelCreateInDsDto
    __faker__ = faker


class ChannelCreateOutDsDtoFactory(ModelFactory[ChannelCreateOutDsDto]):
    __model__ = ChannelCreateOutDsDto


class ChannelCreateInDtoFactory(ModelFactory[ChannelCreateInDto]):
    __faker__ = faker
    __model__ = ChannelCreateInDto


class ChannelCreateOutDtoFactory(ModelFactory[ChannelCreateOutDto]):
    __model__ = ChannelCreateOutDto


class ChannelListOutDsDtoFactory(ModelFactory[ChannelListOutDsDto]):
    __model__ = ChannelListOutDsDto


class ChannelListInDsDtoFactory(ModelFactory[ChannelListInDsDto]):
    __model__ = ChannelListInDsDto


class ChannelListInDtoFactory(ModelFactory[ChannelListInDto]):
    __model__ = ChannelListInDto


class ChannelListOutDtoFactory(ModelFactory[ChannelListOutDto]):
    __model__ = ChannelListOutDto


class ChannelDeleteOutDsDtoFactory(ModelFactory[ChannelDeleteOutDsDto]):
    __model__ = ChannelDeleteOutDsDto


class ChannelDeleteInDsDtoFactory(ModelFactory[ChannelDeleteInDsDto]):
    __model__ = ChannelDeleteInDsDto

#################################################
# Record
#################################################


class RecordCreateInDsDtoFactory(ModelFactory[RecordCreateInDsDto]):
    __model__ = RecordCreateInDsDto
    __faker__ = faker


class RecordCreateOutDsDtoFactory(ModelFactory[RecordCreateOutDsDto]):
    __model__ = RecordCreateOutDsDto


class RecordCreateInDtoFactory(ModelFactory[RecordCreateInDto]):
    __faker__ = faker
    __model__ = RecordCreateInDto


class RecordCreateOutDtoFactory(ModelFactory[RecordCreateOutDto]):
    __model__ = RecordCreateOutDto


class RecordListInDsDtoFactory(ModelFactory[RecordListInDsDto]):
    __model__ = RecordListInDsDto
    __faker__ = faker


class RecordListOutDsDtoFactory(ModelFactory[RecordListOutDsDto]):
    __model__ = RecordListOutDsDto
    __faker__ = faker


class RecordListInDtoFactory(ModelFactory[RecordListInDto]):
    __model__ = RecordListInDto
    __faker__ = faker


class RecordListIDataOutDtoFactory(ModelFactory[RecordListDataOutDto]):
    __model__ = RecordListDataOutDto


class RecordListOutDtoFactory(ModelFactory[RecordListOutDto]):
    __model__ = RecordListOutDto


class RecordDeleteOutDsDtoFactory(ModelFactory[RecordDeleteOutDsDto]):
    __model__ = RecordDeleteOutDsDto


class RecordDeleteInDsDtoFactory(ModelFactory[RecordDeleteInDsDto]):
    __model__ = RecordDeleteInDsDto


class RecordOutDsDtoFactory(ModelFactory[RecordOutDsDto]):
    __model__ = RecordOutDsDto
