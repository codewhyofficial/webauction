import os
from eth_account.messages import encode_defunct
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()
INFURA_RPC_URL = os.getenv("INFURA_RPC_URL")

def verify_signature(wallet_address: str, signed_message: str) -> bool:
    message = encode_defunct(text="Sign this message to authenticate")
    recovered_address = Account.recover_message(message, signature=signed_message)
    return recovered_address.lower() == wallet_address.lower()
