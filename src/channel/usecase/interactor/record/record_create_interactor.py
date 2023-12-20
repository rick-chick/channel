from channel.usecase.input_port.record import RecordCreateInputPort
from channel.usecase.repository.record import RecordCreateRepository
from channel.usecase.output_port.record import RecordCreateOututPort
from channel.usecase.interactor.record.translator import RecordTranslator

from channel.usecase.models import (
    RecordCreateInDto,
    RecordCreateOutDto
)
from channel.usecase.exception import (
    BusinessException,
    ValidationException,
    UnauthorizedException
)

from channel.entity.models import Record

from pydantic import ValidationError


class RecordCreateInteractor(RecordCreateInputPort):

    translator: RecordTranslator

    def __init__(
            self,
            gateway: RecordCreateRepository,
            presenter: RecordCreateOututPort):
        self.gateway = gateway
        self.presenter = presenter
        self.translator = RecordTranslator()

    def create(
            self, record_dto: RecordCreateInDto) -> RecordCreateOutDto:

        try:

            device_ds_dto = self.gateway.load_session_device()

            if device_ds_dto is None:
                raise UnauthorizedException

            record = Record(
                **record_dto.model_dump(),
                device_id=device_ds_dto.id,
            )

            record_ds_dto_list = self.translator.entity_to_create_in_ds(
                record
            )

            record_res_ds_dto_list = []
            for record_ds_dto in record_ds_dto_list:
                record_res_ds_dto_list.append(
                    self.gateway.create(record_ds_dto)
                )

            record_out_dto = self.translator.ds_to_create_out(
                record.time,
                record_res_ds_dto_list
            )

            self.presenter.prepare_success_view(
                record_out_dto
            )

            return record_out_dto

        except ValidationError as e:
            ex = ValidationException(e)
            self.presenter.prepare_fail_view(ex)
            raise ex

        except BusinessException as e:
            self.presenter.prepare_fail_view(e)
            raise e
