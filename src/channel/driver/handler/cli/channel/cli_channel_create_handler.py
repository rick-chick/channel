from channel.driver.db.sqlalchemy.conf import engine, Session
from channel.driver.handler.cli.channel.cli_channel_create_input_parser import CliChannelCreateInputParser
from channel.driver.handler.cli.handler_buss import UserTokenAuthenticateHandlerBuss
from channel.driver.handler.cli.parser import parse
from channel.driver.view.cli.channel.cli_channel_create_view import CliChannelCreateView
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.adapter.controller.channel.channel_create_controller import ChannelCreateController


memory = {}
session = Session()

controller = ChannelCreateController(
    user_session=MemoryUserRepository(memory),
    channel_repository=SqlalchemyChannelRepository(session),
    channel_view=CliChannelCreateView(),
    parser=CliChannelCreateInputParser(memory),
)


buss = UserTokenAuthenticateHandlerBuss(memory, session)
buss.add(controller)
buss.handle(parse())
