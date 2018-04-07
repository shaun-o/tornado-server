import os
import blockchain.blockexplorer


class TransactionDetails():
    def __init__(self, value, address):
        self.value = str(value).encode()
        self.address = address.encode()


def read_blockchain_address(read_address):
    address = blockchain.blockexplorer.get_address(read_address)

    transactions = address.transactions
    input_details = []
    for transaction in transactions:
        for output in transaction.outputs:
            if output.address == read_address:
                for input in transaction.inputs:
                    input_details.append(TransactionDetails(
                        input.value, input.address))
    return input_details
