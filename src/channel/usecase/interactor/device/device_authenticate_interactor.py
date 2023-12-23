from pydantic import ValidationError
from channel.usecase.exception import (
    BusinessException,
    UnauthenticateException,
    ValidationException,
)
from channel.usecase.input_port.device.device_authenticate_input_port import (
    DeviceAuthenticateInputPort,
)
from channel.usecase.models import (
    DeviceAuthenticateInDto,
    DeviceAuthenticateOutDto,
    DeviceSessionDsDto,
)
from channel.usecase.output_port.device.device_authenticate_output_port import (
    DeviceAuthenticateOututPort,
)
from channel.usecase.repository.device.device_authenticate_repository import (
    DeviceAuthenticateRepository,
)


class DeviceAuthenticateInteractor(DeviceAuthenticateInputPort):

    def __init__(
            self,
            gateway: DeviceAuthenticateRepository,
            presenter: DeviceAuthenticateOututPort):
        self.gateway = gateway
        self.presenter = presenter

    def authenticate(
            self, device_dto: DeviceAuthenticateInDto
    ) -> DeviceAuthenticateOutDto:

        try:

            device_id = self.gateway.find_device_id_by_api_key(
                device_dto.api_key
            )

            if device_id is None:
                raise UnauthenticateException

            # セッションにDeviceを保存
            device_session_ds_dto = DeviceSessionDsDto(
                id=device_id,
            )
            self.gateway.save_device_session(device_session_ds_dto)

            # 戻り値の作成
            device_out_dto = DeviceAuthenticateOutDto(
                id=device_id
            )

            self.presenter.prepare_success_view(
                device_out_dto
            )

            return device_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
