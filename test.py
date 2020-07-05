import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest", params = {"access_key": "f0520f941d2c2bf56b2ae5fdc69c0cba", "symbols": "USD"})
    if res.status_code != 200:
        raise Exception("ERROR")
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()
