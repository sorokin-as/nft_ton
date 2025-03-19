from TonWallet import CryptoTonWallet




def startWallet():
    while True:
        user_input = input("Введите сообщение (или 0 для выхода): ")
        
        if user_input == "0":
            print("Выход из цикла.")
            break
        
        print(f"Вы ввели: {user_input}")




if __name__ == "__main__":
    FirstWallet =  CryptoTonWallet()
    #startWallet()