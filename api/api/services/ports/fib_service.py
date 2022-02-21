from abc import ABC, abstractmethod


class FibServicePort(ABC):
    @abstractmethod
    def get_fib(self, index: int) -> int:
        raise NotImplementedError("Abstract method not implemented.")
