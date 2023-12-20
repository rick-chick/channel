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

from abc import ABC, abstractmethod
from typing import Optional, List


class DeviceRepository(ABC):

    @abstractmethod
    def exists_by_id(self, id: Optional[int]) -> bool:
        pass

    @abstractmethod
    def find_by_id(self, id: Optional[int]) -> Optional[DeviceOutDsDto]:
        pass

    @abstractmethod
    def list(self, ds_dto: DeviceListInDsDto) -> List[DeviceListOutDsDto]:
        pass

    @abstractmethod
    def create(self, ds_dto: DeviceCreateInDsDto) -> DeviceCreateOutDsDto:
        pass

    @abstractmethod
    def update(self, ds_dto: DeviceUpdateInDsDto) -> Optional[DeviceUpdateOutDsDto]:
        pass

    @abstractmethod
    def delete(self, ds_dto: DeviceDeleteInDsDto) -> List[DeviceDeleteOutDsDto]:
        pass

    @abstractmethod
    def find_id_by_api_key(self, api_key: str) -> Optional[int]:
        pass
