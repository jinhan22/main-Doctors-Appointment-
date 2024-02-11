def main():
    print("""
        +===================================+
        |                                   |
        |  Welcome to the Doctor's RaeJin's |
        |             Dog Vet!              |
        |                                   |
        +===================================+""")
    
    print("")

    schedule = {}

    while True:
        print_menu()
        choice = get_choice("Enter your choice (1-3): ")

        if choice == 1:
            schedule_appointment(schedule)
        elif choice == 2:
            view_appointments(schedule)
        elif choice == 3:
            print("Thank you for using the RaeJin's Dog Vet!. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


def print_menu():
    print("")
    print("1. Schedule an Appointment")
    print("2. View Appointments")
    print("3. Exit")

def view_appointments(schedule):
    print("\nScheduled Appointments:")
    if schedule:
        for day, appointments in schedule.items():
            print(f"\n{day}:")
            for time, name in appointments:
                print(f"- {time}, Scheduled by: {name}")
    else:
        print("No appointments scheduled.")

    input("\nPress Enter to return to the main menu...")

def get_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def schedule_appointment(schedule):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("")
    print("Days available:")
    for index, day in enumerate(days, start=1):
        print(f"{index}. {day}")

    day_choice = get_choice("Choose a day (1-7): ")
    time_slots = {'9am', '1pm', '4pm'}

    if 1 <= day_choice <= 7:
        day = days[day_choice - 1]
        if day not in schedule:
            schedule[day] = []

        print("")
        print("Times available:")
        print("1. 9am")
        print("2. 1pm")
        print("3. 4pm")
        print("4. cancel")

        while True:
            time_choice = get_choice("Choose a time (1-3): ")
            if time_choice == 1:
                time = '9am'
            elif time_choice == 2:
                time = '1pm'
            elif time_choice == 3:
                time = '4pm'
            elif time_choice == 4:
                return
            else:
                print("Invalid choice.")
                continue

            if (time, '') in schedule[day]:
                print("Sorry, this time is already taken.")
            else:
                name = input("Enter your name: ")  # Prompt for user's name
                schedule[day].append((time, name))  # Store appointment with user's name
                after_schedule()
                break
    else:
        print("Invalid choice.")

def after_schedule():
    print("")
    print("How may I help you?\n1. Checkup\n2. Parlor\n3. Exit")
    choice = get_choice("Choose from 1-3: ")
    if choice == 1:
        pet_information()
    elif choice == 2:
        parlor_info()
    elif choice == 3:
        exit(0)
    else:
        print("Invalid choice. Returning to the main menu.")
    

def pet_information():
    print("")
    print("Please provide the following information about your pet:")

    name = input("Pet's name: ")
    sex = input("Pet's sex: ")
    age = input("Pet's age: ")
    unusual_discovery = input("What unusual behavior did you discover in your pet: ")

    print("\nOwner's Information:")
    owner_name = input("Owner's name: ")
    contact_number = input("Contact number: ")
    email = input("E-mail: ")

    summary ={
        'name': name,
        'sex': sex,
        'age': age,
        'unusual_discovery': unusual_discovery,
        'owner_name': owner_name,
        'contact_number': contact_number,
        'email': email
    }

    confirm_information(summary)


def confirm_information(info):
    print("\nConfirmation:")
    print(f"Pet's name: {info['name']}")
    print(f"Pet's sex: {info['sex']}")
    print(f"Pet's age: {info['age']}")
    print(f"What unusual behavior did you discover in your pet: {info['unusual_discovery']}")
    print(f"Owner's name: {info['owner_name']}")
    print(f"Contact number: {info['contact_number']}")
    print(f"E-mail: {info['email']}")

    print("")
    confirm = input("Are these information correct? (Type 'confirm' to confirm or 'deny' to make changes): ")

    if confirm.lower() == 'confirm':
        print ("")
        print("Thank you for setting an appointment with us! We will contact you after confirming your request.")
        return True
    elif confirm.lower() == 'deny':
        print("Please input the information again.")
        return False
    else:
        print("Invalid choice. Please try again.")
        return (info)



def parlor_info():
    print("Please provide the following information about your dog:")
    name = input("Dog's name: ")
    sex = input("Dog's sex: ")
    age = input("Dog's age: ")

    print("\nServices for your dog:")
    print("1. Bathing")
    print("2. Haircut")
    print("3. Nail trimming")
    services = input("Enter the numbers corresponding to the services you want (e.g., '1 2'): ")

    owner_name = input("\nOwner's name: ")
    contact_number = input("Contact number: ")
    email = input("E-mail: ")

    return {
        'name': name,
        'sex': sex,
        'age': age,
        'services': services,
        'owner_name': owner_name,
        'contact_number': contact_number,
        'email': email
    }

def confirm_parlor(info):
    print("\nConfirmation:")
    print(f"Dog's name: {info['name']}")
    print(f"Dog's sex: {info['sex']}")
    print(f"Dog's age: {info['age']}")

    services = [int(service) for service in info['services'].split()]
    print("Services for your dog:")

    for service in services:
        if service == 1:
            print("- Bathing")
        elif service == 2:
            print("- Haircut")
        elif service == 3:
            print("- Nail trimming")

    print(f"Owner's name: {info['owner_name']}")
    print(f"Contact number: {info['contact_number']}")
    print(f"E-mail: {info['email']}")

    confirm = input("\nAre these information correct? (Type 'confirm' to confirm or 'deny' to make changes): ")

    if confirm.lower() == 'confirm':
        print("Thank you! Information confirmed.")
        return True
    elif confirm.lower() == 'deny':
        print("Please input the information again.")
        return False
    else:
        print("Invalid choice. Please try again.")
        return confirm_parlor(info)


main()
