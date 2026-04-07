for i in range(12):
    print(i)

n = int(input("number: "))

for i in range(n):
    print("hello, world")

tools = ["Postman", "Wireshark", "Splunk"]

for tool in tools:
    print(tool)

for i in range(5):
    print("hello") # prints hello 5 times

for i in range(5):
    print(i) # prints numbers from 0 to 4

for i in range(5):
    print("Phil")

for i in range(1, 11):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print(fruit)

skills = ['Python', 'APIs', 'Writing', 'Cloud', 'Rigor']
for s in skills:
    print(s)

num = [1, 2, 3, 4, 5]
for n in num:
    print(n)

char = ["P", "h", "i", "l"]
for c in char:
    print(c)

word = "Stripe"
count = 0

# Loop through each character in the word
for letter in word:
    count = count + 1
print(count)

word = "Stripe"
print(len(word))

numbers = [1, 2, 3, 4, 5]

for num in numbers: 
    if num % 2 == 0: 
        print(num, "is even")