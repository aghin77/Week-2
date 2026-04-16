# Day 6 - Functions & Scope

# 1. Basic Function
def greet_user(name):
    print(f"Hello {name}, welcome!")

greet_user("Aghin")


# 2. Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum is:", result)


# 3. Default Arguments
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("Buddy")
describe_pet("Whiskers", "cat")


# 4. Using *args
def sum_all(*args):
    return sum(args)

print("Total sum:", sum_all(1, 2, 3, 4, 5))


# 5. Using **kwargs
def build_profile(first_name, last_name, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    profile.update(kwargs)
    print(profile)

# Updated values here
build_profile("Aghin", "Aji", middle_name="Jose", location="Kerala", job="Student")


# 6. Scope Challenge
count = 0

def change_count():
    global count   # allows modifying global variable
    count = count + 1
    print("Inside function:", count)

change_count()
print("Outside function:", count)

# Explanation:
# Without 'global', Python treats count inside the function as a new local variable.
# With 'global', it modifies the global variable.