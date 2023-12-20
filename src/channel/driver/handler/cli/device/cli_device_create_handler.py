from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.handler.cli.parser import parse
from channel.driver.view.cli.device.cli_device_create_view import CliDeviceCreateView
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import SqlalchemyDeviceRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.adapter.controller.device.device_create_controller import DeviceCreateController
from channel.driver.handler.cli.handler_buss import UserTokenAuthenticateHandlerBuss
from channel.driver.handler.cli.device.cli_device_create_input_parser import CliDeviceCreateInputParser


memory = {}
session = Session()


controller = DeviceCreateController(
    user_session=MemoryUserRepository(memory),
    device_repository=SqlalchemyDeviceRepository(session),
    device_view=CliDeviceCreateView(),
    input_parser=CliDeviceCreateInputParser(memory),
)


buss = UserTokenAuthenticateHandlerBuss(memory, session)
buss.add(controller)
buss.handle(parse())
