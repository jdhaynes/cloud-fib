from abc import ABC, abstractmethod


class FibDatabasePort(ABC):
    @abstractmethod
    def get_fib(self, index: int) -> int:
        raise NotImplementedError("Abstract method not implemented.")
