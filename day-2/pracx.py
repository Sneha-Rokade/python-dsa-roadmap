for i in range(2,6,2):
    print(i)

name = "Alex"

for char in name:
    print(char)

skills = ["Python", "SQL", "AWS"]

for skill in skills:
    print(skill)

total = 0

for i in range(1, 6):
    total += i
print(total)

numbers = [10,20,25,45,15,60]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)

def greet(name="Alex"):
    print(f"Hello {name}")

greet()
greet("David")

def add(a, b):
    result = a + b
    print(result)

add(10,20)


def addR(a, b):
    return a + b

result = addR(52, 26)
print("addition of two numbers:", result)

def intro(name, age):

    print(f"Name:  {name}")
    print(f"Age:  {age}")

intro("Alex", 25)

def employee(name, role):
    print(name)
    print(role)

employee(role="Engineer", name="Alex")

def calculate_salary(hours, rate):
    
    return hours * rate

salary = calculate_salary(160, 500)

print(salary)

def generate_email(name):

    return f"{name.lower()}@company.com"

print(generate_email("Alex"))


