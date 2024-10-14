from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
import json

# Connect to Solana mainnet
client = Client("https://api.mainnet-beta.solana.com")

# Load sender's keypair
with open('../account1.json', 'r') as f:
    priv_key = json.load(f)
    sender = Keypair.from_private_key(priv_key)

# Specify recipient's public key and amount to transfer (0.01 SOL)
receiver = PublicKey("xjtCtLnxnAFUFAwLFvr4zery2JSbyWhGy4SZeDUeDXt")
amount = 0.01 * 1e9  # Convert SOL to lamports

# Create transfer transaction
instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver,
    lamports=int(amount)
)
transaction = Transaction(instructions=[instruction], signers=[sender])

# Send the transaction
result = client.send_transaction(transaction)
print("Transaction signature:", result)