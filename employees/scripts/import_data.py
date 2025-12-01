import json
from employees.models import Employee

def run():
    
    with open('employees/scripts/employees.json', 'r') as f:
        data = json.load(f)

    
    for item in data:
        Employee.objects.create(
            first_name=item["first_name"],
            last_name=item["last_name"],
            salary=item["salary"],
        )

    print("Data imported!")
