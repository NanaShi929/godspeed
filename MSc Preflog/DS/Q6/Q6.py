class Employee:
    def __init__(self, name, gender, location, salary):
        self.name = name
        self.gender = gender.lower()
        self.location = location
        self.salary = int(salary)

class State:
    def __init__(self, name):
        self.name = name
        self.employeeList = []

    def add_employee(self, employee):
        self.employeeList.append(employee)

    def total_salary(self):
        return sum(emp.salary for emp in self.employeeList)

class Organization:
    def __init__(self):
        self.states = {}

    def add_employee(self, employee):
        loc = employee.location
        if loc not in self.states:
            self.states[loc] = State(loc)
        self.states[loc].add_employee(employee)

    def total_salary_by_state(self):
        return {state: self.states[state].total_salary() for state in self.states}

    def gender_based_salary(self):
        male_salary = 0
        female_salary = 0
        for state in self.states.values():
            for emp in state.employeeList:
                if emp.gender == "male":
                    male_salary += emp.salary
                elif emp.gender == "female":
                    female_salary += emp.salary
        return {"male salary": male_salary, "female salary": female_salary}


# === File reading and processing ===

with open("employee.txt") as file:
    records = file.read().strip().split("\n")

org = Organization()

for i in range(1, len(records)):  # assuming row 0 is header
    if not records[i].strip():
        continue
    name, gender, location, salary = [x.strip() for x in records[i].split(",")]
    emp = Employee(name, gender, location, salary)
    org.add_employee(emp)

# === Output ===

'''print("Total Salary by State:")
for state, total in org.total_salary_by_state().items():
    print(f"{state}: {total}")
'''

'''print("\nGender-wise Salary Distribution:")
print(org.gender_based_salary())'''
'''
for state_name, state_obj in org.states.items():
    for emp in state_obj.employeeList:
        print(f"Name: {emp.name}, Gender: {emp.gender}, State: {emp.location}, Salary: {emp.salary}")
'''
print(org.states.keys())

'''print("\nTotal States in Organization:", len(org.states))
print("States Present in Organization:")
for state_name in org.states.keys():
    print("-", state_name)
    '''