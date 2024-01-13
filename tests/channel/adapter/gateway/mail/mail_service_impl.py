from typing import Optional

from channel.adapter.gateway.mail.mail_service import MailService
from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto,
)
from tests.channel.factories import MailSendOutDsDtoFactory


class MailServiceImpl(MailService):

    send_in: Optional[MailSendInDsDto] = None
    send_out: MailSendOutDsDto = MailSendOutDsDtoFactory.build()

    def send(
        self,
        mail_dto: MailSendInDsDto
    ):
        self.create_in = mail_dto
        return self.send_out
