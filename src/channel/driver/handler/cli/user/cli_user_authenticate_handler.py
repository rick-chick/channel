from channel.adapter.controller.user.user_authenticate_controller import (
    UserAuthenticateController,
)
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.driver.db.sqlalchemy.conf import engine, Session
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user.cli_user_authenticate_input_parser import (
    CliUserAuthenticateInputParser,
)
from channel.driver.view.cli.user.cli_user_authenticate_view import (
    CliUserAuthenticateView,
)

memory = {}
session = Session()

controller = UserAuthenticateController(
    user_authenticate_input_parser=CliUserAuthenticateInputParser(memory),
    user_session=MemoryUserRepository(memory),
    user_repository=SqlalchemyUserRepository(session),
    user_authenticate_view=CliUserAuthenticateView(),
)

controller.handle(parse())
