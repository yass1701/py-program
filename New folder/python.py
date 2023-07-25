def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"

def main():
    try:
        marks = float(input("Enter the marks obtained by the student: "))
        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            print(f"The grade for {marks:.2f} marks is: {grade}")
        else:
            print("Invalid input. Marks should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
