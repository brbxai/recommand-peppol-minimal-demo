# Recommand configuration
API_KEY = "key_"
API_SECRET = "secret_"
TEAM_ID = "team_"

COMPANY_ID = "c_" # Sender is 0208:1012081766

# Information about the customer
BUYER = {
    "name": "LRM NV",
    "street": "Corda Campus - Corda 1",
    "city": "Hasselt", 
    "postalZone": "3500",
    "country": "BE",
    "vatNumber": "BE0452138972",
    "peppolAddress": "0208:0452138972",
}

# Our invoice lines
INVOICE_LINES = [
    {
        "name": "LED schermen",
        "quantity": "325",
        "netPriceAmount": "635.00",
        "vat": {
            "percentage": "21.00"
        }
    },
    {
        "name": "WiFi access points",
        "quantity": "15",
        "netPriceAmount": "325.30",
        "vat": {
            "percentage": "21.00"
        }
    }
]