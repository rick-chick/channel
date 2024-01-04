from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import SqlalchemyRecordRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.device.cli_device_delete_input_parser import CliDeviceDeleteInputParser
from channel.driver.view.cli.device.cli_device_delete_view import CliDeviceDeleteView
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import (
    SqlalchemyDeviceRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.device.device_delete_controller import (
    DeviceDeleteController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = DeviceDeleteController(
    device_delete_input_parser=CliDeviceDeleteInputParser(memory),
    user_session=MemoryUserRepository(memory),
    device_repository=SqlalchemyDeviceRepository(session),
    channel_repository=SqlalchemyChannelRepository(session),
    record_repository=SqlalchemyRecordRepository(session),
    device_delete_view=CliDeviceDeleteView(),
)
buss.add(controller)

buss.handle(parse())
