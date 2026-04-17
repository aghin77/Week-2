class Student:
    school_name = "Global Tech School"   # class variable

    def __init__(self, name, id_number):
        self.name = name              # public
        self.__id_number = id_number  # private

    # Getter
    def get_id(self):
        return self.__id_number

    # Setter
    def set_id(self, new_id):
        if len(str(new_id)) == 4 and str(new_id).isdigit():
            self.__id_number = new_id
            print("ID updated successfully")
        else:
            print("Invalid ID! Must be 4 digits")

    # Instance Method
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Class Method
    @classmethod
    def school_info(cls):
        print(f"School Name: {cls.school_name}")


# ----------- Testing ------------

# Create object
student1 = Student("Aghin", 1234)

# Access public
print("Name:", student1.name)

# Try accessing private (will cause error if uncommented)
# print(student1.__id_number)

# Access using getter
print("Student ID:", student1.get_id())

# Update using setter
student1.set_id(5678)
print("Updated ID:", student1.get_id())

# Invalid update
student1.set_id(12)

# Instance method
student1.study("Python")

# Class method
Student.school_info()