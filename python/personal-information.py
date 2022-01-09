# Takes basic information from user 
# and places it in a table that is 
# displayed back to the user
first= input("First name: ")
last= input("Last name: ")
email= input("Email address: ")
phone= input("Phone number: ")
job= input("Job title: ")
id= input("ID number: ")

#additional info
hair= input("Hair color: ")
eye= input("Eye color: ")
month= input("Starting month: ")
training= input("Completed additional training?")

#Prints ID Card on user display
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()},{first.capitalize()}")
print(job.title())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair:15} Eyes: {eye}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------")