from abc import ABC, abstractmethod
from typing import Callable


class MessageBusPort(ABC):
    @abstractmethod
    def publish(self, queue: str, body: str) -> None:
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def subscribe(self, queue: str, callback: Callable[[str], None]) -> None:
        raise NotImplementedError("Abstract method not implemented.")
