# Given the following Person class:

class Person:

    

    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greetingcount = 0


    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greetingcount = self.greetingcount + 1

# Create a new method for class Person to return the person phone number and email so that we can call the method if we needed the person information.
    def description(self):
      return f'{self.name} phone number is {self.phone} and his email is {self.email}.'

# Add a method to print out the contact info for a object instance of Person
    def print_contact_info(self):
     print(f"{self.name}'s email: {self.email}")
     print(f"{self.name}'s phone number: {self.phone}")   

# add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor __init__. Once you've done this you should be able to add a friend to a person using list's append method:

    def add_friend(self, other_friend):
      self.friends.append(other_friend)
      for friend in self.friends:
        print(friend.name)

#
    def num_friends(self):
      print(len(self.friends))

    def greeting_count(self):
        return self.greetingcount



# Instantiate an instance object to the class Person with their name, email, and phone number
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# Have sonny greet jordan using the greet method
sonny.greet(jordan)

# Have jordan greet sonny using the greet method
jordan.greet(sonny)

# Write a print statement to print the contact info (email and phone) of Sonny
print(sonny.description())

# Write a print statement to print the contact info (email and phone) of Jordan
print(jordan.description())

sonny.print_contact_info()


jordan.add_friend(sonny)
sonny.add_friend(jordan)

sonny.num_friends()
jordan.num_friends()


sonny.greet(jordan)
sonny.greet(jordan)

print(sonny.greeting_count())