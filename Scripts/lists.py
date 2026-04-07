# ============================================================
# Lists in Python — Tutorial
# ============================================================


# ---- 1. CREATING A LIST ----
# A list is a collection of items in a single variable
# Lists are ordered, changeable, and allow duplicates

fruits = ["apple", "banana", "cherry", "mango", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # lists can hold any data type

print(fruits)
print(numbers)
print(mixed)


# ---- 2. ACCESSING ITEMS ----
# Items are accessed by index — starting at 0
# Negative indexes count from the end

print(fruits[0])    # apple  (first item)
print(fruits[1])    # banana (second item)
print(fruits[-1])   # orange (last item)
print(fruits[-2])   # mango  (second to last)


# ---- 3. SLICING ----
# Get a range of items using [start:end]
# end is not included

print(fruits[0:3])   # ['apple', 'banana', 'cherry']
print(fruits[2:])    # from index 2 to end
print(fruits[:3])    # from start to index 3
print(fruits[-2:])   # last 2 items


# ---- 4. CHANGING ITEMS ----
# Lists are mutable — you can change items after creation

fruits[1] = "grape"
print(fruits)   # banana is now grape


# ---- 5. ADDING ITEMS ----
# append() adds to the end
# insert() adds at a specific index

fruits.append("pineapple")
print(fruits)   # pineapple added to end

fruits.insert(1, "kiwi")
print(fruits)   # kiwi inserted at index 1


# ---- 6. REMOVING ITEMS ----
# remove() removes by value
# pop() removes by index (default: last item)
# del removes by index

fruits.remove("kiwi")
print(fruits)   # kiwi removed

fruits.pop()
print(fruits)   # last item removed

fruits.pop(0)
print(fruits)   # item at index 0 removed


# ---- 7. LOOPING THROUGH A LIST ----
# Use a for loop to iterate over each item

for fruit in fruits:
    print(fruit)

# Loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(index, fruit)


# ---- 8. USEFUL LIST METHODS ----

numbers = [5, 2, 8, 1, 9, 3]

print(len(numbers))     # 6      — number of items
print(sum(numbers))     # 28     — total of all items
print(max(numbers))     # 9      — highest value
print(min(numbers))     # 1      — lowest value
print(sorted(numbers))  # ascending order (does not modify original)

numbers.sort()
print(numbers)          # sorts the list in place

numbers.sort(reverse=True)
print(numbers)          # descending order

numbers.reverse()
print(numbers)          # reverses the list in place

print(numbers.count(5)) # counts how many times 5 appears
print(numbers.index(8)) # returns index of value 8


# ---- 9. CHECKING IF ITEM EXISTS ----

if "apple" in fruits:
    print("apple is in the list")
else:
    print("apple is not in the list")


# ---- 10. COMBINING LISTS ----
# Use + to combine or extend() to add one list to another

list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]

combined = list1 + list2
print(combined)

list1.extend(list2)
print(list1)


# ---- 11. COPYING A LIST ----
# Never copy a list with = — it creates a reference not a copy
# Use copy() or list() instead

original = [1, 2, 3]

wrong_copy = original       # both point to same list
right_copy = original.copy()

wrong_copy.append(99)
print(original)   # 99 is added — wrong!

right_copy.append(88)
print(original)   # unchanged — correct


# ---- 12. LIST COMPREHENSION ----
# A concise way to create a new list from an existing one
# Syntax: [expression for item in list]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numbers]
print(squares)   # [1, 4, 9, 16, 25 ...]

evens = [n for n in numbers if n % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10]


# ---- 13. NESTED LISTS ----
# A list can contain other lists (2D list)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0])      # [1, 2, 3] — first row
print(grid[1][2])   # 6         — row 1, column 2


# ---- 14. CLEARING A LIST ----

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)   # []