# ---------------------------------------
#    Welcome to the Visa Eligibility System   
# ---------------------------------------

print("---------------------------------------")
print("   Welcome to the Visa Eligibility System")
print("---------------------------------------\n")

# Traveler Profile Input
print("Traveler Profile:")
Name_info = input("Name: ")
Age_info = int(input("Age: "))
Nationality_info = input("Nationality (e.g., allowed or restricted): ").lower()
passport_info = input("Passport Valid? (valid/expired): ").lower()
vaccination_info = input("Vaccinated? (yes/no): ").lower()

# Eligibility Conditions
if Age_info >= 18 and Nationality_info == "allowed" and passport_info == "valid" and vaccination_info == "yes":
    print("\n✅ Visa Eligibility Result: Visa Approved")
    print(f"Congratulations, {Name_info}! You meet all the requirements for visa approval.")
    print("Safe travels! 🌍✈️")

else:
    print("\n❌ Visa Eligibility Result: Visa Denied")
    print(f"Sorry, {Name_info}. You are not eligible for visa approval based on the following reason(s):")
    if Age_info < 18:
        print("- You must be at least 18 years old.")
    if Nationality_info != "allowed":
        print("- Your nationality is currently restricted.")
    if passport_info != "valid":
        print("- Your passport must be valid.")
    if vaccination_info != "yes":
        print("- COVID vaccination is required for travel.")
    print("Please review the requirements and try again.")

# End of System
print("\n---------------------------------------")
print("  Thank you for using the Visa Eligibility System")
print("  Stay safe and informed. 🌐")
print("---------------------------------------")