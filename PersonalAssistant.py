class PersonalAssistant:
    def __init__(self, todos, birthdays,
    contacts):

        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts

    def get_contacts(self):
      return self.contacts

    def add_todo(self, new_item):
      self.todos.append(new_item)

    def get_contact(self, name):
      if name in self.contacts:
        return (f"{name} is a/an {self.contacts[name]}.")
      else:
          return "Can't find a contact for this person."

    def add_contact(self, name, contact):
      if name in self.contacts:
        return ("You already have a contact for this person!")
      else:
        self.birthdays[name] = contact
        return  (f"You added {name}'s contact of {contact} to your list!")

    def remove_contact(self, name):
      if name in self.contacts:
        self.contacts.pop(name)
        return (f"{name}'s contact has been removed!")
      else:
         return ("You do not have a contact for this person!")

    def remove_todo(self, todo_item):
      # Checks if todo_item is in todos list
      if todo_item in self.todos:
        # Gets the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
        return f'{todo_item} was removed'
      else:
        print("To-do is not in list!")

    def get_todos(self):
      return self.todos

    def get_birthday(self, name):
      if name in self.birthdays:
        return (f"{name}'s birthday is on {self.birthdays[name]}.")
      else:
          return "Can't find a birthday for this person."

    def add_birthday(self, name, bday):
      if name in self.birthdays:
        return ("You already have a birthday for this person!")
      else:
        self.birthdays[name] = bday
        return  (f"You added {name}'s birthday of {bday} to your list!")

    def remove_birthday(self, name):
      if name in self.birthdays:
        self.birthdays.pop(name)
        return (f"{name}'s birthday has been removed!")
      else:
        return ("You do not have a birthday for this person!")


