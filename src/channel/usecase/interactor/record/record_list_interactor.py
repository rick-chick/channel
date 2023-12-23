from typing import Optional

from pydantic import ValidationError

from channel.entity.models import Record
from channel.usecase.exception import (
    BusinessException,
    UnauthorizedException,
    ValidationException,
)
from channel.usecase.input_port.record import RecordListInputPort
from channel.usecase.interactor.record.translator import RecordTranslator
from channel.usecase.models import ChannelListInDsDto, RecordListInDsDto, RecordListDataOutDto
from channel.usecase.models import RecordListInDto, RecordListOutDto
from channel.usecase.output_port.record import RecordListOututPort
from channel.usecase.repository.record import RecordListRepository


class RecordListInteractor(RecordListInputPort):

    def __init__(
            self,
            gateway: RecordListRepository,
            presenter: RecordListOututPort):
        self.gateway = gateway
        self.presenter = presenter
        self.translator = RecordTranslator()

    def list(
            self, record_dto: RecordListInDto) -> RecordListOutDto:

        try:

            # ユーザー確認
            session_user_ds_dto = self.gateway.load_session_user()
            if not session_user_ds_dto:
                raise UnauthorizedException

            record_ds_dto = RecordListInDsDto(
                **record_dto.model_dump(),
            )

            # 検索 Record
            record_res_ds_dtos = self.gateway.list(record_ds_dto)
            # 検索 Channel
            channel_res_ds_dtos = self.gateway.channel_list(
                ChannelListInDsDto(
                    device_id=record_ds_dto.device_id
                )
            )

            # 変換
            record_out_dtos = self.translator.ds_to_list_out(
                record_res_ds_dtos,
		        channel_res_ds_dtos
            )

            self.presenter.prepare_success_view(
                record_out_dtos)

            return record_out_dtos

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
