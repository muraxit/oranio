import random
import time
import json
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from spl_token import Token, TOKEN_PROGRAM_ID

# Solana Client einrichten
client = Client("https://api.mainnet-beta.solana.com")

# Erstelle ein neues Wallet (Keypair) für den Agenten
agent_keypair = Keypair.generate()
agent_public_key = agent_keypair.public_key

# Beispielhafte Token-Daten
token_data = {
    "name": "Oranio Token",
    "symbol": "ORAI",
    "value": 1000,  # Startwert des Tokens
    "decimals": 9
}

# Funktion zur Optimierung von Token-Werten (AI-Modell)
def ai_optimize_token(token_data):
    """Optimiert den Token-Wert basierend auf KI-Algorithmen"""
    optimized_value = token_data["value"] * random.uniform(1.05, 1.15)  # Erhöht den Wert um 5-15%
    token_data["optimized_value"] = optimized_value
    return token_data

# Funktion zur Erstellung eines neuen Tokens
def create_token():
    """Erstellt ein neues Token auf der Solana Blockchain"""
    token = Token.create_mint(
        client,
        agent_keypair,
        agent_public_key,
        9,  # Dezimalstellen
        TOKEN_PROGRAM_ID
    )
    token_account = token.create_account(agent_public_key)
    print(f"Token erstellt: {token.public_key}")
    return token, token_account

# Funktion zur Durchführung einer Token-Übertragung
def transfer_token(amount, receiver_public_key):
    """Überträgt Token von Agent zu einem Empfänger"""
    token = Token(client, "YourTokenAddressHere", TOKEN_PROGRAM_ID, agent_keypair)
    sender_token_account = token.get_associated_token_address(agent_public_key)
    receiver_token_account = token.get_associated_token_address(receiver_public_key)

    transaction = transfer(
        TransferParams(
            from_pubkey=sender_token_account,
            to_pubkey=receiver_token_account,
            lamports=amount
        )
    )
    response = client.send_transaction(transaction, agent_keypair)
    print(f"Übertragung abgeschlossen: {response}")
    return response

# Funktion zur Durchführung des gesamten Experiments
def run_experiment():
    """Führt das gesamte Experiment durch (Token-Erstellung, AI-Optimierung und Übertragung)"""
    print("Experiment startet...")

    # 1. Token erstellen
    token, token_account = create_token()

    # 2. Token optimieren
    optimized_token = ai_optimize_token(token_data)
    print(f"Optimierte Token-Daten: {optimized_token}")

    # 3. Übertragung von Token (z. B. 1000 Einheiten)
    receiver_public_key = "ReceiverWalletPublicKeyHere"
    transfer_token(1000, receiver_public_key)

    # 4. Speichern der optimierten Ergebnisse
    with open("experiment_results.json", "w") as f:
        json.dump(optimized_token, f)
    
    print("Experiment abgeschlossen!")

# Hauptschleife des Agenten
def agent_loop():
    """Der Agent führt regelmäßig Experimente durch"""
    while True:
        print("Agent startet neues Experiment...")
        run_experiment()
        # Warte 10 Minuten, bevor das nächste Experiment gestartet wird
        time.sleep(600)

if __name__ == "__main__":
    agent_loop()
