from dataclasses import dataclass
from abc import ABC, abstractmethod
import csv


def connect_to_api(api_client):

    return [
        {"client_id": "1", "client_name": "Alice", "client_age": 30},
        {"client_id": "2", "client_name": "João", "client_age": 25},
        {"client_id": "3", "client_name": "Caio", "client_age": 35},
    ]


@dataclass
class ClientData:
    client_id: str
    client_name: str
    client_age: int


@dataclass
class InternalSourceData:
    clients_data: list[ClientData]


class Adapter(ABC):
    @abstractmethod
    def get_data(self):
        pass


class InternalSourceAdapter(Adapter):
    def __init__(self, source_data: InternalSourceData):
        self._source_data = source_data

    def get_data(self):
        try:
            return self._source_data.clients_data
        except Exception as e:
            print(f"Erro ao acessar dados internos: {e}")
            return list()


class CSVAdapter(Adapter):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_data(self):
        try:
            with open(self._file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em '{self._file_path}'")
            return list()
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")
            return list()


class APIAdapter(Adapter):
    def __init__(self, api_client):
        self._api_client = api_client

    def get_data(self):
        try:
            response = connect_to_api(self._api_client)
            return response
        except Exception as e:
            print(f"Erro ao buscar dados da API: {e}")
            return list()
