import requests
from base64 import b64encode
from invoice import API_KEY, API_SECRET, TEAM_ID

def get_auth_header():
    credentials = f"{API_KEY}:{API_SECRET}"
    return b64encode(credentials.encode()).decode()

def fetch_document_xml(document_id):
    # Auth header
    auth_header = get_auth_header()
    
    # Make the API request
    try:
        response = requests.get(
            f"https://peppol.recommand.eu/api/peppol/{TEAM_ID}/documents/{document_id}",
            headers={"Authorization": f"Basic {auth_header}"}
        )
                
        if response.status_code == 200:
            result = response.json()
            xml_content = result.get('document').get('xml')
            
            if xml_content:
                # Save XML to file
                with open("invoice.xml", "w", encoding="utf-8") as f:
                    f.write(xml_content)
                return True
            else:
                print("❌ No XML content found in response")
                return False
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
