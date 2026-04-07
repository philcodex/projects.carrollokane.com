"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

print("Hello, World!")

name = "Phil"
age = 35
is_engineer = True

skills = ["python", "api", "linux"]

user = {
    "name": "Phil",
    "role": "support engineer"
}

print("Hello", name)
print(f"{name} works as a {user['role']}")
print(f"{name} has skills: {', '.join(skills)}")

service = "Stripe API"
status = "UP"

print(f"{service} status: {status}")

status = 200

if status == 200:
    print("OK")
else:
    print("Error")

for i in range(5):
    print(i)

user = {"name": "Phil", "role": "Engineer"}
for key, value in user.items():
    print(key, value)

status_codes = [200,200,500,404,200]

errors = 0

for code in status_codes:
    if code != 200:
        errors += 1
print("Errors:", errors)

numbers = [1,2,3,4,5]
squared = [n*n for n in numbers]
print(squared)



