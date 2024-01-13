from channel.usecase.models import (
    ChannelUpdateInDsDto,
    SignupCreateInDsDto,
    UserTokenCreateInDsDto,
    UserCreateInDsDto,
    DeviceCreateInDsDto,
    ChannelCreateInDsDto,
    RecordCreateInDsDto,
    UserUpdateInDsDto,
)

from channel.driver.db.sqlalchemy.models import (
    SignupDataSource,
    UserTokenDataSource,
    UserDataSource,
    DeviceDataSource,
    ChannelDataSource,
    RecordDataSource,
)


class SqlalchemyUserTranslator():

    @classmethod
    def create(cls, user_ds_dto: UserCreateInDsDto) -> UserDataSource:
        return UserDataSource(
            ** user_ds_dto.model_dump()
        )

    @classmethod
    def update(cls, user_ds_dto: UserUpdateInDsDto, user_ds: UserDataSource) -> UserDataSource:
        if user_ds_dto.password_hash:
            user_ds.password_hash = user_ds_dto.password_hash
        user_ds.email = user_ds_dto.email
        user_ds.updated_by = user_ds_dto.updated_by
        return user_ds


class SqlalchemyDeviceTranslator():

    @classmethod
    def create(cls, device_ds_dto: DeviceCreateInDsDto) -> DeviceDataSource:
        return DeviceDataSource(
            ** device_ds_dto.model_dump(exclude={'tags'})
        )


class SqlalchemyChannelTranslator():

    @classmethod
    def create(cls, channel_ds_dto: ChannelCreateInDsDto) -> ChannelDataSource:
        return ChannelDataSource(
            ** channel_ds_dto.model_dump(exclude={'tags'})
        )

    @classmethod
    def update(
        cls,
        channel_ds_dto: ChannelUpdateInDsDto,
        channel_ds: ChannelDataSource
    ) -> ChannelDataSource:
        channel_ds.name = channel_ds_dto.name
        channel_ds.unit = channel_ds_dto.unit
        channel_ds.updated_by = channel_ds_dto.updated_by
        return channel_ds


class SqlalchemyRecordTranslator():

    @classmethod
    def create(cls, record_ds_dto: RecordCreateInDsDto) -> RecordDataSource:
        return RecordDataSource(
            ** record_ds_dto.model_dump()
        )


class SqlalchemyUserTokenTranslator():
    @classmethod
    def create(cls, record_ds_dto: UserTokenCreateInDsDto) -> UserTokenDataSource:
        return UserTokenDataSource(
            ** record_ds_dto.model_dump()
        )


class SqlalchemySignupTranslator():
    @classmethod
    def create(cls, record_ds_dto: SignupCreateInDsDto) -> SignupDataSource:
        return SignupDataSource(
            ** record_ds_dto.model_dump()
        )
