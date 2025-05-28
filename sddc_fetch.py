from dotenv import load_dotenv
import requests
import os
import sys

load_dotenv("testcreds.env")
# Environment variables for security
SDDC_URL = "https://REDACTED_SDDC_HOST/"
SDDC_USERNAME = os.getenv("SDDC_USERNAME")
SDDC_PASSWORD = os.getenv("SDDC_PASSWORD")

if not SDDC_USERNAME or not SDDC_PASSWORD:
    print("Error: SDDC credentials are missing. Set SDDC_USERNAME and SDDC_PASSWORD.")
    sys.exit(1)  # Exit the script with an error code

OP_API_TOKEN = os.getenv("OP_API_TOKEN")
VAULT_ID = "REDACTED_VAULT_ID"

# Authentication with SDDC Manager
auth_response = requests.post(
    f"{SDDC_URL}/v1/tokens",
    json={"username": SDDC_USERNAME, "password": SDDC_PASSWORD},
    verify=False  # Use certificate validation in production
)
print(auth_response)
auth_token = auth_response.json().get("accessToken")
print(f"Authenticated with SDDC Manager. Token: {auth_token}")

# Fetch credentials from SDDC Manager
headers = {"Authorization": f"Bearer {auth_token}"}
params = {"resourceType": "VRA"}
creds_response = requests.get(f"{SDDC_URL}/v1/credentials", headers=headers, verify=False)
credentials = creds_response.json()

# Authenticate with 1Password
op_headers = {"Authorization": f"Bearer {OP_API_TOKEN}", "Content-Type": "application/json"}
op_items_url = f"https://connect.1password.com/v1/vaults/{VAULT_ID}/items"

# Get existing 1Password credentials
op_response = requests.get(op_items_url, headers=op_headers, params=params, verify=True)
op_items = op_response.json()

# Compare and update only if changed
for cred in credentials:
    title = f"SDDC - {cred['name']}"
    existing_item = next((item for item in op_items if item['title'] == title), None)

    if existing_item:
        # Check if password has changed
        current_password = next(field['value'] for field in existing_item['fields'] if field['label'] == "Password")
        if current_password != cred['password']:
            print(f"Updating password for {title} in 1Password...")
            update_payload = {
                "fields": [
                    {"label": "Username", "value": cred["username"], "type": "STRING"},
                    {"label": "Password", "value": cred["password"], "type": "CONCEALED"}
                ]
            }
            requests.put(f"{op_items_url}/{existing_item['id']}", headers=op_headers, json=update_payload, verify=True)
    else:
        print(f"Creating new entry for {title} in 1Password...")
        new_payload = {
            "title": title,
            "category": "LOGIN",
            "fields": [
                {"label": "Username", "value": cred["username"], "type": "STRING"},
                {"label": "Password", "value": cred["password"], "type": "CONCEALED"}
            ]
        }
        requests.post(op_items_url, headers=op_headers, json=new_payload, verify=True)

print("Password synchronization completed.")
