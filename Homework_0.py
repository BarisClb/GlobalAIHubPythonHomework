student_name = "Baris Celebi"
classes = []

import sys

def welcome():
    c = 3
    while c > 0:
        name = input("Your Name: ")
        if name == student_name:
            c = 0
            return print("Welcome, " + name)
        elif name != student_name and c > 0:
            c -= 1
            print("Wrong name, try again.")
    sys.exit("Please try again later.")

welcome()

classes = None

def enter_classes():
    tries = 3
    classes = input("Enter your classes with a ',' between them: ")
    classes = list(classes.split(","))
    while tries > 0:
        if len(classes) < 3:
            return print("You failed in class.")
        elif len(classes) > 5:
            print("You can't take more than 5 classes. Try again.")
            tries -= 1
        else:
            return print("Your classes are: " + str(classes))

enter_classes()

exam_course = input("Pick a course to take exam: ")

def exam_result():
    exam_grades = input("Enter your midterm, final and project grades with a ',' between them: ")
    exam_grades = list(exam_grades.split(","))
    midterm_grade = int(exam_grades[0])
    final_grade = int(exam_grades[1])
    project_grade = int(exam_grades[2])
    final_grade = (midterm_grade * 0.3) + (final_grade * 0.5) + (project_grade * 0.2)
    if final_grade > 90:
        return print("Your final grade in " + exam_course + " is AA with: " + str(final_grade))
    elif final_grade > 70:
        return print("Your final grade in " + exam_course + " is BB with: " + str(final_grade))
    elif final_grade > 50:
        return print("Your final grade in " + exam_course + " is CC with: " + str(final_grade))
    elif final_grade > 30:
        return print("Your final grade in " + exam_course + " is DD with: " + str(final_grade))
    else:
        return print("Your final grade is FF in " + exam_course + " with: " + str(final_grade) + ". You failed this class.")

exam_result()
