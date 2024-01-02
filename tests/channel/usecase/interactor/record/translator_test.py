

from datetime import datetime, timedelta
from typing import List

from channel.usecase.interactor.record.translator import RecordTranslator
from channel.usecase.models import ChannelListOutDsDto, RecordListOutDsDto


def test_ds_to_list_out_when_input_length_is_zero():
    channel_ds_dto: List[ChannelListOutDsDto] = []
    record_ds_dto: List[RecordListOutDsDto] = []
    target = RecordTranslator()
    ret = target.ds_to_list_out(
        record_ds_dto,
        channel_ds_dto,
    )

    assert len(ret.datasets) == 0


def test_ds_to_list_out_when_input_length_is_one():
    time = datetime.now()

    channel_ds_dto: List[ChannelListOutDsDto] = [
        ChannelListOutDsDto(
            id=1,
            name="hoge",
            unit="huga",
            device_id=1

        )
    ]
    record_ds_dto: List[RecordListOutDsDto] = [
        RecordListOutDsDto(
            channel_id=1,
            time=time,
            value=5
        )
    ]
    target = RecordTranslator()
    ret = target.ds_to_list_out(
        record_ds_dto,
        channel_ds_dto,
    )

    assert len(ret.labels) == 1
    assert ret.labels[0] == time
    assert len(ret.datasets) == 1
    assert ret.datasets[0].label == "hoge"
    assert len(ret.datasets[0].data) == 1
    assert ret.datasets[0].data[0] == 5


def test_ds_to_list_out_when_data_channel_count_is_two():
    time = datetime.now()

    channel_ds_dto: List[ChannelListOutDsDto] = [
        ChannelListOutDsDto(
            id=1,
            name="hoge",
            unit="huga",
            device_id=1
        ),
        ChannelListOutDsDto(
            id=2,
            name="bra",
            unit="role",
            device_id=1
        )
    ]
    record_ds_dto: List[RecordListOutDsDto] = [
        RecordListOutDsDto(
            channel_id=1,
            time=time,
            value=5
        ),
        RecordListOutDsDto(
            channel_id=2,
            time=time,
            value=6
        )
    ]
    target = RecordTranslator()
    ret = target.ds_to_list_out(
        record_ds_dto,
        channel_ds_dto,
    )

    assert len(ret.labels) == 1
    assert ret.labels[0] == time
    assert len(ret.datasets) == 2
    assert ret.datasets[0].label == "hoge"
    assert ret.datasets[1].label == "bra"
    assert len(ret.datasets[0].data) == 1
    assert len(ret.datasets[1].data) == 1
    assert ret.datasets[0].data[0] == 5
    assert ret.datasets[1].data[0] == 6


def test_ds_to_list_out_when_data_label_count_is_two():
    time1 = datetime.now()
    time2 = datetime.now() - timedelta(minutes=2)

    channel_ds_dto: List[ChannelListOutDsDto] = [
        ChannelListOutDsDto(
            id=1,
            name="hoge",
            unit="huga",
            device_id=1
        ),
        ChannelListOutDsDto(
            id=2,
            name="bra",
            unit="role",
            device_id=1
        )
    ]
    record_ds_dto: List[RecordListOutDsDto] = [
        RecordListOutDsDto(
            channel_id=1,
            time=time1,
            value=5
        ),
        RecordListOutDsDto(
            channel_id=1,
            time=time2,
            value=6
        )
    ]
    target = RecordTranslator()
    ret = target.ds_to_list_out(
        record_ds_dto,
        channel_ds_dto,
    )

    assert len(ret.labels) == 2
    assert ret.labels[0] == time2
    assert ret.labels[1] == time1
    assert len(ret.datasets) == 2
    assert ret.datasets[0].label == "hoge"
    assert ret.datasets[1].label == "bra"
    assert len(ret.datasets[0].data) == 2
    assert len(ret.datasets[1].data) == 2
    assert ret.datasets[0].data[0] == 6
    assert ret.datasets[0].data[1] == 5
    assert ret.datasets[1].data[0] is None
    assert ret.datasets[1].data[1] is None
