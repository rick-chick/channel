from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import SqlalchemyUserRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user_token.cli_user_token_refresh_input_parser import CliUserTokenRefreshInputParser
from channel.driver.view.cli.user_token.cli_user_token_refresh_view import CliUserTokenRefreshView
from channel.driver.db.sqlalchemy.sqlalchemy_user_token_repository import (
    SqlalchemyUserTokenRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.user_token.user_token_refresh_controller import (
    UserTokenRefreshController
)
from channel.driver.handler.cli.handler_buss import (
    HandlerBuss,
    UserTokenAuthenticateHandlerBuss
)

session = Session()
memory = {}

buss = HandlerBuss(memory, session)

controller = UserTokenRefreshController(
    user_token_refresh_input_parser=CliUserTokenRefreshInputParser(memory),
    user_repository=SqlalchemyUserRepository(session),
    user_token_repository=SqlalchemyUserTokenRepository(session),
    user_token_refresh_view=CliUserTokenRefreshView(),
)
buss.add(controller)

buss.handle(parse())
