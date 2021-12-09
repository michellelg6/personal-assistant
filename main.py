#imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class

with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)

  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    4: Display birthdays
    5: Add a birthday
    6: Remove a birthday
    7: Get contacts
    8: Add a contact
    9: Remove a contact

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    elif user_command == "4":
        for bday in assistant.birthdays:
          print (assistant.get_birthday(bday))
        name = input("\nWhich birthday would you like get?\n")
        print(f"\n{assistant.get_birthday(name)}")
    elif user_command == "5":
        print("Add a birthday: \n")
        name = input("Name of the person: ")
        birthday = input("Their birthday (ex: 08/18/2000): ")
        print(f"\n{assistant.add_birthday(name, birthday)}")
    elif user_command == "6":
        for bday in assistant.birthdays:
          print(f"\n {assistant.get_birthday(bday)}")
        name = input("\nWhich birthday would you like removed?\n")
        print(f"\n{assistant.remove_birthday(name)}")
    elif user_command == "7":
      for cont in assistant.contacts:
          print (assistant.get_contact(cont))
      name = input("\nWhich contact would you like to get?\n")
      print(f"\n{assistant.get_contact(name)}")
    elif user_command == "8":
      print("Add a contact: \n")
      name = input("Name of the person: ")
      contact = input("Enter their contact ")
      print(f"\n{assistant.add_contact(name,contact)}")
    elif user_command == "9":
      for contact in assistant.contacts:
          print(f"\n {assistant.get_contact(contact)}")
      name = input("\nWhich contact would you like removed?\n")
      print(f"\n{assistant.remove_contact(name)}")
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file

with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays:
  json.dump(assistant.get_todos(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)