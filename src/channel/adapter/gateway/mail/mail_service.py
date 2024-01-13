from channel.usecase.models import MailSendInDsDto, MailSendOutDsDto
from abc import ABC, abstractmethod


class MailService(ABC):

    @abstractmethod
    def send(
        self,
        mail_dto: MailSendInDsDto
    ) -> MailSendOutDsDto:
        pass
