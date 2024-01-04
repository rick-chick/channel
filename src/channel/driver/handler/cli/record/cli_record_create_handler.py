from channel.driver.db.memory.memory_device_repository import MemoryDeviceRepository
from channel.driver.handler.cli.handler_buss import DeviceKeyAuthenticateHandlerBuss
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.record.cli_record_create_input_parser import CliRecordCreateInputParser
from channel.driver.view.cli.record.cli_record_create_view import CliRecordCreateView
from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import SqlalchemyRecordRepository
from channel.driver.db.memory.memory_user_repository import MemoryUserRepository
from channel.adapter.controller.record.record_create_controller import RecordCreateController


memory = {}
session = Session()

buss = DeviceKeyAuthenticateHandlerBuss(memory, session)

controller = RecordCreateController(
    user_session=MemoryUserRepository(memory),
    device_session=MemoryDeviceRepository(memory),
    record_repository=SqlalchemyRecordRepository(session),
    record_view=CliRecordCreateView(),
    input_parser=CliRecordCreateInputParser(memory),
)
buss.add(controller)

try:
    buss.handle(parse())
    session.commit()
except Exception:
    session.rollback()
