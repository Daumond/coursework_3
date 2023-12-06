def mask_info(info):
    if info.startswith("M") or info.startswith("V"):
        card = info[:-16]
        card_number = info[-16:]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return card + masked_number
    elif info.startswith("Счет"):
        account_number = info[-20:]
        masked_number = f"**{account_number[-4:]}"
        return "Счет " + masked_number

info1 = "Maestro 1596837868705199"
info2 = "Счет 64686473678894779589"
info3 = "Visa Platinum 1596837868705199"
info4 = "Maestercard 1596837868705199"

print(mask_info(info1))
print(mask_info(info2))
print(mask_info(info3))
print(mask_info(info4))