# nft_ton

python3 -m venv .venv_nftton

source .venv_nftton/bin/activate

pip freeze > requirements.txt
pip install -r requirements.txt




Для активации коцелька его адрес надо передать сюда @testgiver_ton_bot
придет 2 тона
Адрес кошелька взять тут     print(wallet.address.to_string(True, True, True, True))