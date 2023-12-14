def password_checker(input1, input2):
    number1 = len(input1)
    number2 = len(input2)

    if (input1 == input2) and (number1 == 0 and number2 == 0):
        return "Enter the password first!"
    elif (number1 > 0 and number2 == 0) or (number1 == 0 and number2 > 0):
        return "Enter the password first!"
    elif input1 == input2 and number1 == number2:
        return "Verified!"
    else:
        return "Password Mismatched"


# Example usage:
input1 = input("Enter Password: ")
input2 = input("Verify Password: ")

result = password_checker(input1, input2)
print(result)
 
