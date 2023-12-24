from flask import Flask, request
from channel.adapter.controller.channel.channel_create_controller import ChannelCreateController
from channel.adapter.controller.device.device_create_controller import DeviceCreateController
from channel.adapter.controller.record.record_create_controller import RecordCreateController
from channel.adapter.controller.record.record_list_controller import RecordListController

from channel.adapter.controller.user.user_authenticate_controller import (
    UserAuthenticateController,
)
from channel.adapter.controller.user.user_update_controller import UserUpdateController
from channel.driver.db.memory.memory_device_repository import MemoryDeviceRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import SqlalchemyDeviceRepository
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import SqlalchemyRecordRepository
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from channel.driver.env import ALLOWD_ORIGINS
from channel.driver.handler.cli.handler_buss import UserTokenAuthenticateHandlerBuss
from channel.driver.handler.flask.channel.flask_channel_create_input_parser import FlaskChannelCreateInputParser
from channel.driver.handler.flask.device.flask_device_create_input_parser import FlaskDeviceCreateInputParser
from channel.driver.handler.flask.handler_buss import FlaskDeviceKeyAuthenticateHandlerBuss, FlaskUserTokenAuthenticateHandlerBuss
from channel.driver.handler.flask.record.flask_record_create_input_parser import FlaskRecordCreateInputParser
from channel.driver.handler.flask.record.flask_record_list_input_parser import FlaskRecordListInputParser
from channel.driver.handler.flask.user.flask_user_authenticate_input_parser import (
    FlaskUserAuthenticateInputParser,
)
from channel.driver.handler.flask.user.flask_user_update_input_parser import FlaskUserUpdateInputParser
from channel.driver.view.flask.channel.flask_channel_create_view import FlaskChannelCreateView
from channel.driver.view.flask.device.flask_device_create_view import FlaskDeviceCreateView
from channel.driver.view.flask.record.flask_record_create_view import FlaskRecordCreateView
from channel.driver.view.flask.record.flask_record_list_view import FlaskRecordListView
from channel.driver.view.flask.user.flask_user_authenticate_view import (
    FlaskUserAuthenticateView,
)
from channel.driver.view.flask.user.flask_user_update_view import FlaskUserUpdateView
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=ALLOWD_ORIGINS)


@app.route('/user/authenticate', methods=["POST"])
def user_authenticate():
    memory = {}
    session = Session()

    view = FlaskUserAuthenticateView()
    controller = UserAuthenticateController(
        user_authenticate_input_parser=FlaskUserAuthenticateInputParser(
            memory),
        user_session=MemoryUserRepository(memory),
        user_repository=SqlalchemyUserRepository(session),
        user_authenticate_view=view,
    )
    controller.handle(request)
    return view.render()


@app.route('/user', methods=["PUT"])
def user_update():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskUserUpdateView()
    controller = UserUpdateController(
        user_update_input_parser=FlaskUserUpdateInputParser(memory),
        user_session=MemoryUserRepository(memory),
        user_repository=SqlalchemyUserRepository(session),
        user_update_view=view,
    )
    buss.add(controller)
    buss.handle(request)
    return view.render()


@app.route('/device', methods=["POST"])
def device_create():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskDeviceCreateView()
    controller = DeviceCreateController(
        input_parser=FlaskDeviceCreateInputParser(memory),
        user_session=MemoryUserRepository(memory),
        device_repository=SqlalchemyDeviceRepository(session),
        device_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/channel', methods=["POST"])
def channel_create():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskChannelCreateView()
    controller = ChannelCreateController(
        parser=FlaskChannelCreateInputParser(memory),
        user_session=MemoryUserRepository(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        channel_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/record', methods=["POST"])
def record_create():
    memory = {}
    session = Session()

    buss = FlaskDeviceKeyAuthenticateHandlerBuss(memory, session)

    view = FlaskRecordCreateView()
    controller = RecordCreateController(
        input_parser=FlaskRecordCreateInputParser(memory),
        device_session=MemoryDeviceRepository(memory),
        user_session=MemoryUserRepository(memory),
        record_repository=SqlalchemyRecordRepository(session),
        record_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/records', methods=["POST"])
def record_list():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskRecordListView()
    controller = RecordListController(
        record_list_input_parser=FlaskRecordListInputParser(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        user_session=MemoryUserRepository(memory),
        record_repository=SqlalchemyRecordRepository(session),
        record_list_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
