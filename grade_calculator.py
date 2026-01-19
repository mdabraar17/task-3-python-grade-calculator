# Program to calculate grade based on marks

# Taking marks input from the user
marks_input = input("Enter your marks (0 - 100): ")

try:
    # Convert input string to integer
    marks = int(marks_input)

    # Validate marks range
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")

    else:
        # Nested conditions to simulate real business rules
        if marks >= 90:
            grade = "A+"
            message = "Excellent performance!"
        elif marks >= 80 and marks < 90:
            grade = "A"
            message = "Very good job!"
        elif marks >= 70 and marks < 80:
            grade = "B"
            message = "Good effort!"
        elif marks >= 60 and marks < 70:
            grade = "C"
            message = "You passed. Keep improving!"
        elif marks >= 40 and marks < 60:
            grade = "D"
            message = "Needs improvement."
        else:
            grade = "F"
            message = "Failed. Better luck next time."

        # Display final result
        print("\n--- Grade Result ---")
        print("Marks:", marks)
        print("Grade:", grade)
        print("Message:", message)

except ValueError:
    # Handles non-numeric input
    print("Invalid input! Please enter numeric marks only.")
