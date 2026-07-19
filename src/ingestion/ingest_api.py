## Connect to FakeStoreAPI
import requests
import yaml
from src.util.config_load import load_filepath

# Access YAML file for required configurations
yaml_config = load_filepath()

with open(yaml_config) as file:
    config = yaml.safe_load(file)

api_link = config['api']['fsa_products']

response_API = requests.get(api_link)
print(response_API.json())