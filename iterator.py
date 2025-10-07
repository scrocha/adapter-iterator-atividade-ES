"""
Este módulo contém a implementação do padrão Iterator para percorrer coleções de dados.

Classes:
- DataIterator: Iterador genérico para coleções de dados.
"""


class DataIterator:
    """
    Iterador genérico para coleções de dados.

    Métodos:
        __init__(data: list[dict], sort_key: str = None, reverse: bool = False):
            Inicializa o iterador com os dados fornecidos.
        __iter__() -> DataIterator:
            Retorna o próprio iterador.
        __next__() -> dict:
            Retorna o próximo item da coleção ou levanta StopIteration.
    """

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
