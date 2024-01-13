from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_signup_repository import SqlalchemySignupRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user.cli_user_reset_password_input_parser import CliUserResetPasswordInputParser
from channel.driver.view.cli.user.cli_user_reset_password_view import CliUserResetPasswordView
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.user.user_reset_password_controller import (
    UserResetPasswordController
)
from channel.driver.handler.cli.handler_buss import (
    HandlerBuss,
    UserTokenAuthenticateHandlerBuss
)

session = Session()
memory = {}

buss = HandlerBuss(memory, session)

controller = UserResetPasswordController(
    user_reset_password_input_parser=CliUserResetPasswordInputParser(memory),
    user_reset_password_view=CliUserResetPasswordView(),
    signup_repository=SqlalchemySignupRepository(session),
    user_repository=SqlalchemyUserRepository(session),
)
buss.add(controller)

buss.handle(parse())
