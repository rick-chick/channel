from channel.adapter.controller.record.record_list_controller import RecordListController
from tests.channel.adapter.controller.record.record_list_input_parser_impl import RecordListInputParserImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.record.record_repository_impl import RecordRepositoryImpl
from tests.channel.adapter.presenter.record.record_list_view_impl import RecordListViewImpl
from tests.channel.factories import RecordListInDtoFactory


def test_success():
    target = RecordListController(
        user_session=UserSessionImpl(),
        record_repository=RecordRepositoryImpl(),
        channel_repository=ChannelRepositoryImpl(),
        record_list_view=RecordListViewImpl(),
        record_list_input_parser=RecordListInputParserImpl(),
    )
    target.handle(RecordListInDtoFactory.build())
