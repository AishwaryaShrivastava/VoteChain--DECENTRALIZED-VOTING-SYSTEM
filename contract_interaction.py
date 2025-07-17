from web3_config import load_contract
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Use admin address and private key from .env file
admin_address = Web3.to_checksum_address(os.getenv("ADMIN_ADDRESS"))
admin_private_key = os.getenv("ADMIN_PRIVATE_KEY")

# Load web3 connection and contract instance
web3, contract = load_contract()

def start_election(election_name):
    nonce = web3.eth.get_transaction_count(admin_address)
    txn = contract.functions.startElection(election_name).build_transaction({
        "from": admin_address,
        "nonce": nonce,
        "gas": 3000000,
        "gasPrice": web3.to_wei("20", "gwei")
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=admin_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def end_election():
    nonce = web3.eth.get_transaction_count(admin_address)
    txn = contract.functions.endElection().build_transaction({
        "from": admin_address,
        "nonce": nonce,
        "gas": 2000000,
        "gasPrice": web3.to_wei("20", "gwei")
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=admin_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def add_candidate(candidate_name):
    nonce = web3.eth.get_transaction_count(admin_address)
    txn = contract.functions.addCandidate(candidate_name).build_transaction({
        "from": admin_address,
        "nonce": nonce,
        "gas": 2000000,
        "gasPrice": web3.to_wei("20", "gwei")
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=admin_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def register_voter(voter_address):
    nonce = web3.eth.get_transaction_count(admin_address)
    txn = contract.functions.registerVoter(voter_address).build_transaction({
        "from": admin_address,
        "nonce": nonce,
        "gas": 2000000,
        "gasPrice": web3.to_wei("20", "gwei")
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=admin_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def vote(candidate_id, voter_address, voter_private_key):
    nonce = web3.eth.get_transaction_count(voter_address)
    txn = contract.functions.vote(candidate_id).build_transaction({
        "from": voter_address,
        "nonce": nonce,
        "gas": 2000000,
        "gasPrice": web3.to_wei("20", "gwei")
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=voter_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def get_candidate(id):
    return contract.functions.getCandidate(id).call()

def get_total_candidates():
    return contract.functions.candidatesCount().call()
