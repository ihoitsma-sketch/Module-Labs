# Isabelle Hoitsma
# Mod2_Case_study
# This app takes a students name, and checks their GPA to see if they made it onto the Honor Roll or Dean's list.

students_last = ""
students_first = ""
students_gpa = ""

students_last = input("Enter students last name, or ZZZ to quit: ")

while students_last != "ZZZ":

    students_first = input("Enter students first name: ")
    students_gpa = float(input("Enter students current GPA: "))

    if students_gpa >= 3.5:
        print(f"{students_first} {students_last} has made the Dean's List.")

    elif students_gpa >= 3.25:
        print(f"{students_first} {students_last} has made the Honor Roll.")

    else:
        print(f"{students_first} {students_last} has not made either list.")

    students_last = input("Enter students last name, or ZZZ to quit: ")