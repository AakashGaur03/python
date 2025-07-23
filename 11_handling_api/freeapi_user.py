# Step-by-step:
# Create a virtual environment:

# python3 -m venv venv
# Activate the virtual environment:

# source venv/bin/activate
# You’ll see (venv) in your terminal, indicating it's active.

# Now install requests:

# pip install requests



import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response  = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        # print(response)
        # print(data)
        user_data = data["data"]
        # print(user_data)
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username,country
    else:
        # raise is used to raise Errors
        raise Exception("Failed to fetch User Data")
    
def main():
    try:
        username,country = fetch_random_user()
        print(f"Username :{username} \nCountry:{country}")
    except Exception as e:
        print((str(e)))
        

if __name__ == "__main__":
    main()