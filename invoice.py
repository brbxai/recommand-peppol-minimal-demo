# Recommand configuration
API_KEY = "key_01K4TPA9EA1C2PG7SPHFCEZD1J"
API_SECRET = "secret_6fb0e1f6844a4d4d861dc23662f21cad"
TEAM_ID = "team_01K4TPA3VYABGQVRHK9CR2ZH0N"

COMPANY_ID = "c_01K4TPB98ZJBR9GX4173VCVS88" # Sender is 0208:1012081766

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