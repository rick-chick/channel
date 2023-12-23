from channel.adapter.gateway.record import RecordListGateway
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.gateway.record.record_repository_impl\
    import RecordRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl

RecordListGateway(
    record_repository=RecordRepositoryImpl(),
    channel_repository=ChannelRepositoryImpl(),
    user_session=UserSessionImpl(),
)
