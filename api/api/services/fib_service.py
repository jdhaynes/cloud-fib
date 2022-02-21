from api.api.services.ports.fib_service import FibServicePort
from api.api.services.ports.database import FibDatabasePort
from api.api.services.ports.message_bus import MessageBusPort


class FibService(FibServicePort):
    def __init__(self, message_bus: MessageBusPort, database: FibDatabasePort):
        self.__message_bus = message_bus
        self.__database = database

    def get_fib(self, index: int) -> int:
        fib_result = self.__database.get_fib(index)

        if fib_result is not None:
            return fib_result
        else:
            self.__message_bus.publish("values", str(index))
            return None