from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import SqlalchemyDeviceRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.channel.cli_channel_list_input_parser import CliChannelListInputParser
from channel.driver.view.cli.channel.cli_channel_list_view import CliChannelListView
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import (
    SqlalchemyChannelRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.channel.channel_list_controller import (
    ChannelListController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = ChannelListController(
    channel_list_input_parser=CliChannelListInputParser(memory),
    user_session=MemoryUserRepository(memory),
    device_repository=SqlalchemyDeviceRepository(session),
    channel_repository=SqlalchemyChannelRepository(session),
    channel_list_view=CliChannelListView(),
)
buss.add(controller)

buss.handle(parse())
