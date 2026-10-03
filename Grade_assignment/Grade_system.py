# Grade System using a Function
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

# Get marks from the user
try: 
    mark = float(input("Enter your mark (0-100): "))

    #Valid mark range
    if mark < 0 or mark > 100:
        print("Please enter a valid mark between 0 and 100.")
    else:
        # Call the function
        grade = calculate_grade(mark)

        # Display the result
        print("Your Grade is:", grade)

except ValueError:
    print("Invalid input! Please enter a numeric value for the mark.")