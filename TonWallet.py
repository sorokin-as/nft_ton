from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from dotenv import load_dotenv, dotenv_values, set_key
import os

load_dotenv()

class CryptoTonWallet:
    def __init__(self, myWalletAdress=None):
        if myWalletAdress: 
            self.wallet_address = self.load_wallet_from_mnemonics(myWalletAdress)
        else:
            self.wallet_address = self.create_wallet()
        #self.owner_name = owner_name
        #self.balance = initial_balance
        #self.wallet_address = self.generate_wallet_address()
        #self.mnemonic_phrase = self.generate_mnemonic_phrase()
        print('INIT CryptoTonWallet')


    def create_wallet(self):
        # Создаем кошелек
        mnemonics, pub_k, priv_k, wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
        wallet_address = wallet.address.to_string(True, True, True, True)

        # Сохраняем параметры в .env файл
        env_file = f"{wallet_address}.env"
        
        # Если файл .env существует, загружаем его текущие значения
        if os.path.exists(env_file):
            config = dotenv_values(env_file)
        else:
            config = {}

        # Убедимся, что все значения являются строками
        config["WALLET_ADDRESS"] = str(wallet_address)  # Преобразуем в строку, если это не строка
        config["MNEMONICS"] = " ".join(map(str, mnemonics))  # Преобразуем мнемоники в строку
        config["PUBLIC_KEY"] = str(pub_k)  # Преобразуем в строку, если это не строка
        config["PRIVATE_KEY"] = str(priv_k)  # Преобразуем в строку, если это не строка


        # Записываем обновленные значения в .env файл
        for key, value in config.items():
            set_key(env_file, key, value)

        print(f"Создан новый кошелек. Данные сохранены в {wallet_address}")
        return wallet_address


    def load_wallet_from_mnemonics(self):
        mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)
        wallet_address = wallet.address.to_string(True, True, True, True)
        print("Кошелек успешно загружен:", wallet_address)
        return wallet_address

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит на {amount} успешно выполнен. Новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть больше нуля.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снятие {amount} успешно выполнено. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств или сумма снятия некорректна.")

    def get_balance(self):
        return self.balance

    def get_wallet_info(self):
        return {
            "owner_name": self.owner_name,
            "wallet_address": self.wallet_address,
            "balance": self.balance,
            "mnemonic_phrase": self.mnemonic_phrase
        }

# # Пример использования
# if __name__ == "__main__":
#     # Создаем кошелек для пользователя "Alice" с начальным балансом 100
#     alice_wallet = CryptoWallet("Alice", 100)

#     # Выводим информацию о кошельке
#     print(alice_wallet.get_wallet_info())

#     # Депозит на кошелек
#     alice_wallet.deposit(50)

#     # Снятие с кошелька
#     alice_wallet.withdraw(30)

#     # Выводим обновленную информацию о кошельке
#     print(alice_wallet.get_wallet_info())