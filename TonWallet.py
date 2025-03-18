import uuid
from mnemonic import Mnemonic

class CryptoWallet:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.wallet_address = self.generate_wallet_address()
        self.mnemonic_phrase = self.generate_mnemonic_phrase()

    def generate_wallet_address(self):
        # Генерация уникального адреса кошелька
        return str(uuid.uuid4())

    def generate_mnemonic_phrase(self):
        # Генерация мнемонической фразы из 12 слов
        mnemo = Mnemonic("english")
        return mnemo.generate(strength=128)  # 128 бит = 12 слов

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

# Пример использования
if __name__ == "__main__":
    # Создаем кошелек для пользователя "Alice" с начальным балансом 100
    alice_wallet = CryptoWallet("Alice", 100)

    # Выводим информацию о кошельке
    print(alice_wallet.get_wallet_info())

    # Депозит на кошелек
    alice_wallet.deposit(50)

    # Снятие с кошелька
    alice_wallet.withdraw(30)

    # Выводим обновленную информацию о кошельке
    print(alice_wallet.get_wallet_info())