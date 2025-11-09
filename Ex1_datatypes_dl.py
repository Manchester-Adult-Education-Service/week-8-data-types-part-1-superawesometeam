# Darrens code
# -------------------------------------------
# Exercise 1: Dictionaries & Data Types
# -------------------------------------------
# In this exercise, you'll work in groups of 2–3.
# You'll review data types you already know and learn about DICTIONARIES.
#
# WHAT ARE DICTIONARIES?
# Dictionaries store data in KEY-VALUE pairs.
# Think of a real dictionary: you look up a WORD (key) to find its DEFINITION (value).
#
# Example:
# student = {"name": "Alex", "age": 16, "grade": "A"}
#
# Access values using keys:
# print(student["name"])  # Output: Alex
# print(student["age"])   # Output: 16
#
# Add new items:
# student["hobby"] = "football"
#
# Each learner will build on the previous one's work.
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3 learners.
# Share the same GitHub Classroom repository.
#
# After each task:
# - Current learner: git add, commit, and push
# - Next learner: move to your computer and git pull origin main
#
# If you are in pairs: swap computers after each task.
# -------------------------------------------


# Task 1: Recording a Found Item
#DomatWheel

# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Recording a Found Item\n"
    + "-------------------------------------------")
# Imagine you're creating a system to track items that have been found.
# Let's start by recording one item.
#
# TODO:
# 1. Ask the user for: item name, colour, and location where it was found.
# 2. Create a dictionary called 'found_item' with keys: "name", "colour", "location"
# 3. Print the entire dictionary.
# 4. Print a message: "Recorded: <item name> (<colour>) found at <location>"
#
# Example:
# Enter item name: wallet
# Enter colour: black
# Enter location: train station
# Output:
# {'name': 'wallet', 'colour': 'black', 'location': 'train station'}
# Recorded: wallet (black) found at train station
#
# Write your code below:

# HINT: Create dictionary syntax is:
# my_dict = {"key1": value1, "key2": value2, "key3": value3}
found_item = {}
found_item ["Name"] = input("Item name: ")
found_item ["Colour"] = input("Item colour: ")
found_item ["Location"] = input("Location found: ")
print(found_item)
print(f"Recorded: {found_item["Name"].lower()} ({found_item["Colour"].lower()}) found at {found_item["Location"].lower()}.")
# Task 2: Multiple Found Items
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Multiple Found Items\n"
    + "-------------------------------------------")
# We need to track multiple items, not just one!
# Let's store several found items in a list.
#
# TODO:
# 1. Create an empty list called 'found_items'.
# 2. Add the 'found_item' dictionary from Task 1 to this list.
# 3. Ask the user if they want to add another item (yes/no).
# 4. If yes, ask for item name, colour, and location again.
#    Create a new dictionary and add it to the 'found_items' list.
# 5. Print the total number of items recorded.
# 6. Use a for loop to print each item in a readable format:
#    "Item <number>: <name> (<colour>) - Found at: <location>"
#
# Example:
# Add another item? yes
# Total items recorded: 2
# Item 1: wallet (black) - Found at: train station
# Item 2: phone (silver) - Found at: shopping centre
#
# Write your code below:

# HINT: To access dictionary values, use: dictionary_name["key_name"]
# Example: found_item["name"] gets the name value
count = 0
found_items = []
found_items .append(found_item)
count = (count +1)
add_property = input("Do you wish to add a new item: yes/no ".lower())
if add_property == "yes":
    new_item = {}
    new_item ["Name"] = input("Item name: ".lower())
    new_item ["Colour"] = input("Item colour: ".lower())
    new_item ["Location"] = input("Location found: ".lower())
    found_items .append(new_item)
    count = (count +1)
    print(f"Total items recorded: {count}")
    for item in found_items:
        print(f"Item 1: {found_item["Name"].lower()} ({found_item["Colour"].lower()}) found at {found_item["Location"].lower()}")
        print(f"Item 2: {new_item ["Name"].lower()} ({new_item["Colour"].lower()}) found at {new_item["Location"].lower()}")
        break
#    
# Task 3: Viewing All Records
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Viewing All Records\n"
    + "-------------------------------------------")
# We need to display all found items in a clear, easy-to-read format.
#
# TODO:
# 1. Print a header: "=== FOUND ITEMS RECORDS ==="
# 2. Check if the 'found_items' list is empty.
#    - If empty, print "No items recorded yet."
#    - If not empty, use a for loop to display all items.
# 3. For each item, print:
#    "Record <number>:"
#    "  Name: <name>"
#    "  Colour: <colour>"
#    "  Location: <location>"
#    (Print a blank line between each record)
# 4. Print the total count: "Total items: <number>"
#
# Example:
# === FOUND ITEMS RECORDS ===
# Record 1:
#   Name: wallet
#   Colour: black
#   Location: train station
#
# Record 2:
#   Name: phone
#   Colour: silver
#   Location: shopping centre
#
# Total items: 2
#
# Write your code below:

# HINT: When looping through a list of dictionaries:
# for item in found_items:
#     print(item["name"])  # Access the name from each dictionary
record = 1
print("==== FOUND ITEMS RECORDS ====")
print()
for d in found_items:
    name = d.get("Name", "")
if name == "":
    print("No items recorded yet!")
else:
    print(f"Record {record}:")
    for item in (found_items):
        print(f"Name: {item["Name"]}")
        print(f"Colour: {item["Colour"]}")
        print(f"Location: {item["Location"]}")
        print()
        print(f"Record {record +1}:")      
    print()
    print(f"Total items: {count}")
