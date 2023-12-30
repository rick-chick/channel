from datetime import timedelta, timezone

from pydantic import ValidationError

from channel.usecase.exception import (
    BusinessException,
    UnauthorizedException,
    ValidationException,
)
from channel.usecase.input_port.record import RecordListInputPort
from channel.usecase.interactor.record.translator import RecordTranslator
from channel.usecase.models import ChannelListInDsDto, RecordListInDsDto, RecordListOutDsDto
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

            # 検索 Channel
            channel_res_ds_dtos = self.gateway.channel_list(
                ChannelListInDsDto(
                    device_id=record_dto.device_id
                )
            )

            # 検索 Record
            record_ds_dto = RecordListInDsDto(
                **record_dto.model_dump(),
                channel_ids=[channel.id for channel in channel_res_ds_dtos]
            )
            record_res_ds_dtos = self.gateway.list(
                record_ds_dto
            )

            # 集計
            current_start = record_dto.date_from
            records = []
            i = 0
            while current_start <= record_dto.date_to:
                # 集計範囲の終了位置
                current_end = current_start + \
                    timedelta(minutes=record_dto.span)

                # 各チャンネルの集計値
                sums = {}
                counts = {}
                for channel in channel_res_ds_dtos:
                    sums[channel.id] = 0
                    counts[channel.id] = 0

                # 集計
                while i < len(record_res_ds_dtos):
                    record = record_res_ds_dtos[i]
                    if (current_start.tzinfo or current_end.tzinfo):
                        time = record.time.astimezone(timezone.utc)
                    else:
                        time = record.time

                    # 範囲外の場合はブレーク
                    if current_start > time:
                        i += 1
                        continue

                    if current_end <= time:
                        break

                    if record.channel_id in sums:
                        sums[record.channel_id] += record.value
                        counts[record.channel_id] += 1

                    i += 1

                # 平均を求める
                for channel in channel_res_ds_dtos:
                    average = None
                    if counts[channel.id] > 0:
                        average = sums[channel.id] / counts[channel.id]
                    records.append(RecordListOutDsDto(
                        time=current_start,
                        channel_id=channel.id,
                        value=average,
                    ))

                # 集計範囲の開始位置
                current_start = current_start + \
                    timedelta(minutes=record_dto.span)

            # 変換
            record_out_dtos = self.translator.ds_to_list_out(
                records,
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
