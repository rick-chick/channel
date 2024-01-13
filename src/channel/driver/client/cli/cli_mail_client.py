from channel.adapter.gateway.mail.mail_service import MailService
from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto
)


class CliMailClient(MailService):

    def __init__(
        self,
    ):
        pass

    def send(
        self,
        mail_dto: MailSendInDsDto
    ) -> MailSendOutDsDto:
        print(f"Title: {mail_dto.title}")
        print(f"To:    {mail_dto.user_to}")
        print(f"Body:  {mail_dto.body}")
        return MailSendOutDsDto(
            success=True
        )
