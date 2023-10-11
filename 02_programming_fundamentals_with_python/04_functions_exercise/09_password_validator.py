def validation(password):
    errors_occurred = []
    if 6 > len(password) or len(password) > 10:
        errors_occurred.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors_occurred.append("Password must consist only of letters and digits")
    digit_count = 0
    for digit in password:
        if digit.isdigit():
            digit_count += 1
    if digit_count < 2:
        errors_occurred.append("Password must have at least 2 digits")
    return errors_occurred


given_password = input()
expected_errors = validation(given_password)
if not expected_errors:
    print("Password is valid")
else:
    print("\n".join(expected_errors))
