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


found_item = {
  
 }
found_item["name"] = input("Please enter the type of item found: ")
found_item["colour"] = input("Please enter the colour of the item found: ")
found_item["location"] = input("Please enter the location where the item was found: ")

print(found_item)

# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Task 1"
# git push origin main
# Next learner: git pull origin main
# -------------------------------------------


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



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Task 2"
# git push origin main
# Next learner: git pull origin main
# -------------------------------------------


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



# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Task 3"
# git push origin main
# Next learner: git pull origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Search by Item Name
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Search by Item Name\n"
    + "-------------------------------------------")
# Users need to search for specific items quickly.
#
# TODO:
# 1. Ask the user: "Enter item name to search for:"
# 2. Create a variable called 'found' and set it to False.
# 3. Use a for loop to check each item in 'found_items'.
#    If the item's name matches the search (use .lower() for both to ignore case):
#    - Set 'found' to True
#    - Print the full details of that item
# 4. After the loop, if 'found' is still False, print "No items found with that name."
#
# Example:
# Enter item name to search for: wallet
# Found: wallet (black) - Found at: train station
#
# HINT: Use item["name"].lower() == search_term.lower()
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Extension 1"
# git push origin main
# Next learner: git pull origin main
# -------------------------------------------


# Extension 2: Data Validation
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2: Data Validation\n"
    + "-------------------------------------------")
# We need to make sure users enter valid data!
#
# TODO:
# 1. Ask for a new item name, colour, and location.
# 2. BEFORE creating the dictionary, check:
#    - Item name is not empty (length > 0)
#    - Colour is not empty (length > 0)
#    - Location is not empty (length > 0)
# 3. If ANY field is empty, print "Error: All fields must be filled in!" and DON'T add the item.
# 4. If all fields are valid:
#    - Create the dictionary
#    - Add it to 'found_items'
#    - Print "Item added successfully!"
# 5. Print the updated total count.
#
# Example (invalid):
# Enter item name: 
# Error: All fields must be filled in!
#
# Example (valid):
# Item added successfully!
# Total items: 3
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Extension 2"
# git push origin main
# Next learner: git pull origin main
# -------------------------------------------


# Extension 3: Adding Item IDs
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3: Adding Item IDs\n"
    + "-------------------------------------------")
# Each found item should have a unique reference number for easy tracking.
#
# TODO:
# 1. Create a variable called 'next_id' and set it to 1.
# 2. Go through each item in 'found_items' using a for loop.
# 3. Add an "id" key to each dictionary with the current 'next_id' value.
# 4. Increase 'next_id' by 1 after each item.
# 5. Display all items again, but this time include the ID:
#    "ID: <id> | Name: <name> | Colour: <colour> | Location: <location>"
# 6. Update your search function from Extension 1 to also show the ID when found.
#
# Example:
# ID: 1 | Name: wallet | Colour: black | Location: train station
# ID: 2 | Name: phone | Colour: silver | Location: shopping centre
#
# HINT: You can add new keys to existing dictionaries like this:
# item["id"] = next_id
#
# Write your code below:




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# git add Ex1_datatypes.py
# git commit -m "Completed Extension 3"
# git push origin main
# Check GitHub to confirm your group's final version appears.
# -------------------------------------------
