import requests

def print_three_cat_facts():
    # Your code goes here
    response_1 = requests.get('https://catfact.ninja/fact')
    data_1 = response_1.json()
    fact_1 = data_1.get('fact','There is no fact')
    response_2 = requests.get('https://catfact.ninja/fact')
    data_2 = response_2.json()    
    fact_2 = data_2.get('fact','There is no fact')
    response_3 = requests.get('https://catfact.ninja/fact')
    data_3 = response_3.json()    
    fact_3 = data_3.get('fact','There is no fact')
    print(fact_1)
    print(fact_2)
    print(fact_3)

    
print_three_cat_facts()
