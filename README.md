# myPets.py

**Pet Name Checker Script**

### Description

This Python script checks if a user-inputted pet name exists in a predefined list of pets. If the pet name is found, it displays a confirmation message; otherwise, it displays a message indicating that the pet is not in the list.

### Code Analysis

```python
my_pets = ['Zophie', 'Pooka', 'Fat-tail']  # List of pet names
```

*   A list called `my_pets` is initialized with three pet names.

```python
print('Enter a pet name:')  # Prompt user to input a pet name
name = input()  # Get user input and store it in the variable 'name'
```

*   The script prompts the user to enter a pet name and stores the input in the `name` variable.

```python
if name not in my_pets:  # Check if the entered pet name is not in the list
    print('