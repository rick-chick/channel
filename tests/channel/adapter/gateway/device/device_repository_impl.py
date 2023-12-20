from channel.adapter.gateway.device.device_repository import (
    DeviceRepository
)
from channel.usecase.models import (
    DeviceOutDsDto,
    DeviceCreateInDsDto,
    DeviceCreateOutDsDto,
    DeviceUpdateInDsDto,
    DeviceUpdateOutDsDto,
    DeviceDeleteInDsDto,
    DeviceDeleteOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
)

from typing import Optional, List


class DeviceRepositoryImpl(DeviceRepository):

    create_out: DeviceCreateOutDsDto
    find_id_by_api_key_out: Optional[int]

    def exists_by_id(self, id: Optional[int]) -> bool:
        return False

    def find_by_id(self, id: Optional[int]) -> Optional[DeviceOutDsDto]:
        pass

    def find_id_by_api_key(self, api_key: str) -> Optional[int]:
        self.api_key_in = api_key
        return self.find_id_by_api_key_out

    def list(self, ds_dto: DeviceListInDsDto) -> List[DeviceListOutDsDto]:
        return []

    def create(self, ds_dto: DeviceCreateInDsDto) -> DeviceCreateOutDsDto:
        return self.create_out

    def update(self, ds_dto: DeviceUpdateInDsDto) -> DeviceUpdateOutDsDto:
        pass

    def delete(self, ds_dto: DeviceDeleteInDsDto) -> List[DeviceDeleteOutDsDto]:
        return []
