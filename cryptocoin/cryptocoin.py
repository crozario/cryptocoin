import json
from urllib.request import urlopen

def get_coin_list():
	base_list_url = "https://www.cryptocompare.com/api/data/coinlist/"
	coin_list = urlopen(base_list_url)
	coin_list = json.loads(coin_list.read())
	if coin_list["Response"] == "Success":
		data = coin_list["Data"]
		data_dict = {}
		for value in data.values():
			name = value["Name"]
			coin_name = value["CoinName"]
			data_dict.update({name : coin_name})
		return data_dict


def print_coin_list():
	coin_list = get_coin_list()
	print("Symbol - Name")
	for key, value in coin_list.items():
		print(key, "-", value)


def get_coin():
	base_price_url = "https://min-api.cryptocompare.com/data/"
	pass



