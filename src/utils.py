from datetime import datetime
import json


def read_json_file(file_path):
    """Открываем файл на чтение, возвращаем информацию списком"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def mask_info(info):
    """Максирует информацию о карте или счете"""
    if info.startswith("Счет"):
        account_number = info[-20:]
        masked_number = f"**{account_number[-4:]}"
        return f"Счет {masked_number}"
    else:
        card = info[:-17]
        card_number = info[-16:]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return f"{card} {masked_number}"


def format_transaction_date(date_str):
    """Преобразовывает дату в упрощенный формат"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


def format_transaction(transaction):
    """Собирает воедино информацию об операции. Если нет отправителя, то выводится только инфо о получателе"""
    if 'from' in transaction:
        from_info = f"{mask_info(transaction['from'])} -> "
    else:
        from_info = ""

    to_info = mask_info(transaction['to'])

    formatted_output = (
        f"{format_transaction_date(transaction['date'])} {transaction['description']}\n"
        f"{from_info}{to_info}\n"
        f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}"
    )
    return formatted_output
