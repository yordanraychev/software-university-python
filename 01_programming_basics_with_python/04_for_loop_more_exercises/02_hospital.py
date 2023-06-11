days = int(input())
doctors = 7
treated = 0
untreated = 0

for p in range(1, days + 1):
    patients = int(input())

    if p % 3 == 0 and untreated > treated:
        doctors += 1

    if patients == doctors:
        treated += doctors
    elif patients < doctors:
        treated += patients
    elif patients > doctors:
        treated += doctors
        untreated += patients - doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
