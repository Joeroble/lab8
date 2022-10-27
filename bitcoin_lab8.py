import requests


coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    bitcoin = 123
    current_price = get_bitcoin_current_price()
    converted_price = get_bitcoin_value_in_dollars(bitcoin, current_price)
    print(f'{bitcoin} Bitcoin is equivalent to ${converted_price}')


def get_bitcoin_current_price():
    response = requests.get(coindesk_url)
    bitcoin_data = response.json()
    return bitcoin_data


def get_bitcoin_value_in_dollars(bitcoin, bitcoin_data):
    dollars_exchange_rate = bitcoin_data['bpi']['USD']['rate_float']
    bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate
    return bitcoin_value_in_dollars


if __name__ == '__main__':
    main()