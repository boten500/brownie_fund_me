from brownie import config, network, accounts, MockV3Aggregator
from web3 import Web3


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev1~~"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache1-local"]
DECIMALS = 80
START_PRICE = 2000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENTS: 
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])






        