"""
Este módulo contém implementações do padrão Adapter para unificar o acesso a diferentes fontes de dados.

Classes:
- ClientData: Representa os dados de um cliente.
- InternalSourceData: Contém dados internos e fornece uma interface para acessá-los.
- Adapter: Interface abstrata para adaptadores.
- InternalSourceAdapter: Adaptador para dados internos.
- CSVAdapter: Adaptador para arquivos CSV.
- APIAdapter: Adaptador para APIs externas.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
import csv


def connect_to_api(api_client: str) -> list[dict]:
    """
    Simula a conexão a uma API externa para obter dados de clientes.

    Parâmetros:
        api_client (str): Identificador do cliente da API.

    Retorna:
        list[dict]: Lista de dicionários contendo dados de clientes.
    """
    return [
        {"client_id": "1", "client_name": "Alice", "client_age": 30},
        {"client_id": "2", "client_name": "João", "client_age": 25},
        {"client_id": "3", "client_name": "Caio", "client_age": 35},
    ]


@dataclass
class ClientData:
    """
    Representa os dados de um cliente.

    Atributos:
        client_id (str): Identificador único do cliente.
        client_name (str): Nome do cliente.
        client_age (int): Idade do cliente.
    """

    client_id: str
    client_name: str
    client_age: int


@dataclass
class InternalSourceData:
    """
    Contém dados internos e fornece uma interface para acessá-los.

    Métodos:
        get_clients() -> list[dict]: Retorna os dados dos clientes como uma lista de dicionários.
    """

    clients_data: list[ClientData]

    def get_clients(self) -> list[dict]:
        result = list()
        for client in self.clients_data:
            result.append(client.__dict__)
        return result


class Adapter(ABC):
    """
    Interface abstrata para adaptadores.

    Métodos abstratos:
        get_data(): Retorna os dados adaptados.
    """

    @abstractmethod
    def get_data(self):
        pass


class InternalSourceAdapter(Adapter):
    """
    Adaptador para dados internos.

    Métodos:
        get_data() -> list[dict]: Retorna os dados internos adaptados.
    """

    def __init__(self, source_data: InternalSourceData):
        self._source_data = source_data

    def get_data(self) -> list[dict]:
        try:
            return self._source_data.get_clients()
        except Exception as e:
            print(f"Erro ao acessar dados internos: {e}")
            return list()


class CSVAdapter(Adapter):
    """
    Adaptador para arquivos CSV.

    Métodos:
        get_data() -> list[dict]: Lê e retorna os dados do arquivo CSV.
    """

    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_data(self) -> list[dict]:
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
    """
    Adaptador para APIs externas.

    Métodos:
        get_data() -> list[dict]: Conecta-se à API e retorna os dados.
    """

    def __init__(self, api_client):
        self._api_client = api_client

    def get_data(self) -> list[dict]:
        try:
            response = connect_to_api(self._api_client)
            return response
        except Exception as e:
            print(f"Erro ao buscar dados da API: {e}")
            return list()
