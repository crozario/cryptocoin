import json
from urllib.request import urlopen


def get_coin_list():
	coin_list = {}
	base_list_url = "https://www.cryptocompare.com/api/data/coinlist/"
	list_request = urlopen(base_list_url)
	load_list = json.loads(list_request.read())
	data = load_list["Data"]
	for value in data.values():
		name = value["Name"]
		coin_name = value["CoinName"]
		coin_list.update({name : coin_name})
	return coin_list


def print_coin_list():
	coin_list = get_coin_list()
	print("Symbol - Name")
	for key, value in coin_list.items():
		print(key, "-", value)

def is_coin_in_list(name):
	coin_list = get_coin_list()

	name = name.upper()
	if name in coin_list.keys():
		return True
	else:
		return False

def get_coin_price(coin_name="BTC", rate="USD"):

	base_price_url = "https://min-api.cryptocompare.com/data/price?"
	base_multiprice_url = "https://min-api.cryptocompare.com/data/pricemulti?"

	if type(coin_name) is str:
		fsym = coin_name.upper()
		if type(rate) is str:	
			tsym = rate.upper()
			price_url = base_price_url + "fsym=" + fsym + "&tsyms=" + tsym
			price_request = urlopen(price_url)
			price = json.loads(price_request.read())
			return price[tsym]
		elif type(rate) is list:
			price_url = base_price_url + "fsym=" + fsym + "&tsyms="
			for tsym in rate:
				price_url = price_url + tsym.upper() + ','
			price_url = price_url[:-1]
			price_request = urlopen(price_url)
			prices = json.loads(price_request.read())
			return prices
		else:
			return None

	elif type(coin_name) is list:
		if type(rate) is str:
			tsym = rate.upper()
			price_url = base_multiprice_url + "fsyms=" 
			for fsym in coin_name:
				price_url = price_url + fsym.upper() + ','
			price_url = price_url[:-1]
			price_url = price_url + "&tsyms=" + tsym
			price_request = urlopen(price_url)
			prices = json.loads(price_request.read())
			return prices
		elif type(rate) is list:
			price_url = base_multiprice_url + "fsyms=" 
			for fsym in coin_name:
				price_url = price_url + fsym.upper() + ','
			price_url = price_url[:-1]
			price_url += "&tsyms=" 
			for tsym in rate:
				price_url = price_url + tsym.upper() + ','
			price_url = price_url[:-1]	
			price_request = urlopen(price_url)
			prices = json.loads(price_request.read())
			return prices
		else:
			return None

	else:
		return None

def get_full_coin_prices(coin_name="BTC", rate="USD"):
	base_fullmultiprice_url = "https://min-api.cryptocompare.com/data/pricemultifull?"

	if type(coin_name) is str:
		fsym = coin_name.upper()
		if type(rate) is str:	
			tsym = rate.upper()
			price_url = base_fullmultiprice_url + "fsyms=" + fsym + "&tsyms=" + tsym
			price_request = urlopen(price_url)
			info = json.loads(price_request.read())
			return info["RAW"][fsym][tsym]
		elif type(rate) is list:
			price_url = base_fullmultiprice_url + "fsyms=" + fsym + "&tsyms=" 
			for tsym in rate:
				price_url = price_url + tsym.upper() + ','
			price_url = price_url[:-1]
			price_request = urlopen(price_url)
			info = json.loads(price_request.read())
			return info["RAW"][fsym]
		else:
			return None

	elif type(coin_name) is list:
		if type(rate) is str:
			tsym = rate.upper()
			price_url = base_fullmultiprice_url + "fsyms=" 
			for fsym in coin_name:
				price_url = price_url + fsym.upper() + ','
			price_url = price_url[:-1]
			price_url = price_url + "&tsyms=" + tsym
			price_request = urlopen(price_url)
			info = json.loads(price_request.read())
			return info["RAW"]

		elif type(rate) is list:
			price_url = base_fullmultiprice_url + "fsyms=" 
			for fsym in coin_name:
				price_url = price_url + fsym.upper() + ','
			price_url = price_url[:-1]
			price_url += "&tsyms=" 
			for tsym in rate:
				price_url = price_url + tsym.upper() + ','
			price_url = price_url[:-1]	
			price_request = urlopen(price_url)
			info = json.loads(price_request.read())
			return info["RAW"]
		else:
			return None

	else:
		return None




	



