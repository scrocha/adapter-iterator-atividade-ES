class DataIterator:
    def __init__(self, data: list[dict]):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> dict:
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        raise StopIteration
