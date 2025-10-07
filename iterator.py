class DataIterator:
    def __init__(
        self, data: list[dict], sort_key: str = None, reverse: bool = False
    ):
        self._data = data
        self._index = 0
        if sort_key:
            self._data.sort(key=lambda x: int(x[sort_key]))
        if reverse:
            self._data.reverse()

    def __iter__(self):
        return self

    def __next__(self) -> dict:
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        raise StopIteration
