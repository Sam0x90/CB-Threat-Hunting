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
parser.add_argument("--no-verify-tls", action='store_true', help="Disable TLS certificate verification")

# Parse arguments
args = parser.parse_args()

# Prepare the variables
watchlist_dir = args.folder
api_key = args.apikey
cb_response_url = args.url
verify_tls = not args.no_verify_tls
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
                    'description': '{}\nReferences: {}\nTags: {}'.format(
                        watchlist_data.get('description', ''),
                        watchlist_data.get('references', ''),
                        watchlist_data.get('tags', '')
                    )
                }

                # POST request to create the watchlist
                response1 = requests.post(api_endpoint, headers=headers, data=json.dumps(data), verify=verify_tls)

                # Check the response
                if response1.status_code == 200:
                    print(f"Watchlist '{watchlist_data['name']}' created successfully")
                    # Add action trigger based on the "on_hit" field [email , syslog, alert]
                    on_hit=watchlist_data.get('on_hit', '').split(',')
                    if on_hit:
                        # Get the ID of the watchlist to update with action trigger
                        watchList_id = response1.json()['id']
                        for action in on_hit:
                            # Prepare the API endpoint with watchlist ID and action_type
                            action_url = '{0}/{1}/action_type/{2}'.format(api_endpoint,watchList_id,action.strip())
                            action_payload = json.dumps({"enabled": True})

                            # PUT request to update the watchlist action trigger
                            response2 = requests.put(url=action_url, headers=headers, data=action_payload, verify=False)
                            if response1.status_code == 200:
                                print(f"Watchlist '{watchList_id}' updated successfully")
                            else:
                                print(f"Failed to update action trigger for watchlist ID: '{watchList_id}' with response code: {response1.status_code}")
                                print(response1.text)

                else:
                    print(f"Failed to create watchlist '{watchlist_data['name']}': {response1.status_code}")
                    print(response1.text)

            except yaml.YAMLError as exc:
                print(f"Error parsing YAML file {filename}: {exc}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

print("Processing complete.")
