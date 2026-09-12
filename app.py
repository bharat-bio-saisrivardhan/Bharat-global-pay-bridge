# Bharat-Global-Pay-Bridge - by Sai Srivardhan
# Hackathon Project - Solves Cross Border Payment Blocks

def check_transfer(country):
    blocked_countries = {
        "iran": "OFAC Sanctions - US Ban",
        "north korea": "UN Sanctions",
        "syria": "USA & EU Ban",
        "russia": "SWIFT Network Blocked",
        "belarus": "EU Sanctions"
    }

    c = country.lower().strip()
    if c in blocked_countries:
        print(f"\n{c.upper()} - PAYMENT BLOCKED!")
        print(f"Reason: {blocked_countries[c]}")
        print("\n--- MY SOLUTION ---")
        print("Bharat Global Pay Bridge:")
        print("1. Mobile Money + Crypto Bridge")
        print("2. 100% Legal & Compliant")
        print("3. Low Fee: Only 2% vs 8% bank")
        print("4. Instant Transfer in 5 mins")
    else:
        print(f"\n{c.upper()} - PAYMENT ALLOWED")
        print("Fee: 2% | Time: 5 mins")

print("=== Bharat Global Pay Bridge ===")
country = input("Enter Country Name: ")
check_transfer(country)
