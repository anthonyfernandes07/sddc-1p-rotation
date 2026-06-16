# SDDC Manager to 1Password Synchronization

Automates synchronization of VMware Cloud Foundation (VCF) / SDDC Manager credentials into 1Password Connect.

## Features

- Authenticates to SDDC Manager API
- Retrieves credential objects
- Compares existing 1Password entries
- Creates new entries when required
- Updates passwords when changes are detected

## Requirements

- Python 3.11+
- 1Password Connect
- VMware Cloud Foundation / SDDC Manager

## Environment Variables

SDDC_URL=
SDDC_USERNAME=
SDDC_PASSWORD=
OP_API_TOKEN=
VAULT_ID=

## Usage

python sddcto1pass.py
