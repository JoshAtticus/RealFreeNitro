import requests

def make_request(user_id):
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {"Content-Type": "application/json"}
    payload = {"partnerUserId": user_id}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        token_data = response.json().get('token')
        print("Nitro Code generated!")
        return token_data
    else:
        print(f"Error: Received status code {response.status_code}. Nitro Code was not generated.")
        return None

num_codes = int(input("How many codes do you want to make? (Note that generating large amounts will get you ratelimited!) "))
user_id = input("What is your user ID? (If you don't have one, there's one on the GitHub Page) ")
base_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"
full_urls = []

for i in range(num_codes):
    token = make_request(user_id)
    if token:
        full_url = base_url + token
        full_urls.append(full_url)

with open('nitrolinks.txt', 'a') as file:
    for full_url in full_urls:
        file.write(full_url + '\n')

print(f"Finished making {num_codes} codes. Data saved to nitrolinks.txt.")