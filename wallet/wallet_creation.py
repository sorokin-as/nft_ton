from tonsdk.contract.wallet import Wallets, WalletVersionEnum



#mnemonics, pub_k, priv_k, wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)

mnemonics =  ['garlic', 'deal', 'hood', 'rocket', 'essay', 'noble', 'during', 'error', 'day', 'smart', 'unlock', 'juice', 'girl', 'silk', 'nominee', 'among', 'false', 'novel', 'position', 'differ', 'into', 'payment', 'lion', 'hip']


mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)




if __name__ == '__main__':
    print(mnemonics)
    print(wallet.address.to_string(True, True, True, True))