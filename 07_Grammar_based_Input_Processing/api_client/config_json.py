import json

# load configuration from JSON file atau deserilize JSON string
def get_base_url():
    with open("config.json", "r") as f:
        config = json.load(f) 
        base_url = config["base_url"]
    return base_url

