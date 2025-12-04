#Name - Sree Parvati
#Date - 24/11/2025
#Title - Analysing and Reporting Student grades

#TASK 1

print("Welcome to the Gradebook Analyzer!")
print("This system is designed to simplify the process of evaluating student performance. It helps teachers enter marks, calculate grades, analyze overall results, and generate clear, organized reports. The Gradebook Analyzer ensures accuracy, saves time, and provides meaningful insights into each student's academic progress.")

#TASK 2

import csv

marks = {}   

print("Choose an option:")
print("1. Manual Entry")
print("2. Load from CSV file")

choice = input("Enter choice (1/2): ")

# OPTION 1: MANUAL ENTRY 
if choice == "1":
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        mark = float(input(f"Enter marks of {name}: "))
        marks[name] = mark
    
    print("\nData successfully saved!")
    print("Marks Dictionary:", marks)


elif choice == "2":
    filename = input("Enter CSV file name (with .csv extension): ").strip()

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            # Try to determine if there's a header. If first row contains non-numeric second field, treat it as header.
            try:
                first_row = next(reader)
            except StopIteration:
                print("CSV is empty.")
                first_row = None

            # If a header-like first row found, and its second column is not numeric, treat it as header and continue.
            if first_row is not None:
                treat_as_header = False
                if len(first_row) >= 2:
                    try:
                        float(first_row[1])
                        # first_row[1] is numeric -> treat as data row
                        name = first_row[0].strip()
                        mark = float(first_row[1])
                        marks[name] = mark
                    except ValueError:
                        # non-numeric -> assume header, skip it
                        treat_as_header = True
                else:
                    treat_as_header = True

                if treat_as_header:
                    pass

            
            for row in reader:
                if not row or len(row) < 2:
                    
                    continue
                name = row[0].strip()
                try:
                    mark = float(row[1])
                except ValueError:
                    print(f"Warning: couldn't parse marks for '{name}' (value: {row[1]}). Skipping row.")
                    continue
                marks[name] = mark

        print("\nCSV file successfully loaded!")
        print("Marks Dictionary:", marks)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. No data loaded.")
    except Exception as e:
        print("An unexpected error occurred while reading the CSV:", e)


else:
    print("Invalid choice. Exiting.")
    


#TASK 3


def calculate_average(marks_dict):
    """Return the average marks of all students."""
    if len(marks_dict) == 0:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    """Return the median of marks."""
    if len(marks_dict) == 0:
        return 0
    
    marks_list = sorted(marks_dict.values())
    n = len(marks_list)
    
    if n % 2 == 1:
        return marks_list[n // 2]                       
    else:
        return (marks_list[n//2 - 1] + marks_list[n//2]) / 2   


def find_max_score(marks_dict):
    """Return (name, score) for the student with the highest marks."""
    if len(marks_dict) == 0:
        return None
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]


def find_min_score(marks_dict):
    """Return (name, score) for the student with the lowest marks."""
    if len(marks_dict) == 0:
        return None
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

avg = calculate_average(marks)
median = calculate_median(marks)
topper_name, topper_score = find_max_score(marks)
lowest_name, lowest_score = find_min_score(marks)


print("\n=== ANALYSIS SUMMARY ===")
print(f"Average Score: {avg:.2f}")
print(f"Median Score : {median:.2f}")
print(f"Highest Score: {topper_name} ({topper_score})")
print(f"Lowest Score : {lowest_name} ({lowest_score})")



#TASK 4
grades = {} 

for name, mark in marks.items():

    
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"
    
    grades[name] = grade

grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for g in grades.values():
    grade_count[g] += 1

print("\n=== TASK 4: GRADE ASSIGNMENT & DISTRIBUTION ===")
print("Gradebook (Student : Grade)")
for name, grade in grades.items():
    print(f"{name}: {grade}")

print("\nGrade Distribution:")
for grade, count in grade_count.items():
    print(f"{grade}: {count} students")

#Task 5
passed_students = [name for name, mark in marks.items() if mark >= 40]
failed_students = [name for name, mark in marks.items() if mark < 40]

print("\n=== TASK 5: PASS / FAIL REPORT ===")

print(f"Total Passed Students: {len(passed_students)}")
print("Passed Students:", ", ".join(passed_students) if passed_students else "None")

print(f"\nTotal Failed Students: {len(failed_students)}")
print("Failed Students:", ", ".join(failed_students) if failed_students else "None")



#TASK 6

def print_results_table():
    """Print a formatted table of all students."""
    print("\n================ STUDENT RESULTS TABLE ================")
    print("Name\t\tMarks\tGrade")
    print("-------------------------------------------------------")

    for name, mark in marks.items():
        grade = grades[name]
        print(f"{name}\t\t{mark}\t{grade}")

    print("-------------------------------------------------------")

#Bonus
def export_to_csv():
    """Export the student results (Name, Marks, Grade) to a CSV file."""
    filename = input("Enter name for output CSV file (with .csv extension): ").strip()

    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Marks", "Grade"])  # header

            for name, mark in marks.items():
                writer.writerow([name, mark, grades[name]])

        print(f"\nResults successfully exported to '{filename}'")

    except Exception as e:
        print("Error while saving CSV:", e)


# USER LOOP MENU 

while True:
    print("\n====== MAIN MENU ======")
    print("1. Show Results Table")
    print("2. Show Analysis Summary (Task 3)")
    print("3. Show Grade Distribution (Task 4)")
    print("4. Show Pass/Fail Report (Task 5)")
    print("5. Export Results to CSV (Bonus)")
    print("6. Exit Program")


    choice = input("\nEnter your choice (1–5): ")

    if choice == "1":
        print_results_table()

    elif choice == "2":
        print("\n=== ANALYSIS SUMMARY ===")
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print(f"Total Students : {len(marks)}")
        print(f"Average Score  : {avg:.2f}")
        print(f"Median Score   : {median:.2f}")
        print(f"Highest Score  : {max_name} ({max_score})")
        print(f"Lowest Score   : {min_name} ({min_score})")

    elif choice == "3":
        print("\n=== GRADE DISTRIBUTION ===")
        for grade, count in grade_count.items():
            print(f"{grade}: {count} students")

    elif choice == "4":
        print("\n=== PASS / FAIL REPORT ===")
        print(f"Total Passed Students: {len(passed_students)}")
        print("Passed Students:", ", ".join(passed_students) if passed_students else "None")

        print(f"\nTotal Failed Students: {len(failed_students)}")
        print("Failed Students:", ", ".join(failed_students) if failed_students else "None")

    elif choice == "5":
        export_to_csv()
    
    elif choice == "6":
        print("\nExiting program... Goodbye!")
        break


    else:
        print("Invalid choice! Please select between 1–5.")






