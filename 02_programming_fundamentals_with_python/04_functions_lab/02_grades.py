def grades(g):
    if 2.00 <= g <= 2.99:
        return "Fail"
    elif 3.00 <= g <= 3.49:
        return "Poor"
    elif 3.50 <= g <= 4.49:
        return "Good"
    elif 4.50 <= g <= 5.49:
        return "Very Good"
    elif 5.50 <= g <= 6.00:
        return "Excellent"


grade = float(input())
result = grades(grade)
print(result)
