from channel.driver.client.cli.cli_mail_client import CliMailClient
from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_signup_repository import SqlalchemySignupRepository
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import SqlalchemyUserRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.user.cli_user_signup_input_parser import CliUserSignupInputParser
from channel.driver.view.cli.user.cli_user_signup_view import CliUserSignupView
from channel.adapter.controller.user.user_signup_controller import (
    UserSignupController
)
from channel.driver.handler.cli.handler_buss import (
    HandlerBuss,
)
from channel.driver.env import PASSWORD_RESET_URL

session = Session()
memory = {}

buss = HandlerBuss(memory, session)

controller = UserSignupController(
    user_signup_input_parser=CliUserSignupInputParser(memory),
    user_repository=SqlalchemyUserRepository(session),
    signup_repository=SqlalchemySignupRepository(session),
    mail_service=CliMailClient(),
    user_signup_view=CliUserSignupView(),
    password_reset_url=PASSWORD_RESET_URL,
)
buss.add(controller)

buss.handle(parse())
