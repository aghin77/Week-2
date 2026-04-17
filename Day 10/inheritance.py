# Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"User {self.username} logged in.")


# Child Class (Inheritance)
class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    # Method Overriding
    def login(self):
        print(f"Admin {self.username} logged in with full access.")

    # Special Method
    def delete_user(self):
        print(f"Admin {self.username} deleted a user.")


# Creating objects
user1 = User("Aghin", "aghin@email.com")
admin1 = Admin("AdminAghin", "admin@email.com", "All")

# Polymorphism
users = [user1, admin1]

for u in users:
    u.login()

# Admin special method
admin1.delete_user()

# This will give error if uncommented
# user1.delete_user()