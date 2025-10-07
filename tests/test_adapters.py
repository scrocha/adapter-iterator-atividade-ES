from adapters import (
    ClientData,
    InternalSourceData,
    InternalSourceAdapter,
    CSVAdapter,
    APIAdapter,
)


def test_internal_source_adapter():
    client_1 = ClientData(client_id="1", client_name="Ana", client_age=28)
    client_2 = ClientData(client_id="2", client_name="Bruno", client_age=32)
    client_3 = ClientData(client_id="3", client_name="Caio", client_age=35)

    internal_source_data = InternalSourceData(
        clients_data=[client_1, client_2, client_3]
    )

    internal_data = InternalSourceAdapter(source_data=internal_source_data)

    data = internal_data.get_data()
    assert len(data) == 3
    assert data[0]["client_name"] == "Ana"


def test_csv_adapter():
    csv_data = CSVAdapter(file_path="tests/clients.csv")
    data = csv_data.get_data()
    assert len(data) > 0
    assert data[0]["client_name"] == "Amanda"


def test_api_adapter():
    api_data = APIAdapter(api_client="api_test_client")
    data = api_data.get_data()
    assert len(data) == 3
    assert data[0]["client_name"] == "Alice"


if __name__ == "__main__":
    test_internal_source_adapter()
    test_csv_adapter()
    test_api_adapter()
    print("All tests passed.")
