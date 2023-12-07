from src import utils

def test_mask_info():
    assert utils.mask_info("Maestro 1234567890123456") == "Maestro 1234 56** **** 3456"
    assert utils.mask_info("Visa Platinum 1596837868705199") == "Visa Platinum 1596 83** **** 5199"
    assert utils.mask_info("Счет 64686473678894779589") == "Счет **9589"
