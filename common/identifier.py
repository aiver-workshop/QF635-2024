from datetime import datetime
import uuid


# A class to generate unique identifier of an order
class OrderIdGenerator:
    def __init__(self, prefix: str):
        random_id = uuid.uuid4()
        date_str = datetime.now().strftime("%Y%m%d")
        self._prefix = prefix + "-" + date_str + "-" + str(random_id)[0:8] + "-"
        self._counter = 0

    def get_prefix(self) -> str:
        return self._prefix

    def next(self) -> str:
        self._counter += 1
        return self._prefix + str(self._counter)

    def match(self, client_id: str) -> bool:
        if client_id:
            return client_id.startswith(self._prefix)
        return False


if __name__ == '__main__':
    id_generator = OrderIdGenerator('algo')
    identifier = id_generator.next()
    print(identifier)
