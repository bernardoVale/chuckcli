import requests


def get_quote():
    response = requests.get('https://api.chucknorris.io/jokes/random')

    if response.status_code == 200:
        return response.json()['value']

    return None


def main():
    quote = get_quote()
    if quote is not None:
        print(quote)
    else:
        print("Can't collect checknorris quotes")
        exit(1)
