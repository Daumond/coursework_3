from src import utils


def test_mask_info():
    assert utils.mask_info("Maestro 1234567890123456") == "Maestro 1234 56** **** 3456"
    assert utils.mask_info("Visa Platinum 1596837868705199") == "Visa Platinum 1596 83** **** 5199"
    assert utils.mask_info("Счет 64686473678894779589") == "Счет **9589"
    assert utils.mask_info("МИР 6381702861749111") == "МИР 6381 70** **** 9111"


def test_format_transaction_date():
    assert utils.format_transaction_date("2019-02-14T17:38:09.910336") == "14.02.2019"
    assert utils.format_transaction_date("2018-08-14T05:42:30.104666") == "14.08.2018"
    assert utils.format_transaction_date("2019-05-17T01:50:00.166954") == "17.05.2019"


def test_format_operation():
    assert utils.format_transaction({
        "id": 556488059,
        "state": "CANCELED",
        "date": "2019-05-17T01:50:00.166954",
        "operationAmount": {
            "amount": "74604.56",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие счета",
        "to": "Счет 87027170579332481295"
    }) == ('17.05.2019 Открытие счета\n'
           'Счет **1295\n'
           '74604.56 USD')
