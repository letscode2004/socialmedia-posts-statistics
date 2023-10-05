import time
import db_manager
import blockchain_util

def track_transactions(start_block):
    current_block = start_block

    while True:
        if current_block <= blockchain_util.get_latest_block_number():
            transactions = blockchain_util.get_transaction_by_block(current_block)

            for trans in transactions:
                trans_dict = dict(trans)
                trans_dict['hash'] = str(trans.hash.hex())
                trans_dict['blockHash'] = str(trans.blockHash.hex())
                db_manager.store_transaction(trans_dict)

            print(f"Transactions from block {current_block} saved.")
            current_block += 1
            time.sleep(5)  # Avoid request limits
        else:
            print("Waiting for new blocks...")
            time.sleep(10)


if __name__ == "__main__":
    track_transactions(blockchain_util.get_latest_block_number())
