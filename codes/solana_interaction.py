from solana.rpc.api import Client
import base58

def get_wallet_balance(wallet_address: str):
    """
    Retrieve the Solana wallet balance for a given address.
    """
    client = Client("https://api.mainnet-beta.solana.com")
    wallet_address = base58.b58decode(wallet_address)
    balance = client.get_balance(wallet_address)
    print(f"Wallet Balance: {balance['result']['value']} lamports")
    return balance
