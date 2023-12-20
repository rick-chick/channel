from channel.driver.db.sqlalchemy.conf import engine, Session
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user.cli_user_update_input_parser import CliUserUpdateInputParser
from channel.driver.view.cli.user.cli_user_update_view import CliUserUpdateView
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.user.user_update_controller import (
    UserUpdateController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


memory = {}
session = Session()

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = UserUpdateController(
    user_update_input_parser=CliUserUpdateInputParser(memory),
    user_session=MemoryUserRepository(memory),
    user_repository=SqlalchemyUserRepository(session),
    user_update_view=CliUserUpdateView(),
)
buss.add(controller)

buss.handle(parse())
