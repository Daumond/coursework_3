from datetime import datetime


def mask_info(info):
    if info.startswith("M") or info.startswith("V") or info.startswith("М"):
        card = info[:-17]
        card_number = info[-16:]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return f"{card} {masked_number}"
    elif info.startswith("Счет"):
        account_number = info[-20:]
        masked_number = f"**{account_number[-4:]}"
        return f"Счет {masked_number}"


def format_transaction_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
