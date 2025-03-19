from TonWallet import CryptoTonWallet

FirstWallet =  CryptoTonWallet

while True:
    user_input = input("Введите сообщение (или 0 для выхода): ")
    
    if user_input == "0":
        print("Выход из цикла.")
        break
    
    print(f"Вы ввели: {user_input}")а