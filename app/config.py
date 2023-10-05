import os
from dotenv import load_dotenv

load_dotenv()

ETHEREUM_NODE_URL = os.getenv('ETHEREUM_NODE_URL')
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')
TRANS_COLLECTION = os.getenv('TRANS_COLLECTION')