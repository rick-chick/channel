from typing import Any, Dict, List

from sqlalchemy.orm import Session
from channel.adapter.controller.device.device_authenticate_controller import DeviceAuthenticateController

from channel.adapter.controller.handler import Handler
from channel.adapter.controller.user_token.user_token_authenticate_controller import (
    UserTokenAuthenticateController,
)
from channel.driver.db.memory.memory_device_repository import MemoryDeviceRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import SqlalchemyDeviceRepository
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from channel.driver.handler.cli.device.cli_device_authenticate_input_parser import CliDeviceAuthenticateInputParser
from channel.driver.handler.cli.user.cli_user_token_authenticate_input_parser import (
    CliUserTokenAuthenticateInputParser,
)
from channel.driver.view.cli.device.cli_device_authenticate_view import CliDeviceAuthenticateView
from channel.driver.view.cli.user_token import CliUserTokenAuthenticateView


class HandlerBuss():

    def __init__(
        self,
        memory: Dict[str, Any],
        session: Session
    ):
        self.handlers: List[Handler] = []
        self.memory = memory
        self.session = session

    def add(self, handler: Handler):
        self.handlers.append(handler)

    def handle(self, input_dto: Any):

        for handler in self.handlers:
            try:
                handler.handle(input_dto)
            except Exception as ex:
                print(ex)
                self.session.rollback()
                return
        self.session.commit()


class UserTokenAuthenticateHandlerBuss(HandlerBuss):

    def __init__(
        self,
        memory: Dict[str, Any],
        session: Session
    ):
        super().__init__(memory, session)
        self.add(
            UserTokenAuthenticateController(
                user_session=MemoryUserRepository(memory),
                user_repository=SqlalchemyUserRepository(session),
                user_token_authenticate_view=CliUserTokenAuthenticateView(),
                input_parser=CliUserTokenAuthenticateInputParser(memory)
            )
        )


class DeviceKeyAuthenticateHandlerBuss(HandlerBuss):

    def __init__(
        self,
        memory: Dict[str, Any],
        session: Session
    ):
        super().__init__(memory, session)
        self.add(
            DeviceAuthenticateController(
                device_session=MemoryDeviceRepository(memory),
                device_repository=SqlalchemyDeviceRepository(session),
                device_authenticate_view=CliDeviceAuthenticateView(),
                device_authenticate_input_parser=CliDeviceAuthenticateInputParser(
                    memory)
            )
        )
