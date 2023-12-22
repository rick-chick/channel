
from datetime import datetime
from channel.usecase.models import RecordCreateInDto


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
