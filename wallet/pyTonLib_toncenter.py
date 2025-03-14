from pytonlib import TonlibClient
import requests
from pathlib import Path
import asyncio
from wallet_creation import wallet




async def main():
    url = 'https://ton.org/testnet-global.config.json'
    config = requests.get(url).json()

    # create keystore directory for tonlib
    # kQA7xuBEAyCkOotI0A_f4NIXTTPK5H-n3i7knhQ5MMKU-iYP
    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)
    
    client = TonlibClient(ls_index=0, config=config, keystore=keystore_dir)
    print(wallet.address.to_string(True, True, True, True))

    await client.init()

    query = wallet.create_init_external_message()
    #print(query['message'].to_boc(False))
    deploy_message = query['message'].to_boc(False)
    await client.raw_send_message(deploy_message)



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())