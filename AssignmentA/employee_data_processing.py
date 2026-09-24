employees = [
   {"id": 1, "name": "John", "salary": 100000},
   {"id": 2, "name": "Jane", "salary": 120000},
   {"id": 3, "name": "Mike", "salary": 90000}
]

def print_employees(data): 
    print("All employees")

    for employees in data:
        print (employees)

print_employees(employees)

# 2.Find the highest-paid employee.

def highest_paid(data):
   highest = None
   for employee in data:
       salary = employee["salary"]
       if salary is not None and salary >= 0:
           if highest is None or salary > highest["salary"]:
               highest = employee
   return highest
print("\n Highest paid employee:", highest_paid(employees))

# 3. Calculate average salary.

def avg_salary(data):
    total = 0
    count = 0

    for employee in data:
        salary = employee["salary"]

        if salary is not None:
            total = total+salary
            count = count + 1

    if count == 0:
        return None
    return total / count

print("\n Average salary:", avg_salary(employees))

# 4.Return employees earning more than 100,000.

def high_earners(data):
    result = []

    for employee in data:
        salary = employee["salary"]

        if salary is not None and salary > 100000:
            result.append(employee)

    return result
  
print("\n Employees earn more than 100000 are: ", high_earners(employees))

# 5.Count employees.
def count_employees(data):
    return len(data)

print("\nNo of employees: ", count_employees(employees))

# Assignment B -String & Validation
# 7.Implement reverse_string("Hello") → "olleH". 

def reverse_text(text):
    return text[::-1]

print("Reversed String: ", reverse_text("Hello"))

# 8.Implement is_palindrome("madam") → True

def is_palindrome(text):
    return text == text[::-1]

print("\nIs madam palindrome - ", is_palindrome("madam"))

# 9.Validate that salary is numeric and non-negative.

def valid_salary(salary):
    if type(salary) not in (int, float):
        return False

    if salary < 0:
        return False

    return True

# 10.Handle invalid input without crashing. 

print("-500 is valid: ", valid_salary(-500))
print("'hundred' is valid: ", valid_salary("hundred"))
print("1500 is valid: ", valid_salary(1500))

# Day 1 Hard Scenario 

Employees_with_missingSalary = employees + [
    {"id": 4, "name": "Dini", "salary": None}
]

print("Avg with missing salary: ", avg_salary(Employees_with_missingSalary))

#  what should happen when the employee list is empty 

print("\nAvg with no employees: ", avg_salary([]))