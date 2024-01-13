from flask import Flask, jsonify, redirect, request, url_for
from channel.adapter.controller.channel.channel_create_controller import ChannelCreateController
from channel.adapter.controller.channel.channel_delete_controller import ChannelDeleteController
from channel.adapter.controller.channel.channel_list_controller import ChannelListController
from channel.adapter.controller.channel.channel_update_controller import ChannelUpdateController
from channel.adapter.controller.device.device_create_controller import DeviceCreateController
from channel.adapter.controller.device.device_delete_controller import DeviceDeleteController
from channel.adapter.controller.device.device_list_controller import DeviceListController
from channel.adapter.controller.record.record_create_controller import RecordCreateController
from channel.adapter.controller.record.record_list_controller import RecordListController

from channel.adapter.controller.user.user_authenticate_controller import (
    UserAuthenticateController,
)
from channel.adapter.controller.user.user_signup_controller import UserSignupController
from channel.adapter.controller.user.user_update_controller import UserUpdateController
from channel.adapter.controller.user_token.user_token_refresh_controller import UserTokenRefreshController
from channel.driver.client.gmail.gmail_mail_client import GmailMailClient
from channel.driver.db.memory.memory_device_repository import MemoryDeviceRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.sqlalchemy_device_repository import SqlalchemyDeviceRepository
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import SqlalchemyRecordRepository
from channel.driver.db.sqlalchemy.sqlalchemy_signup_repository import SqlalchemySignupRepository
from channel.driver.db.sqlalchemy.sqlalchemy_user_token_repository import SqlalchemyUserTokenRepository
from channel.driver.db.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from channel.driver.env import (
    ALLOWD_ORIGINS,
    PASSWORD_RESET_URL
)
from channel.driver.handler.cli.handler_buss import HandlerBuss, UserTokenAuthenticateHandlerBuss
from channel.driver.handler.flask.channel.flask_channel_create_input_parser import FlaskChannelCreateInputParser
from channel.driver.handler.flask.channel.flask_channel_delete_input_parser import FlaskChannelDeleteInputParser
from channel.driver.handler.flask.channel.flask_channel_list_input_parser import FlaskChannelListInputParser
from channel.driver.handler.flask.channel.flask_channel_update_input_parser import FlaskChannelUpdateInputParser
from channel.driver.handler.flask.device.flask_device_create_input_parser import FlaskDeviceCreateInputParser
from channel.driver.handler.flask.device.flask_device_delete_input_parser import FlaskDeviceDeleteInputParser
from channel.driver.handler.flask.device.flask_device_list_input_parser import FlaskDeviceListInputParser
from channel.driver.handler.flask.handler_buss import (
    FlaskDeviceKeyAuthenticateHandlerBuss,
    FlaskUserTokenAuthenticateHandlerBuss
)
from channel.driver.handler.flask.record.flask_record_create_input_parser import FlaskRecordCreateInputParser
from channel.driver.handler.flask.record.flask_record_list_input_parser import FlaskRecordListInputParser
from channel.driver.handler.flask.user.flask_user_authenticate_input_parser import (
    FlaskUserAuthenticateInputParser,
)
from channel.driver.handler.flask.user.flask_user_signup_input_parser import FlaskUserSignupInputParser
from channel.driver.handler.flask.user.flask_user_update_input_parser import FlaskUserUpdateInputParser
from channel.driver.handler.flask.user_token.flask_user_token_refresh_input_parser import (
    FlaskUserTokenRefreshInputParser
)
from channel.driver.view.flask.channel.flask_channel_create_view import FlaskChannelCreateView
from channel.driver.view.flask.channel.flask_channel_delete_view import FlaskChannelDeleteView
from channel.driver.view.flask.channel.flask_channel_list_view import FlaskChannelListView
from channel.driver.view.flask.channel.flask_channel_update_view import FlaskChannelUpdateView
from channel.driver.view.flask.device.flask_device_create_view import FlaskDeviceCreateView
from channel.driver.view.flask.device.flask_device_delete_view import FlaskDeviceDeleteView
from channel.driver.view.flask.device.flask_device_list_view import FlaskDeviceListView
from channel.driver.view.flask.record.flask_record_create_view import FlaskRecordCreateView
from channel.driver.view.flask.record.flask_record_list_view import FlaskRecordListView
from channel.driver.view.flask.user.flask_user_authenticate_view import (
    FlaskUserAuthenticateView,
)
from channel.driver.view.flask.user.flask_user_signup_view import FlaskUserSignupView
from channel.driver.view.flask.user.flask_user_update_view import FlaskUserUpdateView
from flask_cors import CORS
from channel.driver.view.flask.user_token.flask_user_token_refresh_view import FlaskUserTokenRefreshView

from channel.usecase.exception import UnauthenticateException

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


@app.route('/user_token/refresh', methods=["POST"])
def user_token_refresh():
    memory = {}
    session = Session()

    buss = HandlerBuss(memory, session)

    view = FlaskUserTokenRefreshView()
    controller = UserTokenRefreshController(
        user_token_refresh_input_parser=FlaskUserTokenRefreshInputParser(
            memory),
        user_token_repository=SqlalchemyUserTokenRepository(session),
        user_repository=SqlalchemyUserRepository(session),
        user_token_refresh_view=view,
    )
    buss.add(controller)
    buss.handle(request)
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


@app.route('/user/signup', methods=["POST"])
def user_signup():
    memory = {}
    session = Session()

    buss = HandlerBuss(memory, session)

    view = FlaskUserSignupView()
    controller = UserSignupController(
        signup_repository=SqlalchemySignupRepository(session),
        user_repository=SqlalchemyUserRepository(session),
        mail_service=GmailMailClient(),
        user_signup_view=view,
        user_signup_input_parser=FlaskUserSignupInputParser(),
        password_reset_url=PASSWORD_RESET_URL,
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


@app.route('/device/delete', methods=["POST"])
def device_delete():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskDeviceDeleteView()
    controller = DeviceDeleteController(
        device_delete_input_parser=FlaskDeviceDeleteInputParser(memory),
        user_session=MemoryUserRepository(memory),
        device_repository=SqlalchemyDeviceRepository(session),
        channel_repository=SqlalchemyChannelRepository(session),
        record_repository=SqlalchemyRecordRepository(session),
        device_delete_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/devices', methods=["POST"])
def device_list():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskDeviceListView()
    controller = DeviceListController(
        device_list_input_parser=FlaskDeviceListInputParser(memory),
        user_session=MemoryUserRepository(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        device_repository=SqlalchemyDeviceRepository(session),
        record_repository=SqlalchemyRecordRepository(session),
        device_list_view=view,
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


@app.route('/channel', methods=["PUT"])
def channel_update():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskChannelUpdateView()
    controller = ChannelUpdateController(
        channel_update_input_parser=FlaskChannelUpdateInputParser(memory),
        user_session=MemoryUserRepository(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        channel_update_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/channel/delete', methods=["POST"])
def channel_delete():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskChannelDeleteView()
    controller = ChannelDeleteController(
        channel_delete_input_parser=FlaskChannelDeleteInputParser(memory),
        user_session=MemoryUserRepository(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        channel_delete_view=view,
    )
    buss.add(controller)

    buss.handle(request)
    return view.render()


@app.route('/channels', methods=["POST"])
def channel_list():
    memory = {}
    session = Session()

    buss = FlaskUserTokenAuthenticateHandlerBuss(memory, session)

    view = FlaskChannelListView()
    controller = ChannelListController(
        channel_list_input_parser=FlaskChannelListInputParser(memory),
        user_session=MemoryUserRepository(memory),
        channel_repository=SqlalchemyChannelRepository(session),
        device_repository=SqlalchemyDeviceRepository(session),
        channel_list_view=view,
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


@app.errorhandler(UnauthenticateException)
def handle_unauthenticate_exception(error):
    response = jsonify({'error': 'Unauthenticated'})
    response.status_code = 401
    return response


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


@app.errorhandler(405)
def page_method_not_allowed(e):
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)
