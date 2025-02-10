from src.token_creation import create_solana_token

def main():
    # Insert your Solana wallet address
    wallet_address = "YOUR_SOLANA_WALLET"
    token_name = "OranioToken"
    symbol = "OTK"

    print(f"Creating token {token_name} with symbol {symbol}")
    create_solana_token(wallet_address, token_name, symbol)

if __name__ == "__main__":
    main()
