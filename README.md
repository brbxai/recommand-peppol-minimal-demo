# PEPPOL Invoice Demo

A simple Python demo for sending electronic invoices via the PEPPOL network using the Recommand API.

Learn more at [recommand.eu](https://recommand.eu).

## Overview

This project demonstrates how to:
- Create and send PEPPOL-compliant invoices
- Authenticate with the Recommand API
- Fetch generated XML documents

## Files

- `invoice.py` - Configuration file containing API credentials, buyer information, and invoice line items
- `send_invoice.py` - Main script that sends the invoice via the Recommand API
- `utils.py` - Utility functions for authentication and document retrieval
- `invoice.xml` - Generated XML output (created after running the demo)

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure your API credentials in `invoice.py`:
   - Update `API_KEY`, `API_SECRET`, and `TEAM_ID` with your Recommand credentials
   - Modify `COMPANY_ID` with your company identifier
   - Update buyer information and invoice line items as needed

## Usage

Run the demo:
```bash
uv run send_invoice.py
```

The script will:
1. Send the invoice to the specified PEPPOL address
2. Print the invoice ID if successful
3. Fetch and save the generated XML document to `invoice.xml`
