from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateInDto,
    ChannelCreateOutDsDto,
    ChannelCreateOutDto,
    ChannelListOutDsDto,
    DeviceAuthenticateInDto,
    DeviceAuthenticateOutDto,
    DeviceCreateInDsDto,
    DeviceCreateInDto,
    DeviceCreateOutDsDto,
    DeviceCreateOutDto,
    DeviceOutDsDto,
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateInDto,
    RecordCreateOutDsDto,
    RecordCreateOutDto,
    RecordListDataOutDto,
    RecordListInDsDto,
    RecordListInDto,
    RecordListOutDsDto,
    RecordListOutDto,
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


class ChanneListOutDsDtoFactory(ModelFactory[ChannelListOutDsDto]):
    __model__=ChannelListOutDsDto

#################################################
# Record
#################################################

class RecordCreateInDsDtoFactory(ModelFactory[RecordCreateInDsDto]):
    __model__=RecordCreateInDsDto
    __faker__=faker


class RecordCreateOutDsDtoFactory(ModelFactory[RecordCreateOutDsDto]):
    __model__=RecordCreateOutDsDto


class RecordCreateInDtoFactory(ModelFactory[RecordCreateInDto]):
    __faker__=faker
    __model__=RecordCreateInDto


class RecordCreateOutDtoFactory(ModelFactory[RecordCreateOutDto]):
    __model__=RecordCreateOutDto


class RecordListInDsDtoFactory(ModelFactory[RecordListInDsDto]):
    __model__=RecordListInDsDto
    __faker__=faker


class RecordListOutDsDtoFactory(ModelFactory[RecordListOutDsDto]):
    __model__=RecordListOutDsDto
    __faker__=faker


class RecordListInDtoFactory(ModelFactory[RecordListInDto]):
    __model__=RecordListInDto
    __faker__=faker


class RecordListIDataOutDtoFactory(ModelFactory[RecordListDataOutDto]):
    __model__=RecordListDataOutDto


class RecordListOutDtoFactory(ModelFactory[RecordListOutDto]):
    __model__=RecordListOutDto
