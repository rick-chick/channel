from channel.adapter.gateway.mail.mail_service import MailService
from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto
)

import smtplib
import ssl
from email.mime.text import MIMEText

from channel.driver.env import GMAIL_ACCOUNT, GMAIL_PASSWORD


class GmailMailClient(MailService):

    def __init__(
        self,
    ):
        pass

    def send(
        self,
        mail_dto: MailSendInDsDto
    ) -> MailSendOutDsDto:
        msg = MIMEText(mail_dto.body, "plain", "utf-8")
        msg["Subject"] = mail_dto.title
        msg["To"] = mail_dto.user_to
        msg["From"] = GMAIL_ACCOUNT
        server = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            context=ssl.create_default_context()
        )
        server.set_debuglevel(0)
        server.login(GMAIL_ACCOUNT, GMAIL_PASSWORD)
        success = len(server.send_message(msg)) == 0
        return MailSendOutDsDto(
            success=success
        )
