from iterator import DataIterator
from adapters import (
    InternalSourceAdapter,
    CSVAdapter,
    APIAdapter,
    ClientData,
    InternalSourceData,
)


def get_csv_data():
    csv_adapter = CSVAdapter(file_path="tests/clients.csv")
    return csv_adapter.get_data()


def get_api_data():
    api_adapter = APIAdapter(api_client="api_test_client")
    return api_adapter.get_data()


def get_internal_data():
    client_1 = ClientData(client_id=100, client_name="Ana", client_age=28)
    client_2 = ClientData(client_id=200, client_name="Bruno", client_age=32)
    client_3 = ClientData(client_id=300, client_name="Caio", client_age=35)

    internal_source_data = InternalSourceData(
        clients_data=[client_1, client_2, client_3]
    )

    internal_adapter = InternalSourceAdapter(source_data=internal_source_data)
    return internal_adapter.get_data()


def get_all_data():
    all_data = list()
    all_data.extend(get_csv_data())
    all_data.extend(get_api_data())
    all_data.extend(get_internal_data())
    return all_data


def main():
    data = get_all_data()
    data_iterator = DataIterator(data, sort_key="client_id",)

    for item in data_iterator:
        print(item)


if __name__ == "__main__":
    main()
