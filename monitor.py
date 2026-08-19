import csv
import urllib.request

def check_vault():
    print("Checking Apex Grant Vault links...")
    broken_links = []
    
    try:
        with open('full-vault.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Program Name']
                url = row['Application URL']
                
                try:
                    req = urllib.request.Request(
                        url, 
                        headers={'User-Agent': 'Mozilla/5.0'}
                    )
                    with urllib.request.urlopen(req, timeout=10) as response:
                        if response.status == 200:
                            print(f"[ACTIVE] {name}")
                        else:
                            print(f"[WARNING: {response.status}] {name}")
                except Exception as e:
                    print(f"[BROKEN/DEAD] {name} ({url}) -> Error: {e}")
                    broken_links.append(name)
                    
        print(f"\nScan complete. Found {len(broken_links)} potential dead links.")
    except Exception as err:
        print(f"Error reading CSV: {err}")

if __name__ == "__main__":
    check_vault()
