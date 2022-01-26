from student import Student

def verification():
    decision = input("What do you want to do?\n\
        Generate the students list and grades (GENERATE)\n\
        Generated passed and failed lists based on grades (CALCULATE)\n\
        List students (LIST)\n\
        List students who passed (PASSED)\n\
        List students who failed (FAILED)\n").lower()

    if decision == 'generate':
        Student.instantiate_from_csv()
        print("Student list generated.\n")
        verification()

    elif decision == 'calculate':
        Student.calculate_grades()
        verification()
    elif decision == 'list':
        if Student.all:
            print(Student.all)
        else:
            print("The student list is empty. Please, generate the list first.\n")

        verification()

    elif decision == 'passed':
        Student.list('passed')
        verification()

    elif decision == 'failed':
        Student.list('failed')
        verification()

    else:
        print("That is not a valid option. Try again.\n")
        verification()

if __name__ == '__main__':
    verification()