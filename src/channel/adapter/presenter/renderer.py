from abc import ABC, abstractmethod
from typing import Any


class Renderer(ABC):

    @abstractmethod
    def render(self) -> Any:
        pass
