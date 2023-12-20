from abc import ABC, abstractmethod
from typing import Any


class InputParser(ABC):

    @abstractmethod
    def parse(self, in_dto: Any) -> Any:
        pass
