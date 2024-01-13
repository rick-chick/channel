from datetime import datetime, timezone
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, field_validator, validator


out_ds_config = ConfigDict(from_attributes=True)

###################################################
# User
###################################################


class UserCreateInDto(BaseModel):
    email: str
    password: str


class UserCreateOutDto(BaseModel):
    id: str
    email: str


class UserCreateInDsDto(BaseModel):
    id: str
    email: str
    password_hash: str
    created_by: str
    updated_by: str


class UserCreateOutDsDto(BaseModel):
    id: str
    email: str
    created_by: str
    updated_by: str

    model_config = out_ds_config


class UserUpdateInDto(BaseModel):
    id: str
    email: str
    password: Optional[str]


class UserUpdateOutDto(BaseModel):
    id: str
    email: str


class UserUpdateInDsDto(BaseModel):
    id: str
    email: str
    password_hash: Optional[str]
    updated_by: str


class UserUpdateOutDsDto(BaseModel):
    id: str
    email: str
    created_by: str
    updated_by: str

    model_config = out_ds_config


class UserListInDsDto(BaseModel):
    pass


class UserListOutDsDto(BaseModel):
    model_config = out_ds_config


class UserDeleteInDsDto(BaseModel):
    pass


class UserDeleteOutDsDto(BaseModel):
    model_config = out_ds_config


class UserOutDsDto(BaseModel):
    id: str
    email: str
    password_hash: str

    model_config = out_ds_config


class UserSessionDsDto(BaseModel):
    id: str
    email: str


class UserAuthenticateInDto(BaseModel):
    email: str
    password: str


class UserAuthenticateOutDto(BaseModel):
    token: str
    refresh_token: str


class UserAuthenticateInDsDto(BaseModel):
    email: str


class UserAuthenticateOutDsDto(BaseModel):
    id: str
    email: str
    password: str
    password_hash: str


class UserSignupInDto(BaseModel):
    email: str


class UserSignupOutDto(BaseModel):
    email: str


class UserResetPasswordInDto(BaseModel):
    token: str
    password: str


class UserResetPasswordOutDto(BaseModel):
    success: bool


class UserResetPasswordInDsDto(BaseModel):
    email: str


class UserResetPasswordOutDsDto(BaseModel):
    email: str


###################################################
# UserToken
###################################################

class UserTokenAuthenticateInDto(BaseModel):
    token: str


class UserTokenAuthenticateOutDto(BaseModel):
    id: str


class UserTokenRefreshInDto(BaseModel):
    refresh_token: str


class UserTokenRefreshOutDto(BaseModel):
    token: str
    refresh_token: str


class UserTokenCreateInDsDto(BaseModel):
    user_id: str
    token: str
    created_by: str
    updated_by: str


class UserTokenCreateOutDsDto(BaseModel):
    user_id: str
    token: str
    model_config = out_ds_config


class UserTokenDeleteInDsDto(BaseModel):
    user_id: str
    date_before: datetime


class UserTokenDeleteOutDsDto(BaseModel):
    pass


###################################################
# Device
###################################################


class DeviceCreateInDto(BaseModel):
    tags: List[str] = []


class DeviceCreateOutDto(BaseModel):
    id: int
    api_key: str
    tags: List[str] = []


class DeviceCreateInDsDto(BaseModel):
    user_id: str
    api_key: str
    tags: List[str] = []
    created_by: str
    updated_by: str


class DeviceCreateOutDsDto(BaseModel):
    user_id: str
    id: int
    api_key: str
    tags: List[str] = []
    created_by: str
    updated_by: str
    model_config = out_ds_config


class DeviceUpdateInDsDto(BaseModel):
    user_id: str
    id: int
    api_key: str
    tags: List[str] = []
    created_by: str
    updated_by: str


class DeviceUpdateOutDsDto(BaseModel):
    user_id: str
    id: int
    api_key: str
    tags: List[str] = []
    created_by: str
    updated_by: str
    model_config = out_ds_config


class DeviceListInDto(BaseModel):
    pass


class DeviceListChannelDataOutDto(BaseModel):
    name: str
    id: int
    unit: str
    record: Optional[float] = None


class DeviceListDataOutDto(BaseModel):
    id: int
    channels: List[DeviceListChannelDataOutDto]
    api_key: str
    latest_time: Optional[datetime]


class DeviceListOutDto(BaseModel):
    values: List[DeviceListDataOutDto] = []


class DeviceListInDsDto(BaseModel):
    user_id: str
    device_id: Optional[int] = None


class DeviceListOutDsDto(BaseModel):
    model_config = out_ds_config
    id: int
    api_key: str


class DeviceDeleteInDto(BaseModel):
    ids: List[int] = []


class DeviceDeleteOutDto(BaseModel):
    ids: List[int] = []
    undeleted_ids: List[int] = []
    model_config = out_ds_config


class DeviceDeleteInDsDto(BaseModel):
    user_id: str
    ids: List[int] = []


class DeviceDeleteOutDsDto(BaseModel):
    id: int
    model_config = out_ds_config


class DeviceOutDsDto(BaseModel):
    model_config = out_ds_config
    user_id: str
    id: int
    api_key: str
    tags: List[str] = []


class DeviceAuthenticateInDto(BaseModel):
    api_key: str


class DeviceAuthenticateOutDto(BaseModel):
    id: int


class DeviceSessionDsDto(BaseModel):
    id: int


###################################################
# Channel
###################################################


class ChannelCreateInDto(BaseModel):
    device_id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelCreateOutDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelCreateInDsDto(BaseModel):
    device_id: int
    name: str
    unit: str
    tags: List[str] = []
    created_by: str
    updated_by: str


class ChannelCreateOutDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []
    created_by: str
    updated_by: str
    model_config = out_ds_config


class ChannelUpdateInDto(BaseModel):
    id: int
    name: Optional[str] = None
    unit: Optional[str] = None
    tags: Optional[List[str]] = None


class ChannelUpdateOutDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelUpdateInDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []
    updated_by: str


class ChannelUpdateOutDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []
    updated_by: str

    model_config = out_ds_config


class ChannelListInDto(BaseModel):
    device_id: Optional[int] = None


class ChannelListDataOutDto(BaseModel):
    id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelListOutDto(BaseModel):
    model_config = out_ds_config

    values: List[ChannelListDataOutDto]


class ChannelListInDsDto(BaseModel):
    user_id: Optional[str] = None
    device_id: Optional[int] = None
    device_ids: Optional[List[int]] = None


class ChannelListOutDsDto(BaseModel):
    model_config = out_ds_config

    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelDeleteInDto(BaseModel):
    ids: List[int] = []


class ChannelDeleteOutDto(BaseModel):
    ids: List[int] = []
    model_config = out_ds_config


class ChannelDeleteInDsDto(BaseModel):
    ids: Optional[List[int]] = None
    device_ids: Optional[List[int]] = None


class ChannelDeleteOutDsDto(BaseModel):
    id: int
    model_config = out_ds_config


class ChannelGetOutDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []

    model_config = out_ds_config

###################################################
# Record
###################################################


class RecordCreateInDto(BaseModel):
    api_key: str
    time: datetime
    values: Dict[int, float]


class RecordCreateOutDto(BaseModel):
    time: datetime
    values: Dict[int, float]


class RecordCreateInDsDto(BaseModel):
    channel_id: int
    time: datetime
    value: float


class RecordCreateOutDsDto(BaseModel):
    channel_id: int
    time: datetime
    value: float
    model_config = out_ds_config


class RecordOutDsDto(BaseModel):
    channel_id: int
    time: datetime
    value: float
    model_config = out_ds_config


class RecordListInDto(BaseModel):
    device_id: int
    date_from: datetime
    date_to: datetime
    span: int

    @field_validator('date_from', 'date_to', mode='after')
    def validate_timezone(cls, v: datetime):
        if v.tzinfo:
            return v.astimezone(timezone.utc).replace(tzinfo=None)
        else:
            return v.replace(tzinfo=None)


class RecordListDataOutDto(BaseModel):
    # 複数のラインチャートを書く場合、それぞれのラインチャートにつけるラベル
    label: str
    # Y軸
    data: List[Optional[float]]


class RecordListOutDto(BaseModel):
    # X軸
    labels: List[datetime]
    datasets: List[RecordListDataOutDto]


class RecordListInDsDto(BaseModel):
    channel_ids: Optional[List[int]] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None


class RecordListOutDsDto(BaseModel):
    model_config = out_ds_config

    channel_id: int
    time: datetime
    value: Optional[float] = None


class RecordDeleteInDsDto(BaseModel):
    channel_ids: Optional[List[int]] = None


class RecordDeleteOutDsDto(BaseModel):
    channel_id: int
    model_config = out_ds_config


###################################################
# Mail
###################################################

class MailSendInDsDto(BaseModel):
    title: str
    body: str
    user_to: str


class MailSendOutDsDto(BaseModel):
    success: bool


###################################################
# Signup
###################################################
class SignupCreateInDsDto(BaseModel):
    email: str
    token: str


class SignupCreateOutDsDto(BaseModel):
    email: str
    token: str
    model_config = out_ds_config


class SignupDeleteInDsDto(BaseModel):
    email: Optional[str]


class SignupDeleteOutDsDto(BaseModel):
    emails: List[str] = []
    model_config = out_ds_config


class SignupGetInDsDto(BaseModel):
    token: str


class SignupGetOutDsDto(BaseModel):
    email: str
    token: str
    created_at: datetime
    model_config = out_ds_config
