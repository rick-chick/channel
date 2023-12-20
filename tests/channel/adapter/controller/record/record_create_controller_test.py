from channel.adapter.controller.record.record_create_controller import RecordCreateController
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.gateway.device.device_session_impl import DeviceSessionImpl

from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.record.record_repository_impl import RecordRepositoryImpl
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.presenter.record.record_create_view_impl import RecordCreateViewImpl
from tests.channel.adapter.controller.record.record_create_input_parser_impl import RecordCreateInputParserImpl
from tests.channel.factories import DeviceSessionDsDtoFactory, RecordCreateOutDsDtoFactory


def test_success():

    device_session = DeviceSessionImpl()
    device_session.load_out = DeviceSessionDsDtoFactory.build()

    record_repository = RecordRepositoryImpl()
    record_repository.create_out = RecordCreateOutDsDtoFactory.build()

    controller = RecordCreateController(
        user_session=UserSessionImpl(),
        record_repository=record_repository,
        device_session=device_session,
        record_view=RecordCreateViewImpl(),
        input_parser=RecordCreateInputParserImpl(),
    )

    controller.handle(None)
