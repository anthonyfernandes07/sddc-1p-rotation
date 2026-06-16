# SDDC Manager to 1Password Synchronization

Automates synchronization of VMware Cloud Foundation (VCF) / SDDC Manager credentials into 1Password Connect.

## Problem

VMware Cloud Foundation (VCF) environments contain critical infrastructure credentials used across management and operational services. Maintaining these credentials manually in enterprise password managers can be time-consuming, error-prone, and difficult to audit at scale.

This project automates the synchronisation of credentials between VMware SDDC Manager and 1Password Connect. By integrating directly with both platforms through their APIs, the solution detects credential changes, creates missing entries, and updates existing records automatically, reducing operational overhead while improving security and consistency.

## Architecture

The solution integrates VMware Cloud Foundation (VCF) SDDC Manager with 1Password Connect.

To securely access vault data, 1Password Connect was deployed on a Kubernetes cluster, providing a self-hosted API endpoint for secret management. The synchronization service authenticates against both the SDDC Manager API and the 1Password Connect API, compares credential records, and updates vault entries when changes are detected.

<img width="1214" height="1295" alt="sddc man to 1pass" src="https://github.com/user-attachments/assets/17449fa4-5e45-465a-a435-4acd01b0e557" />


### Components

* VMware SDDC Manager API
* Python Synchronization Service
* Kubernetes-hosted 1Password Connect
* 1Password Vault

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
