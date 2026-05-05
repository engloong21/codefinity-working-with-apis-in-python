import requests

def print_three_cat_facts():
    # Your code goes here
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    fact = data ["fact"]
    print(fact)

for _ in range(3):
    # request → json → extract → print
    print_three_cat_facts()
