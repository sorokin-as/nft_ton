from pytonlib import TonlibClient
import requests
from pathlib import Path
import asyncio
from wallet_creation import wallet, wallet_address
#from tonsdk import to_nano


async def get_seqno(client:TonlibClient,address:str):
    data = await client.raw_run_method(method='seqno', stack_data=[], address=address)
    print(data)
    return int( data['stack'][0][1], 16)


# async def send_tokens():
#     try:
#         url = 'https://ton.org/testnet-global.config.json'
#         config = requests.get(url).json()

#         # create keystore directory for tonlib
#         # kQA7xuBEAyCkOotI0A_f4NIXTTPK5H-n3i7knhQ5MMKU-iYP
#         keystore_dir = '/tmp/ton_keystore'
#         Path(keystore_dir).mkdir(parents=True, exist_ok=True)
        
#         client = TonlibClient(ls_index=4, config=config, keystore=keystore_dir, tonlib_timeout=300)

#         await client.init()

#         #query = wallet.create_init_external_message()
#         #print(query['message'].to_boc(False))
#         #deploy_message = query['message'].to_boc(False)


#         seqno = await get_seqno(client, wallet_address)
#         print("Seqno:", seqno)
        
#         # wallet.create_transfer_message(to_addr='kf8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIue', 
#         #                                amount=to_nano(0.01, 'ton'), seqno=1)

#     except Exception as e:
#         print("!!!!!!!!!!!!!!!!--------Ошибка:", e)



async def send_tokens():
    try:
        url = 'https://ton.org/testnet-global.config.json'
        config = requests.get(url).json()

        # create keystore directory for tonlib
        keystore_dir = '/tmp/ton_keystore'
        Path(keystore_dir).mkdir(parents=True, exist_ok=True)
        
        client = TonlibClient(ls_index=4, config=config, keystore=keystore_dir, tonlib_timeout=300)

        print("Инициализация клиента...")
        await client.init()
        print("Клиент инициализирован.")

        # Пример длительной операции
        print("Получение seqno...")
        seqno = await get_seqno(client, wallet_address)
        print("Seqno:", seqno)

        # Пример отправки сообщения


    except Exception as e:
        print("!!!!!!!!!!!!!!!!--------Ошибка:", e)


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
    #asyncio.run(main())
    asyncio.run(send_tokens())
    #asyncio.get_event_loop().run_until_complete(send_tokens())