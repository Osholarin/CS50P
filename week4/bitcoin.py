import sys
import requests

def main():
    try:
        no_bitcoin = float(sys.argv[1])
    except (ValueError, IndexError):
        print("Missing command-line arguement")
        sys.exit()
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()

        recieved_data = response.json()
        usd_price = float(recieved_data["bpi"]["USD"]["rate_float"])
        total_cost = no_bitcoin * usd_price

        formatted_price = f"{total_cost:,.4f}"
        print(f"USD ${formatted_price}")
        
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin Price {e}")
    except KeyError:
        print("Error: Unexpected data format from API")

if __name__ == "__main__":
    main()