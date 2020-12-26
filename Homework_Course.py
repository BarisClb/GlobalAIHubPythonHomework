import sys

# Variables

student_list = ["Baris Celebi"]
student_name = None
student_courses = None
student_information = {
    "Name" : None,
    "Courses" : None,
    "Exam_Course" : None,
    "Midterm_Grade" : None,
    "Final_Grade" : None,
    "Project_Grade" : None,
    "Final_Score" : None,
    "Final_Score_Grade" : None
}


# Welcoming Screen

def welcome():
    tries = 3
    global student_name
    while tries > 0:
        student_name = input("Please write your Full Name: ")
        if student_name in student_list:
            student_information["Name"] = student_name
            return print(f"Welcome, {student_name}.")
        else:
            tries -= 1
            print("Wrong name, try again.")
    sys.exit("Too many failed tries, please try again later.")

welcome()

# Picking Courses

def enter_courses():
    tries = 3
    global student_courses
    while tries > 0:
        student_courses = input("Please write your courses with a ',' between them: ")
        student_courses = list(student_courses.split(","))
        if len(student_courses) < 3:
            sys.exit("You failed in class.") 
        elif len(student_courses) > 5:
            print("You can't take more than 5 courses. Try again.")
            tries -= 1
        else:
            student_information["Courses"] = str(student_courses).strip("[]")
            return print("Your courses are: " + student_information["Courses"])
    sys.exit("Too many failed tries, please try again later.")

enter_courses()

# Taking The Exam

def pick_a_course():
    tries = 3
    global exam_course
    while tries > 0:
        exam_course = input("Pick a course to take exam: ")
        if exam_course in student_courses:
            answer = input(f"You choose {exam_course} course to take exams. Are you sure? (Yes/No): ")
            if answer == "Yes":
                student_information["Exam_Course"] = exam_course
                return print(f"You took exams for your {exam_course} course.")
            elif answer == "No":
                tries -= 1
            else:
                print("Wrong input. Please try again.")
                tries -= 1
        else:
            print("You must choose from one of your courses. Please try again.")
            tries -= 1
    sys.exit("Too many failed tries, please try again later.")


pick_a_course()

# Exam Results

def exam_result():
    tries = 3
    while tries > 0:
        exam_grades = input("Please enter your midterm, final and project grades with a ',' between them: ")
        try:
            exam_grades = list(exam_grades.split(","))
            if len(exam_grades) < 3:
                print("Please enter all your grades.")
                tries -= 1
                continue
            elif len(exam_grades) > 3:
                print("Please don't enter more than three grades.")
                tries -= 1
                continue
            midterm_grade = float(exam_grades[0])
            final_grade = float(exam_grades[1])
            project_grade = float(exam_grades[2])
            final_score = (midterm_grade * 0.3) + (final_grade * 0.5) + (project_grade * 0.2)
            if midterm_grade < 0 or final_grade < 0 or project_grade < 0: 
                print("You can't score less than '0' on an exam. Please try again.")
                tries -= 1
            elif midterm_grade > 100 or final_grade > 100 or project_grade > 100:
                print("You can't score more than '100' on an exam. Please try again")
                tries -= 1
            else:
                student_information["Midterm_Grade"] = midterm_grade
                student_information["Final_Grade"] = final_grade
                student_information["Project_Grade"] = project_grade
                student_information["Final_Score"] = final_score                       
                if final_score > 90:
                    student_information["Final_Score_Grade"] = "AA"
                    return print("Your final grade in " + exam_course + " is AA with a score of " + str(final_score) + ".")
                elif final_score > 70:
                    student_information["Final_Score_Grade"] = "BB"
                    return print("Your final grade in " + exam_course + " is BB with a score of " + str(final_score) + ".")
                elif final_score > 50:
                    student_information["Final_Score_Grade"] = "CC"
                    return print("Your final grade in " + exam_course + " is CC with a score of " + str(final_score) + ".")
                elif final_score > 30:
                    student_information["Final_Score_Grade"] = "DD"
                    return print("Your final grade in " + exam_course + " is DD with a score of " + str(final_score) + ".")
                else:
                    student_information["Final_Score_Grade"] = "FF"
                    return print("Your final grade is FF in " + exam_course + " with a score of " + str(final_score) + ". You failed this course.")
        except ValueError:
            print("Please enter your grades in numerical value.")
            tries -= 1
    sys.exit("Too many failed tries, please try again later.")

exam_result()

# All the information 

print("Thank you for your participation. Here is your information."),

def student_info():
    for k,v in student_information.items():
        print(k, " : ", v)

student_info()