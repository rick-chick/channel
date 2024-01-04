from channel.usecase.input_port.device import DeviceDeleteInputPort
from channel.usecase.repository.device import DeviceDeleteRepository
from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    DeviceDeleteOutDsDto,
    DeviceDeleteInDsDto,
    DeviceDeleteOutDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.device import DeviceDeleteOututPort

from channel.usecase.models import DeviceDeleteInDto
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthorizedException
)

from pydantic import ValidationError
from typing import List


class DeviceDeleteInteractor(DeviceDeleteInputPort):

    def __init__(
            self,
            gateway: DeviceDeleteRepository,
            presenter: DeviceDeleteOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def delete(
            self, device_dto: DeviceDeleteInDto) -> DeviceDeleteOutDto:

        try:
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            # Device 削除
            device_ds_dtos: List[DeviceDeleteOutDsDto] = self.gateway.delete(
                DeviceDeleteInDsDto(
                    **device_dto.model_dump(),
                    user_id=session_user_ds_dto.id,
                )
            )

            # 削除されたDevice
            deleted_device_ids = [
                device.id for device in device_ds_dtos
                if device.id is not None]

            # 削除されなかったDevice
            undeleted_ids = [
                device_id for device_id in device_dto.ids
                if device_id not in deleted_device_ids]

            # Channel 削除
            channel_ds_dtos: List[ChannelDeleteOutDsDto] = self.gateway.delete_channel(
                ChannelDeleteInDsDto(
                    device_ids=deleted_device_ids,
                )
            )

            # 削除されたChannel
            deleted_channel_ids = [
                channel.id for channel in channel_ds_dtos
                if channel.id is not None]

            # Record 削除
            self.gateway.delete_record(
                RecordDeleteInDsDto(
                    channel_ids=deleted_channel_ids,
                )
            )

            result = DeviceDeleteOutDto(
                ids=deleted_device_ids,
                undeleted_ids=undeleted_ids
            )

            self.presenter.prepare_success_view(result)

            return result

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
