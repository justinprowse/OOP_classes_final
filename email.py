class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        
    def mark_as_read(self):
        self.has_been_read = True
        
inbox = []

def populate_inbox():
    email_1 = Email("justin.prowse@gmail.com", "OOP Task", "You must complete the first OOP task today.")
    email_2 = Email("justin.prowse@gmail.com", "Hyperion Examples", "Here are the practise examples you asked for.")
    email_3 = Email("justin.prowse@gmail.com", "Study Room", "We are having a study room at 2pm tomorrow.")
    inbox.extend([email_1, email_2, email_3])

def list_emails():
    if not inbox:
        print("Inbox is empty.")
        return
    
    for idx, email in enumerate(inbox):
        print(f"{idx} {email.subject_line}")

def read_email(index):
    try:
        email = inbox[index]
    except IndexError:
        print("Invalid email index.")
        return
    
    print("\n--- Email Details ---")
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content:\n{email.email_content}\n")
    email.mark_as_read()
    print(f"\nEmail from {email.email_address} marked as read.\n")
    
populate_inbox()

menu = True

while True:
    user_choice = input("\nWould you like to:\n"
                            "1. Read an email\n"
                            "2. View unread emails\n"
                            "3. Quit application\n"
                            "Enter selection: ")

        try:                            # changed user_choice isdigit to try except
            user_choice = int()
        except ValueError:
        print("Oops - incorrect input.")
        continue
    user_choice = int(user_choice)
    
    if user_choice == 1:
        if not inbox:
            print("Inbox is empty.")
            continue
        print("\nInbox")
        list_emails()
        idx_input = input("Enter the index of the email you want to read: ")
        if not idx_input.isdigit():
            print("Invalid index.")
            continue
        read_index = int(idx_input)
        read_email(read_index)
        
    elif user_choice == 2:
        unread = [(i, e) for i, e in enumerate(inbox) if not e.has_been_read]
        if not unread:
            print("No unread emails.")
        else:
            print("\nUnread emails: ")
            for i, email in unread:
                print(f"{i} {email.subject_line}")
        
    elif user_choice == 3:
        print("Exiting email simulator. Goodbye!")
        break

    else:
        print("Oops - incorrect input.")

# TODO
# functions dont have docstrings 

# replace user_choice isdigit with try except
