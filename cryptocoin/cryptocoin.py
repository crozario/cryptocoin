import json
from urllib.request import urlopen

coin_list = {}

def get_coin_list():
	global coin_list
	base_list_url = "https://www.cryptocompare.com/api/data/coinlist/"

	if coin_list:
		return coin_list

	list_request = urlopen(base_list_url)
	load_list = json.loads(list_request.read())
	if load_list["Response"] == "Success":
		data = load_list["Data"]
		for value in data.values():
			name = value["Name"]
			coin_name = value["CoinName"]
			coin_list.update({name : coin_name})
		return coin_list


def print_coin_list():
	global coin_list

	if not coin_list:
		coin_list = get_coin_list()

	print("Symbol - Name")
	for key, value in coin_list.items():
		print(key, "-", value)

def is_coin_in_list(name):
	global coin_list

	name = name.upper()
	if name in coin_list.keys():
		return True

	for value in coin_list.values():
		name = name.lower()
		value = value.lower()
		if name == value:
			return True

	return False

def get_coin_price(name, rate="USD"):
	global coin_list

	base_price_url = "https://min-api.cryptocompare.com/data/price?"

	if not coin_list:
		coin_list = get_coin_list()

	if is_coin_in_list(name):
		fsym = name
		tsyms = rate
		price_url = base_price_url + "fsym=" + fsym + "&tsyms=" + rate
		price_request = urlopen(price_url)
		price = json.loads(price_request.read())
		return price[rate]

	else:
		return None



	



