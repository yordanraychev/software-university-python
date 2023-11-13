info_company = {}
command = input()
while command != "End":
    company, employee = command.split(" -> ")
    if company not in info_company.keys():
        info_company[company] = [employee]
    if employee not in info_company[company]:
        info_company[company].append(employee)
    command = input()
for company, employees in info_company.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
