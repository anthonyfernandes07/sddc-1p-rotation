from dotenv import load_dotenv
import requests
import os
import sys

load_dotenv("testcreds.env")
# Environment variables for security

OP_API_TOKEN = os.getenv("OP_API_TOKEN")
if not OP_API_TOKEN:
    print("Error: 1Password API token is missing. Set OP_API_TOKEN.")
    sys.exit(1)  # Exit the script with an error code

VAULT_ID = os.getenv("VAULT_ID")

# 1Password API base URL
op_headers = {"Authorization": f"Bearer {OP_API_TOKEN}", "Content-Type": "application/json"}
op_items_url = f"http://localhost:8080/v1/vaults/{VAULT_ID}/items"

# Get existing 1Password credentials
op_response = requests.get(op_items_url, headers=op_headers, verify=True)
print (op_response)
op_items = op_response.json()

print(f"Fetched {len(op_items)} items from 1Password vault {VAULT_ID}.")
# Print the titles of the fetched items
for item in op_items:
    print(f"Item title: {item['title']}")
# Example of how to process each item
for item in op_items:
    title = item['title']
    print(f"Processing item: {title}")
