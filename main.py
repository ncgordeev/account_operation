from config import FILE_PATH

from utils.utils import load_transactions, print_transactions, sorting_transactions

if __name__ == "__main":
    raw_transactions = load_transactions(FILE_PATH)
    sorted_by_date = sorting_transactions(raw_transactions)

    print_transactions(sorted_by_date)