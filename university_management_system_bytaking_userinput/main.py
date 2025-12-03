# Base class representing a general person
class Person:
    def __init__(self, Id: int, Name: str, Age: int):
        self.Id = Id
        self.Name = Name
        self.Age = Age

# Faculty class inheriting from Person
class Faculty(Person):
    def __init__(self, Id: int, Name: str, Age: int, Dept: str, Salary: int, Subjects: list[str]):
        super().__init__(Id, Name, Age)
        self.Dept = Dept
        self.Subjects = Subjects
        self.Salary = Salary

# Student class inheriting from Person
class Student(Person):
    def __init__(self, Id: int, Name: str, Age: int, Dept: str):
        super().__init__(Id, Name, Age)
        self.Dept = Dept


class University:
    def __init__(self, Name, Course_list):
        self.Name = Name
        self.Course_list = Course_list
        self.std_table = {}
        self.emp_table = {}

    def admission(self, std_obj: Student):
        if std_obj.Id in self.std_table:
            return "Student already exists!"
        self.std_table[std_obj.Id] = [std_obj.Name, std_obj.Age, std_obj.Dept]
        return "Student added Successfully!"

    def employee_admission(self, emp_obj: Faculty):
        if emp_obj.Id in self.emp_table:
            return "Employee already exists!"
        self.emp_table[emp_obj.Id] = [emp_obj.Name, emp_obj.Age, emp_obj.Dept, emp_obj.Salary, emp_obj.Subjects]
        return "Employee added Successfully!"

    def student_details(self):
        if not self.std_table:
            return "No students found."
        return self.std_table

    def employee_details(self):
        if not self.emp_table:
            return "No employees found."
        return self.emp_table

    def remove_student(self, std_id):
        if std_id in self.std_table:
            del self.std_table[std_id]
            return "Student removed successfully!"
        return "Student ID not found!"

    def remove_employee(self, emp_id):
        if emp_id in self.emp_table:
            del self.emp_table[emp_id]
            return "Employee removed successfully!"
        return "Employee ID not found!"

    def total_counts(self):
        return f" Students: {len(self.std_table)} | Employees: {len(self.emp_table)}"


# ---------------- MAIN MENU ----------------
if __name__ == "__main__":
    u = University("NRI", ["ECE", "CSE", "CSD", "CSM","EEE","MECH","CIVIL","AIML"])

    while True:
        print("\n=================== UNIVERSITY MENU ===================")
        print("1. Add Student")
        print("2. Add Employee")
        print("3. Show All Students")
        print("4. Show All Employees")
        print("5. Remove Student")
        print("6. Remove Employee")
        print("7. Show Total Count")
        print("8. Exit")
        print("=========================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            Id = int(input("Enter Student ID: "))
            Name = input("Enter Student Name: ")
            Age = int(input("Enter Age: "))
            Dept = input("Enter Department: ")
            student = Student(Id, Name, Age, Dept)
            print(u.admission(student))

        elif choice == "2":
            Id = int(input("Enter Employee ID: "))
            Name = input("Enter Name: ")
            Age = int(input("Enter Age: "))
            Dept = input("Enter Department: ")
            Salary = int(input("Enter Salary: "))
            Subjects = input("Enter Subjects (comma separated): ").split(",")
            faculty = Faculty(Id, Name, Age, Dept, Salary, Subjects)
            print(u.employee_admission(faculty))

        elif choice == "3":
            print("\n STUDENTS LIST:", u.student_details())

        elif choice == "4":
            print("\n EMPLOYEE LIST:", u.employee_details())

        elif choice == "5":
            Id = int(input("Enter Student ID to remove: "))
            print(u.remove_student(Id))

        elif choice == "6":
            Id = int(input("Enter Employee ID to remove: "))
            print(u.remove_employee(Id))

        elif choice == "7":
            print(u.total_counts())

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid Choice! Please try again.")
