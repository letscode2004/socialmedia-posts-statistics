import os
from web3 import Web3
from pymongo import MongoClient
import time

load_dotenv()

ETHEREUM_NODE_URL = os.getenv('ETHEREUM_NODE_URL')
# Connect to Ethereum node (You can use your node or infura.io)
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')
TRANS_COLLECTION = os.getenv('TRANS_COLLECTION')

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
trans_collection = db[TRANS_COLLECTION]

def get_latest_block_number():
    return w3.eth.block_number


def get_transaction_by_block(block_number):
    block = w3.eth.get_block(block_number, full_transactions=True)
    return block['transactions']


def store_transaction(transaction):
    trans_collection.insert_one(transaction)


def track_transactions(start_block):
    current_block = start_block

    while True:
        if current_block <= get_latest_block_number():
            transactions = get_transaction_by_block(current_block)

            for trans in transactions:
                trans_dict = dict(trans)
                trans_dict['hash'] = str(trans.hash.hex())
                trans_dict['blockHash'] = str(trans.blockHash.hex())
                store_transaction(trans_dict)

            print(f"Transactions from block {current_block} saved.")
            current_block += 1
            time.sleep(5)  # Add delay to avoid exceeding request limits
        else:
            print("Waiting for new blocks...")
            time.sleep(10)


if __name__ == "__main__":
    track_transactions(get_latest_block_number())
