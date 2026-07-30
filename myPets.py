my_pets = ['Zophie', 'Pooka', 'Fat-tail']  # List of pet names

print('Enter a pet name:')  # Prompt user to input a pet name
name = input()  # Get user input and store it in the variable 'name'

if name not in my_pets:  # Check if the entered pet name is not in the list
    print('I do not have a pet named ' + name)  # Display message if pet is not found
else:
    print(name + ' is my pet.')  # Display message if pet is found