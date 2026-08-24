# BCH Software Inc. - Sprint 1: Interactive Kiosk
# Track: Python Software Engineering
#8/20/26
def main():
    print()
    print()
    print("========================================")
    print("Name : " + name)
    print("Company : " + company)
    print("Email Address : " + Email)
    print("Badge Tier : " + badge)
    print("========================================")
    print("      BCH ENTERPRISE VISITOR KIOSK      ")
    print("========================================")
    
    # SE: Use input() to capture Name, Company, Email, and Badge Tier
    # SE: Use print() to render the ASCII badge

print()
print("=====     APEX VISITOR LOGIN     ======")

print("Enter full name:")
name = input()
print("Name : " + name)
print()
print("enter what company you are with: ")
company = input()
print("company : " + company)
print()
print("Enter viable Email:")
Email = input()
print("Email : " + Email)
print()
print("Enter badge tier (e.g VIP, Speaker etc) : ")
badge = input()
print("badge tier : " + badge) 
print()

if __name__ == "__main__":
    main()