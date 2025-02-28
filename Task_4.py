
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return (f'Contact {name} {phone} added.')
    except ValueError: 
        return "Invalid format of contact."

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return (f'Contact {name} changed to {phone}')
    except ValueError: 
        return "Invalid arguments"

def phone_contact(args, contacts):
    try: 
        name = args[0]
        phone = contacts[name]
        return (f'Contact {name} phone is {phone}' )
    except ValueError: 
        return "Invalid argument"
    
def all_contacts(contacts):
    for key, value in contacts.items(): 
        print(f'{key} : {value}')

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))  
            case "phone":
                print(phone_contact(args, contacts))   
            case "all":
                print(all_contacts(contacts))                 
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()

