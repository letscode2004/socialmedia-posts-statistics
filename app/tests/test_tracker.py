# app/tests/test_tracker.py

import unittest
from unittest.mock import Mock, patch
from app.tracker import get_latest_block_number, get_transaction_by_block, store_transaction


class TrackerTests(unittest.TestCase):
    def test_get_latest_block_number(self):
        self.assertIsInstance(get_latest_block_number(), int)

    def test_latest_block_number_positive(self):
        self.assertGreater(get_latest_block_number(), 0)

    @patch('app.tracker.w3.eth.get_block')
    def test_get_transaction_by_block(self, mock_get_block):
        mock_transaction = Mock()
        mock_transaction.hash.hex.return_value = 'mock_hash'
        mock_transaction.blockHash.hex.return_value = 'mock_block_hash'
        mock_get_block.return_value = {'transactions': [mock_transaction]}

        transactions = get_transaction_by_block(1)

        self.assertIsInstance(transactions, list)
        self.assertEqual(transactions[0]['hash'], 'mock_hash')
        self.assertEqual(transactions[0]['blockHash'], 'mock_block_hash')

    @patch('app.db.trans_collection')
    def test_store_transaction(self, mock_trans_collection):
        mock_transaction = {'hash': 'mock_hash', 'blockHash': 'mock_block_hash'}

        store_transaction(mock_transaction)

        mock_trans_collection.insert_one.assert_called_with(mock_transaction)
