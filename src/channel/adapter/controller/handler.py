from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):

    @abstractmethod
    def handle(self, dto: Any) -> Any:
        pass
