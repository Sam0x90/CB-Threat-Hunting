import requests
import json
import yaml
import os
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(description="Create watchlists in Carbon Black from YAML files")
parser.add_argument("--folder", required=True, help="Path to the folder containing YAML watchlist files")
parser.add_argument("--apikey", required=True, help="API key for Carbon Black Response")
parser.add_argument("--url", required=True, help="URL of the Carbon Black Response server")

# Parse arguments
args = parser.parse_args()

# Prepare the variables
watchlist_dir = args.folder
api_key = args.apikey
cb_response_url = args.url
api_endpoint = f'{cb_response_url}/api/v1/watchlist'

# Headers for API Request
headers = {
    'X-Auth-Token': api_key,
    'Content-Type': 'application/json'
}

# Iterate over each YAML file in the directory
for filename in os.listdir(watchlist_dir):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        with open(os.path.join(watchlist_dir, filename), 'r') as file:
            try:
                # Parse YAML file
                watchlist_data = yaml.safe_load(file)

                # Prepare the data for API request
                data = {
                    'name': watchlist_data['name'],
                    'search_query': watchlist_data['search_query'],
                    'index_type': watchlist_data['index_type'],
                    'description': '{}\nReferences: {}\nTags: {}\nOn Hit: {}'.format(
                        watchlist_data.get('description', ''),
                        watchlist_data.get('references', ''),
                        watchlist_data.get('tags', ''),
                        watchlist_data.get('on_hit', '')
                    )
                }

                # POST request to create the watchlist
                response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

                # Check the response
                if response.status_code == 200:
                    print(f"Watchlist '{watchlist_data['name']}' created successfully")
                else:
                    print(f"Failed to create watchlist '{watchlist_data['name']}': {response.status_code}")
                    print(response.text)

            except yaml.YAMLError as exc:
                print(f"Error parsing YAML file {filename}: {exc}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

print("Processing complete.")
