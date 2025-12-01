from employees.models import Employee

first_employee = Employee.objects.first()
if first_employee:
    first_employee.salary *= 3
    first_employee.save()
    print(f"Tripled salary for {first_employee.first_name} {first_employee.last_name}: {first_employee.salary}")
else:
    print("No employees found to triple salary.")

software_count = Employee.objects.filter(job_title__icontains="software").count()
print(f"Number of employees with 'software' in job title: {software_count}")

deleted_count, _ = Employee.objects.filter(job_title="Accountant").delete()
print(f"Number of 'Accountant' employees deleted: {deleted_count}")

high_salary_employees = Employee.objects.filter(salary__gt=6000).order_by("first_name")
print("Employees with salary > 6000 (sorted by name):")
for emp in high_salary_employees:
    print(f"- {emp.first_name} {emp.last_name}: {emp.salary}")