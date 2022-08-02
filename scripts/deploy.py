from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3



def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        Mock_aggregator = MockV3Aggregator.deploy(8, 200000000000, {"from":get_account()})
        price_feed_address = Mock_aggregator.address
        print("Deployed")


    fund_me = FundMe.deploy(price_feed_address,{"from": account})
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
