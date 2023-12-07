def mask_info(info):
    if info.startswith("M") or info.startswith("V"):
        card = info[:-17]
        card_number = info[-16:]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return f"{card} {masked_number}"
    elif info.startswith("Счет"):
        account_number = info[-20:]
        masked_number = f"**{account_number[-4:]}"
        return f"Счет {masked_number}"

