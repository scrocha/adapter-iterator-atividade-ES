from iterator import DataIterator

def test_data_iterator():
    sample_data = [
        {"client_id": "1", "client_name": "Ana", "client_age": 28},
        {"client_id": "2", "client_name": "Bruno", "client_age": 32},
        {"client_id": "3", "client_name": "Caio", "client_age": 35},
    ]

    data_iterator = DataIterator(data=sample_data)

    collected_data = list()
    for item in data_iterator:
        collected_data.append(item)

    assert len(collected_data) == 3
    assert collected_data[0]["client_name"] == "Ana"
    assert collected_data[1]["client_name"] == "Bruno"
    assert collected_data[2]["client_name"] == "Caio"
