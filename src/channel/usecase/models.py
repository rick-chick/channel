from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


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


class UserAuthenticateInDsDto(BaseModel):
    email: str


class UserAuthenticateOutDsDto(BaseModel):
    id: str
    email: str
    password: str
    password_hash: str


###################################################
# UserToken
###################################################

class UserTokenAuthenticateInDto(BaseModel):
    token: str


class UserTokenAuthenticateOutDto(BaseModel):
    id: str


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


class DeviceListInDsDto(BaseModel):
    pass


class DeviceListOutDsDto(BaseModel):
    model_config = out_ds_config


class DeviceDeleteInDsDto(BaseModel):
    pass


class DeviceDeleteOutDsDto(BaseModel):
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


class ChannelUpdateInDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []
    created_by: str
    updated_by: str


class ChannelUpdateOutDsDto(BaseModel):
    device_id: int
    id: int
    name: str
    unit: str
    tags: List[str] = []
    created_by: str
    updated_by: str

    model_config = out_ds_config


class ChannelListInDsDto(BaseModel):
    device_id: int


class ChannelListOutDsDto(BaseModel):
    model_config = out_ds_config

    id: int
    name: str
    unit: str
    tags: List[str] = []


class ChannelDeleteInDsDto(BaseModel):
    pass


class ChannelDeleteOutDsDto(BaseModel):
    model_config = out_ds_config


class ChannelGetOutDsDto(BaseModel):
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


class RecordListInDto(BaseModel):
    device_id: int
    date_from: datetime
    date_to: datetime


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
    channel_ids: List[int]
    date_from: datetime
    date_to: datetime


class RecordListOutDsDto(BaseModel):
    model_config = out_ds_config

    channel_id: int
    time: datetime
    value: Optional[float] = None


class RecordDeleteInDsDto(BaseModel):
    pass


class RecordDeleteOutDsDto(BaseModel):
    model_config = out_ds_config
