from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.channel.cli_channel_update_input_parser import CliChannelUpdateInputParser
from channel.driver.view.cli.channel.cli_channel_update_view import CliChannelUpdateView
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import (
    SqlalchemyChannelRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.channel.channel_update_controller import (
    ChannelUpdateController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = ChannelUpdateController(
    channel_update_input_parser=CliChannelUpdateInputParser(memory),
    user_session=MemoryUserRepository(memory),
    channel_repository=SqlalchemyChannelRepository(session),
    channel_update_view=CliChannelUpdateView(),
)
buss.add(controller)

buss.handle(parse())
