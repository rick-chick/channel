from channel.usecase.models import (
    RecordCreateInDsDto,
    RecordCreateOutDto
)
from channel.entity.models import Record
from typing import List, Dict
from datetime import datetime


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
