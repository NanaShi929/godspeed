
with open("./data.txt") as file:
    records = file.read().strip().split("\n")


for i in range(1, len(records)):
    values = records[i].split(",")
    print(values[3])


class Employee:
    def __init__(self, name, gender, location, salary):
        self.emp_name = name
        self.emp_gender = gender
        self.emp_location = location
        self.emp_salary = float(salary)


employeeList = []
for i in range(1, len(records)):
    values = records[i].split(",")
    empName     = values[0]
    empGender   = values[1]
    empLocation = values[2]
    empSalary   = values[3]


    empObject = Employee(empName, empGender, empLocation, empSalary)
    employeeList.append(empObject)


def totalSalaryToBePaid(emplist):
    totalSalary = 0
    for emp in emplist:
        totalSalary += emp.emp_salary
    return totalSalary


print(totalSalaryToBePaid(employeeList))

def salaryPerGender(emplist):
    salaryPerGender = {
    	"male":0,
    	"female":0
    }
    for emp in emplist:
        if emp.emp_gender == "male":
            salaryPerGender["male"]=
salaryPerGender["male"]+int(emp.emp_salary)
    return salaryPerGender
    
print(salaryPerGender(employeeList))
