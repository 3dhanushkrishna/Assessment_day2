name = []
age = []
designation = []
salary = []
n = int(input("Number of Employee:"))
for i in range(n):
    name1 = input("Employee name:")
    age1 = input("Employee age:")
    designation1 = input("Employee Designation:")
    salary1 = input("Employee salary:")
    name.append(name1)
    age.append(age1)
    designation.append(designation1)
    salary.append(salary1)
print(name)
print(age)
print(designation)
print(salary)