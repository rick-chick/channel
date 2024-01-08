from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.channel.cli_channel_delete_input_parser import CliChannelDeleteInputParser
from channel.driver.view.cli.channel.cli_channel_delete_view import CliChannelDeleteView
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import (
    SqlalchemyChannelRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.channel.channel_delete_controller import (
    ChannelDeleteController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = ChannelDeleteController(
    channel_delete_input_parser=CliChannelDeleteInputParser(memory),
    user_session=MemoryUserRepository(memory),
    channel_repository=SqlalchemyChannelRepository(session),
    channel_delete_view=CliChannelDeleteView(),
)
buss.add(controller)

buss.handle(parse())
