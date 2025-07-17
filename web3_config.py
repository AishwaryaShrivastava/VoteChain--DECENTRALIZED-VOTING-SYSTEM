from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def load_contract():
    # Connect to local Ganache blockchain or Infura node
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Or update if using another RPC

    # Load contract address from environment variable
    contract_address = Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS"))

    # Load contract ABI from file
    with open("abi/VotingABI.json") as f:
        contract_abi = json.load(f)

    # Create contract instance
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    return web3, contract

