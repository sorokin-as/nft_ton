from pytonlib import TonlibClient
import requests



async def main():
    url = 'https://ton.org/testnet-global.config.json'
    client = TonlibClient(ls_index=0)

