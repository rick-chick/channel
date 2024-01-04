from channel.driver.db.sqlalchemy.conf import engine, Session
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user.cli_user_create_input_parser import CliUserCreateInputParser
from channel.driver.view.cli.user.cli_user_create_view import CliUserCreateView
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.user.user_create_controller import (
    UserCreateController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


memory = {}
session = Session()

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = UserCreateController(
    user_create_input_parser=CliUserCreateInputParser(memory),
    user_session=MemoryUserRepository(memory),
    user_repository=SqlalchemyUserRepository(session),
    user_create_view=CliUserCreateView(),
)
buss.add(controller)

try:
    buss.handle(parse())
    session.commit()
except Exception:
    session.rollback()
