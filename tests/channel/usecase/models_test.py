
from datetime import datetime, timedelta, timezone
from channel.usecase.models import RecordCreateInDto, RecordListInDto


def test_record_in_dto_time_from_unixtime():
    data = {
        "api_key": "test",
        "time": 0,
        "values": {}
    }
    ret = RecordCreateInDto(**data)
    assert ret.time.year == 1970

    now = datetime.now()
    data = {
        "api_key": "test",
        "time": now.timestamp(),
        "values": {}
    }
    ret = RecordCreateInDto(**data)

    assert ret.time.year == now.year


def test_record_in_dto_timezone():
    time = datetime.now()
    model = {
        "date_from": time,
        "date_to": time,
        "device_id": 1,
        "span": 30,
    }
    rec = RecordListInDto.model_validate(
        model
    )

    assert not time.tzinfo

    assert rec.date_from.tzinfo is None
    assert rec.date_to.tzinfo is None
    assert rec.date_from == time
    assert rec.date_to == time

    jst = timezone(timedelta(hours=9))

    time = datetime.now(jst)

    model = {
        "date_from": time,
        "date_to": time,
        "device_id": 1,
        "span": 30,
    }
    rec = RecordListInDto.model_validate(
        model
    )

    assert time.tzinfo

    assert rec.date_from.tzinfo is None
    assert rec.date_to.tzinfo is None
    assert rec.date_from.hour == time.astimezone(timezone.utc).hour
    assert rec.date_to.hour == time.astimezone(timezone.utc).hour
