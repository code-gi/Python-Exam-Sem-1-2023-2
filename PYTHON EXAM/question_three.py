w=input("enter your age")


def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
        return 'Invalid Input'

    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

# Test the function with a valid mark
valid_mark =  int(input("Enter your valid mark: "))
output_valid = grade_students(valid_mark)
print(f"The corresponding grade for a mark of {valid_mark} is: {output_valid}")





