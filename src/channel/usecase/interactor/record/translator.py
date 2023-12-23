from datetime import datetime
from functools import cmp_to_key
from typing import Dict, List, Optional

from channel.entity.models import Record
from channel.usecase.models import (
    ChannelListOutDsDto,
    RecordCreateInDsDto,
    RecordCreateOutDto,
    RecordListDataOutDto,
    RecordListOutDsDto,
    RecordListOutDto,
)


def compare(a: RecordListOutDsDto, b: RecordListOutDsDto) -> int:
    if a.time < b.time:
        return -1
    elif a.time > b.time:
        return 1

    if a.channel_id < b.channel_id:
        return -1
    elif a.channel_id > b.channel_id:
        return 1

    return 0


class RecordTranslator():

    def entity_to_create_in_ds(
        self,
        record: Record
    ) -> List[RecordCreateInDsDto]:
        return [
            RecordCreateInDsDto(
                time=record.time,
                channel_id=channel_id,
                value=record.values[channel_id]
            ) for channel_id in record.values
        ]

    def ds_to_create_out(
        self,
        time: datetime,
        create_out_ds_list: List[RecordCreateInDsDto]
    ) -> RecordCreateOutDto:
        values: Dict[int, float] = {}
        for create_out_ds in create_out_ds_list:
            values[create_out_ds.channel_id] = create_out_ds.value
        return RecordCreateOutDto(
            time=time,
            values=values,
        )

    def ds_to_list_out(
        self,
        list_out_ds_dto: List[RecordListOutDsDto],
        list_channel_ds_dto: List[ChannelListOutDsDto],
    ) -> RecordListOutDto:

        # ソート
        list_out_ds_dto = sorted(list_out_ds_dto, key=cmp_to_key(compare))

        # 日付ラベル
        labels = sorted(set([ds_dto.time for ds_dto in list_out_ds_dto]))

        # 変換結果
        datasets: List[RecordListDataOutDto] = []

        # 変換処理
        for channel in list_channel_ds_dto:

            # 探し終わったlist_out_ds_listのループを避けるためのoffset
            offset: int = 0

            # Y軸用のデータを、Channel毎に作成する
            data: List[Optional[float]] = []

            for date in labels:

                # 日付、channel_idで探してdataに加えていく
                target_ds_dto = RecordListOutDsDto(
                    channel_id=channel.id,
                    time=date,
                )

                is_found = False
                for ds_dto in list_out_ds_dto[offset:]:
                    c = compare(ds_dto, target_ds_dto)
                    if c < 0:
                        offset += 1
                        continue
                    elif c > 0:
                        data.append(None)
                        is_found = True
                        break
                    else:
                        offset += 1
                        data.append(ds_dto.value)
                        is_found = True
                        break

                if not is_found:
                    data.append(None)

            if not len(data) == len(labels):
                raise Exception("check code.")

            datasets.append(
                RecordListDataOutDto(
                    label=channel.name,
                    data=data
                )
            )

        return RecordListOutDto(
            labels=labels,
            datasets=datasets
        )
