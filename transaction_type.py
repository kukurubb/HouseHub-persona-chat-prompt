import random

class TransactionType:
    def __init__(self):
        self.transaction_type = [
            "전세",
            "매매",
            "월세"
        ]

    def get_transaction_type(self):
        return random.choice(self.transaction_type)