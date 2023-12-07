import utils


def main():
    file_path = 'operations.json'
    transactions = utils.read_json_file(file_path)

    # Фильтрация и сортировка операций
    executed_transactions = [t for t in transactions if 'state' in t and t['state'] == 'EXECUTED']
    sorted_transactions = sorted(executed_transactions, key=lambda x: x['date'], reverse=True)

    # Вывод последних 5 операций
    for transaction in sorted_transactions[:5]:
        print(utils.format_transaction(transaction))
        print()


if __name__ == "__main__":
    main()
