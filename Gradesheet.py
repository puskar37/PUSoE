def calculate_gpa():
    """Calculate GPA based on grades and credit hours."""

    branches = {
        "Computer": {
            "1": {
                "MATHEMATICS - I": 3,
                "ENGLISH FOR TECHNICAL COMMUNICATION": 4,
                "PHYSICS": 3,
                "COMPUTER PROGRAMMING": 3,
                "FUNDAMENTAL OF COMPUTING TECHNOLOGY": 3,
                "ENGINEERING DRAWING - I": 3,
                "WORKSHOP TECHNOLOGY": 2,
            },
            "2": {
                "MATHEMATICS - II": 3,
                "CHEMISTRY": 3,
                "APPLIED MECHANICS": 3,
                "BASIC ELECTRICAL ENGINEERING": 3,
                "DIGITAL LOGIC": 3,
                "OBJECT ORIENTED PROGRAMMING WITH C++": 3,
            },
            "3": {
                "MATHEMATICS - III": 3,
                "DATA STRUCTURES AND ALGORITHM": 3,
                "OBJECT ORIENTED ANALYSIS AND DESIGN": 3,
                "COMPUTER GRAPHICS": 3,
                "ELECTRONICS DEVICES AND CIRCUITS - I": 3,
                "APPLIED SOCIOLOGY": 2,
                "PROJECT-I": 3,
            },
            "4": {
                "DATABASE MANAGEMENT SYSTEM": 3,
                "PYTHON PROGRAMMING": 3,
                "DISCRETE STRUCTURE": 3,
                "MICROPROCESSOR": 3,
                "COMMUNICATION SYSTEM": 3,
                "PROBABILITY & STATISTICS": 3,
            },
            "5": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            },
            "6": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            },
            "7": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            },
            "8": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            }
        },

        "Civil": {
            "1": {
                "MATHEMATICS - I": 3,
                "CHEMISTRY": 3,
                "APPLIED MECHANICS - I (STATICS)": 3,
                "CIVIL ENGINEERING MATERIALS": 3,
                "BASIC ELECTRICAL ENGINEERING": 2,
                "ENGINEERING DRAWING - I": 3,
                "WORKSHOP TECHNOLOGY": 2,
            },
            "2": {
                "MATHEMATICS - II": 3,
                "PHYSICS": 4,
                "APPLIED MECHANICS - II(DYNAMICS)": 3,
                "BUILDING TECHNOLOGY": 3,
                "FUNDAMENTAL OF THERMO. & HEAT TRANSFER": 2,
                "ENGINEERING DRAWING - II": 3,
            },
            "3": {
                "MATHEMATICS-III": 3,
                "STRENGTH OF MATERIALS": 3,
                "FLUID MECHANICS": 3,
                "SURVEY - I": 3,
                "ENGINEERING GEOLOGY": 3,
                "BASIC ELECTRONICS ENGINEERING": 2,
                "COMPUTER PROGRAMMING": 3,
            },
            "4": {
                "PROBABILITY & STATISTICS": 3,
                "SURVAY - II": 3,
                "HYDRAULICS": 3,
                "THEORY OF STRUCTURE - I": 3,
                "CONCRETE TECHNOLOGY & MASONRY STRCTURES": 3,
                "CIVIL ENGINEERING DRAWING": 2,
                "ENGLISH FOR TECHNICAL COMMUNICATION": 3,
            },
            "5": {
                "SOIL MECHANIC": 3,
                "SURVEY CAMP": 2,
                "THEORY OF STRUCTURE - II": 3,
                "WATER SUPPLY ENGINEERING": 3,
                "TRNSPORTING ENGINEERING - I": 3,
                "ENGINEERING HYDROLOGY": 3,
                "DESIGN OF STEEL AND TIMBER STRUCTURE": 3,
            },
            "6": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            },
            "7": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            },
            "8": {
                "": 3, "": 3, "": 3, "": 3, "": 3, "": 3, "": 3,
            }
        },      
    }

    semester_in_number = {
        "1": "FIRST SEMESTER", "2": "SECOND SEMESTER", "3": "THIRD SEMESTER",
        "4": "FOURTH SEMESTER", "5": "FIFTH SEMESTER", "6": "SIXTH SEMESTER",
        "7": "SEVENTH SEMESTER", "8": "EIGHTH SEMESTER"
    }

    print("Enter 1 for Computer Engineering or 2 for Civil Engineering.")
    branch_input = input("Enter your choice (1 or 2): ").strip()
    if branch_input == "1":
        branch = "Computer"
    elif branch_input == "2":
        branch = "Civil"
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    semester = input("Enter semester (1 -- 8): ").strip()
    if semester not in branches[branch]:
        print("Invalid semester entered. Please enter a number between 1 and 8.")
        return

    semester_name = semester_in_number.get(semester)

    student_name = input("Enter the name of the student: ").strip().upper()
    file_name = student_name.split()[0].capitalize() if " " in student_name else student_name.capitalize()

    subject_list = branches[branch][semester]
    grades = {}
    failed = False  # Flag to check failure

    total_credits = 0
    total_points = 0
    f_count = 0

    # Input grades for each subject
    for subject, credit in subject_list.items():
        while True:
            grade = input(f"Enter grade for {subject}: ").upper()
            if grade not in ["A+", "A", "B+", "B", "C", "D", "F"]:
                print("Invalid grade entered. Please use A+, A, B+, B, C, D, or F.")
            else:
                break

        # Grade-to-point conversion
        grade_point = {
            "A+": 4.0, "A": 3.75, "B+": 3.50, "B": 3.00, "C": 2.50, "D": 1.75, "F": 0,
        }[grade]

        # Check if any subject is failed
        if grade == "F":
            failed = True
            f_count += 1

        total_credits += credit
        total_points += grade_point * credit
        grades[subject] = grade

    # GPA Calculation
    if failed:
        gpa = total_points / total_credits  # GPA but failed
        result = f"Fail, due to {f_count}F grade(s)."
    else:
        gpa = total_points / total_credits
        result = "Pass"

    # Determine the final grade using the dictionary
    final_grade = calculate_final_grade(gpa)

    # Display result
    display_gradesheet(student_name, semester_name, branch, subject_list, grades, total_credits, gpa, result, final_grade)

    # Save gradesheet to a file
    save_gradesheet_to_file(student_name, file_name, semester, semester_name, branch, subject_list, grades, total_credits, gpa, result, final_grade)


def calculate_final_grade(gpa):
    """Determine the final grade based on GPA using a dictionary."""
    grade_map = {
        4.0: "A+", 3.75: "A", 3.50: "B+", 3.00: "B", 2.50: "C",
        1.75: "D", 0.00: "F"
    }
    
    for threshold in grade_map:
        if gpa >= threshold:
            return grade_map[threshold]
    return "F"  # Default case for gpa below 1.0


def display_gradesheet(student_name, semester_name, branch, subject_list, grades, total_credits, gpa, result, final_grade):
    """Display the gradesheet on the console."""
    print("\n\n                          PURBANCHAL UNIVERSITY")
    print("                   Office of The Examination Management")
    print("                            Biratnagar, Nepal")
    if "Fail" in result:
        print("\n                          Sorry! You have failed.")
    else:
        print(f"\n                    Congratulations! You have Passed.")
    print("                             Grade/Mark-Sheet\n")
    print(f"Name: {student_name}")
    print(f"Year/Semester: {semester_name}")
    print(f"Result of: BACHELOR IN {branch} ENGINEERING\n")
    print(f"{'S.N':<4} {'Subjects':<40} {'Credit Hour':<12} {'Mark/Grade Obtained'}")
    print("=" * 78)
    for i, (subject, credit) in enumerate(subject_list.items(), 1):
        print(f"{i:<4} {subject:<40} {credit:<12} {grades[subject]}")
    print("=" * 78)
    print(f"{'Grand Total':<45} {total_credits:<12} {gpa:.2f}({(gpa*25):.2f}%)")
    print(f"Final Grade: {final_grade}\n")
    print(f"Result: {result}\n")


def save_gradesheet_to_file(student_name, file_name, semester, semester_name, branch, subject_list, grades, total_credits, gpa, result, final_grade):
    """Save the gradesheet to a file."""
    filename = f"{file_name}_semester_{semester}_result.txt"
    with open(filename, "w") as file:
        file.write("                          PURBANCHAL UNIVERSITY\n")
        file.write("                   Office of The Examination Management\n")
        file.write("                            Biratnagar, Nepal\n")
        if "Fail" in result:
            file.write("\n                          Sorry! You have failed.\n")
        else:
            file.write(f"\n                    Congratulations! You have Passed.\n")
        file.write("                             Grade/Mark-Sheet\n\n")
        file.write(f"Name: {student_name}\n")
        file.write(f"Year/Semester: {semester_name}\n")
        file.write(f"Result of: BACHELOR IN {branch} ENGINEERING\n\n")
        file.write(f"{'S.N':<4} {'Subjects':<40} {'Credit Hour':<12} {'Mark/Grade Obtained'}\n")
        file.write("=" * 78 + "\n")
        for i, (subject, credit) in enumerate(subject_list.items(), 1):
            file.write(f"{i:<4} {subject:<40} {credit:<12} {grades[subject]}\n")
        file.write("=" * 78 + "\n")
        file.write(f"{'Grand Total':<45} {total_credits:<12} {gpa:.2f}\n")
        file.write(f"Final Grade: {final_grade}\n")
        file.write(f"\nResult: {result}\n")
    print(f"\nGradesheet saved as {filename}!\n")


def main():
    print("Welcome to the Grade and GPA Calculator!")
    calculate_gpa()

main()
