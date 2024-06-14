import requests
import json
import config

# Construct URL for placing orders
order_base_url = f"{config.API_BASE_URL}accounts/"

# Set headers with access token
headers = {
    'Authorization': f'Bearer {config.ACCESS_TOKEN}',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Function to place market order for a specific account ID
def place_market_order(account_id):
    order_url = f"{order_base_url}{account_id}/orders"
    response = requests.post(order_url,
data={'class': 'equity', 'symbol': 'trnr', 'side': 'buy', 'quantity': '1', 'type': 'market', 'duration': 'day'},
        headers=headers
    )
    if response.status_code == 200:
        print(f"Market order placed successfully for account ID {account_id}!")
        order_info = response.json()
        print("Order details:", order_info)
    else:
        print(f"Failed to place market order for account ID {account_id}. Status code: {response.status_code}")
        print("Error message:", response.text)

# Function to retrieve all account IDs from the user's profile
def get_account_ids():
    response = requests.get(config.profile_url, headers=headers)
    account_ids = []
    if response.status_code == 200:
        user_profile = json.loads(response.text)
        account_ids = [account['account_number'] for account in user_profile['profile']['account']]
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return account_ids

# Retrieve all account IDs
account_ids = get_account_ids()

# Place market order for each account ID
for account_id in account_ids:
    place_market_order(account_id)
