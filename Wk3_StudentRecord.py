# A program thst is capabale of storing and viewing student basic information
class StudentRecord:
    def __init__(self):
        self.students = {}
    
    def addStudent(self):
        studentID = input("Enter your student ID: ")
        name = input("Enter your name: ")
        age = input("Enter age: ")
        level = input("Enter level: ")

        self.students[studentID] = {
            "name": name,
            "age": age,
            "level": level
        }
        print(f"Student {name} added!")

    def viewStudent(self):
        studentID = input("Enter student ID: ")
        if studentID in self.students:
            student = self.students[studentID]
            print(f"Student IS: {studentID}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"level: {student['level']}")
        else: 
            print("Student ID not found")
    
    def run(self):
        while True:
            print("1. Add Student")
            print("2. View Student")
            print("3. Exit")

            chosenOption = input("Chosoe an option: ")

            if chosenOption == "1":
                self.addStudent()
            elif chosenOption == "2":
                self.viewStudent()
            elif chosenOption == "3":
                break
            else: 
                print("Invalid option. Try again")

if __name__ == "__main__":
    system = StudentRecord()
    system.run()