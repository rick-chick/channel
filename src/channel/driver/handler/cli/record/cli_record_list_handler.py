from channel.driver.db.sqlalchemy.conf import Session
from channel.driver.db.sqlalchemy.sqlalchemy_channel_repository import SqlalchemyChannelRepository
from channel.driver.handler.cli.parser import parse
from channel.driver.handler.cli.record.cli_record_list_input_parser import CliRecordListInputParser
from channel.driver.view.cli.record.cli_record_list_view import CliRecordListView
from channel.driver.db.sqlalchemy.sqlalchemy_record_repository import (
    SqlalchemyRecordRepository
)
from channel.driver.db.memory.memory_user_repository import (
    MemoryUserRepository
)
from channel.adapter.controller.record.record_list_controller import (
    RecordListController
)
from channel.driver.handler.cli.handler_buss import (
    UserTokenAuthenticateHandlerBuss
)


session = Session()
memory = {}

buss = UserTokenAuthenticateHandlerBuss(memory, session)

controller = RecordListController(
    record_list_input_parser=CliRecordListInputParser(memory),
    channel_repository=SqlalchemyChannelRepository(session),
    user_session=MemoryUserRepository(memory),
    record_repository=SqlalchemyRecordRepository(session),
    record_list_view=CliRecordListView(),
)
buss.add(controller)

buss.handle(parse())
