from invoice import BUYER, INVOICE_LINES, COMPANY_ID
from utils import fetch_document_xml, get_auth_header
import requests

# Basic invoice structure
payload = {
    "recipient": BUYER["peppolAddress"],
    "documentType": "invoice",
    "document": {
        "invoiceNumber": "INV-001",
        "buyer": BUYER,
        "paymentMeans": [{
            "iban": "BE1234567890"
        }],
        "lines": INVOICE_LINES
    }
}

# Send request
response = requests.post(
    f"https://peppol.recommand.eu/api/peppol/{COMPANY_ID}/sendDocument",
    headers={"Authorization": f"Basic {get_auth_header()}", "Content-Type": "application/json"},
    json=payload
)

if response.status_code == 200:
    result = response.json()
    print(f"✅ Invoice sent! ID: {result.get('id')}")
    fetch_document_xml(result.get('id'))
else:
    print(f"❌ Error: {response.text}")