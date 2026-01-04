import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    # Write your code here
    try:
        response = requests.get(url)
        data = response.json()
        print(data['fact'])
    except Exception:
        print('Failed to retrieve cat fact.')

get_cat_fact()
