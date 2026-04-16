# week 2/Day 3/oop_basics.py

class Course:
    # Constructor
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats

    # Method to display course info
    def display_info(self):
        print(f"Course: {self.name} costs ₹{self.price}")

    # Method to enroll a student
    def enroll_student(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Enrolled in {self.name}. Seats left: {self.seats}")
        else:
            print(f"{self.name} is FULL")

    # Method to check status
    def course_status(self):
        if self.seats > 0:
            return "ACTIVE"
        else:
            return "FULL"


# Create objects
course1 = Course("Full Stack Masterclass", 5000, 2)
course2 = Course("Generative AI & LLMs", 8000, 1)
course3 = Course("Advanced System Design", 10000, 0)

# Display info
course1.display_info()
course2.display_info()
course3.display_info()

print()

# Enroll students
course1.enroll_student()
course1.enroll_student()
course1.enroll_student()  # Should show FULL

print()

course2.enroll_student()
course2.enroll_student()  # Should show FULL

print()

course3.enroll_student()  # Already FULL

print()

# Check status
print(f"{course1.name} Status: {course1.course_status()}")
print(f"{course2.name} Status: {course2.course_status()}")
print(f"{course3.name} Status: {course3.course_status()}")