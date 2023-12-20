from channel.adapter.controller.device.device_create_controller import (
    DeviceCreateController,
)
from tests.channel.adapter.controller.device.device_create_input_parser_impl import (
    DeviceCreateInputParserImpl
)

from tests.channel.adapter.gateway.device.device_repository_impl import (
    DeviceRepositoryImpl
)
from tests.channel.adapter.presenter.device.device_create_view_impl import (
    DeviceCreateViewImpl
)
from tests.channel.adapter.gateway.user.user_session_impl import (
    UserSessionImpl
)

from tests.channel.factories import (
    DeviceCreateOutDsDtoFactory
)


def test_success():

    deivce_repository = DeviceRepositoryImpl()
    deivce_repository.create_out = DeviceCreateOutDsDtoFactory.build()

    controller = DeviceCreateController(
        input_parser=DeviceCreateInputParserImpl(),
        user_session=UserSessionImpl(),
        device_repository=deivce_repository,
        device_view=DeviceCreateViewImpl(),
    )

    controller.handle(None)
