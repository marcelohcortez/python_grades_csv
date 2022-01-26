import csv

class Student:
    all = []
    def __init__(self, first_name: str, last_name: str, first_grade: float, second_grade: float):
        assert first_grade >= 0.0, f"The grade for {first_name} {last_name} must be greater than or equal to 0"
        assert first_grade <= 10.0, f"The grade for {first_name} {last_name} must be lower than or equal to 10"
        assert second_grade >= 0.0, f"The grade for {first_name} {last_name} must be greater than or equal to 0"
        assert second_grade <= 10.0, f"The grade for {first_name} {last_name} must be lower than or equal to 10"

        self.__first_name = first_name
        self.__last_name = last_name
        self.__first_grade = first_grade
        self.__second_grade = second_grade

        Student.all.append(self)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv", "r") as f:
            reader = csv.DictReader(f)
            students = list(reader)
        
        for student in students:
            Student(
                first_name = student.get("first name"),
                last_name = student.get("last name"),
                first_grade = float(student.get("first grade")),
                second_grade = float(student.get("second grade"))
            )
    
    @classmethod
    def calculate_grades(cls):
        with open("passed.csv", "w") as passed:
            passed.write("first name,last name,final grade\n")
        
        with open("failed.csv", "w") as failed:
            failed.write("first name,last name,final grade\n")

        with open("data.csv", "r") as data:
            reader = csv.DictReader(data)
            students = list(reader)
        
        for student in students:
            first_grade = float(student.get("first grade"))
            second_grade = float(student.get("second grade"))
            final_grade = (first_grade + second_grade) / 2
            
            if final_grade >= 7.0:
                with open("passed.csv", "a") as passed:
                    passed.write(f'{student.get("first name")},{student.get("last name")},{final_grade}\n')
            else:
                with open("failed.csv", "a") as failed:
                    failed.write(f'{student.get("first name")},{student.get("last name")},{final_grade}\n')

        print("Final grades calculated.")

    @staticmethod
    def list(status):
        with open(f"{status}.csv", "r") as f:
            reader = csv.DictReader(f)
            students = list(reader)
        
        for student in students:
            print(f"{student.get('first name')} {student.get('last name')} || {float(student.get('final grade'))}")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__first_name} {self.__last_name} || First Grade: {self.__first_grade} || Second Grade: {self.__second_grade}\n"