1.Employee.objects.create(first_name="Demetre",last_name="gochelashvili",job_title="software engineer",salary=10000)
2.emp = Employee.objects.first()
emp.salary = emp.salary * 2 
emp.save()
3.Employee.objects.filter(job_title__icontains="software").count()
4.
5.