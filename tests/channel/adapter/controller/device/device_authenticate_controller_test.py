from channel.adapter.controller.device.device_authenticate_controller import (
    DeviceAuthenticateController,
)
from tests.channel.adapter.controller.device.device_authenticate_input_parser_impl import (
    DeviceAuthenticateInputParserImpl,
)
from tests.channel.adapter.gateway.device.device_repository_impl import (
    DeviceRepositoryImpl,
)
from tests.channel.adapter.gateway.device.device_session_impl import DeviceSessionImpl
from tests.channel.adapter.presenter.device.device_authenticate_view_impl import (
    DeviceAuthenticateViewImpl,
)
from tests.channel.factories import DeviceAuthenticateInDtoFactory


def test_success():
    device_repository = DeviceRepositoryImpl()
    device_repository.find_id_by_api_key_out = 0
    target = DeviceAuthenticateController(
        device_session=DeviceSessionImpl(),
        device_repository=device_repository,
        device_authenticate_view=DeviceAuthenticateViewImpl(),
        device_authenticate_input_parser=DeviceAuthenticateInputParserImpl()
    )
    target.handle(DeviceAuthenticateInDtoFactory.build())
