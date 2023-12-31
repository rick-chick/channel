from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import SqlalchemyRecordRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.device.cli_device_list_input_parser import CliDeviceListInputParser
from channel.driver.view.cli.device.cli_device_list_view import CliDeviceListView
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import (
    SqlalchemyDeviceRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.device.device_list_controller import (
    DeviceListController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = DeviceListController(
    device_list_input_parser=CliDeviceListInputParser(memory),
    channel_repository=SqlalchemyChannelRepository(session),
    record_repository=SqlalchemyRecordRepository(session),
    user_session=MemoryUserRepository(memory),
    device_repository=SqlalchemyDeviceRepository(session),
    device_list_view=CliDeviceListView(),
)
buss.add(controller)

try:
    buss.handle(parse())
    session.commit()
except Exception:
    session.rollback()
