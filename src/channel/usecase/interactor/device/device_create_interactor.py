from channel.usecase.input_port.device import DeviceCreateInputPort
from channel.usecase.repository.device import DeviceCreateRepository
from channel.usecase.models import DeviceCreateInDsDto
from channel.usecase.output_port.device import DeviceCreateOututPort

from channel.usecase.models import (
    DeviceCreateInDto, DeviceCreateOutDto)
from channel.usecase.exception import (
    BusinessException, ValidationException, UnauthorizedException)

from channel.entity.models import Device

from pydantic import ValidationError
from uuid import uuid4


class DeviceCreateInteractor(DeviceCreateInputPort):

    def __init__(
            self,
            gateway: DeviceCreateRepository,
            presenter: DeviceCreateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def create(
            self, device_dto: DeviceCreateInDto) -> DeviceCreateOutDto:

        try:

            session_user_ds_dto = self.gateway.load_session_user()

            if not session_user_ds_dto:
                raise UnauthorizedException

            device = Device(
                user_id=session_user_ds_dto.id,
                **device_dto.model_dump(),
                api_key=str(uuid4()),
            )

            device_ds_dto = DeviceCreateInDsDto(
                **device.model_dump(),
                created_by=session_user_ds_dto.id,
                updated_by=session_user_ds_dto.id,
            )

            device_res_ds_dto = self.gateway.create(device_ds_dto)

            device_out_dto = DeviceCreateOutDto(
                **device_res_ds_dto.model_dump())

            self.presenter.prepare_success_view(
                device_out_dto)

            return device_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
