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
from channel.driver.handler.flask.device.flask_device_authenticate_input_parser import FlaskDeviceAuthenticateInputParser
from channel.driver.handler.flask.user_token.flask_user_token_authenticate_input_parser import FlaskUserTokenAuthenticateInputParser
from channel.driver.view.flask.device.flask_device_authenticate_view import FlaskDeviceAuthenticateView
from channel.driver.view.flask.user_token import FlaskUserTokenAuthenticateView


class FlaskHandlerBuss():

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
                self.session.rollback()
                raise ex
        self.session.commit()


class FlaskUserTokenAuthenticateHandlerBuss(FlaskHandlerBuss):

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
                user_token_authenticate_view=FlaskUserTokenAuthenticateView(),
                input_parser=FlaskUserTokenAuthenticateInputParser(memory)
            )
        )


class FlaskDeviceKeyAuthenticateHandlerBuss(FlaskHandlerBuss):

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
                device_authenticate_view=FlaskDeviceAuthenticateView(),
                device_authenticate_input_parser=FlaskDeviceAuthenticateInputParser(
                    memory)
            )
        )
