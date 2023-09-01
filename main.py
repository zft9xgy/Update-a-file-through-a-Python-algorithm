# This script check whether the allow list contains any IP addresses identified on the remove list. 
# If so, you should remove those IP addresses from the file containing the allow list.

# This line of code reset the allow_list.txt
import os
os.system("sh reset.sh")

# Assign the filename to a variable

import_file = "allow_list.txt"

# Given by exercise.
# List of IP addresses that are no longer allowed to access restricted information. 

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Create reader for allow list text
# Open document and read it. 
with open(import_file,"r") as file:
  allow_list_file = file.read()

# Create a allow_list from the allow_list_file using the separator "\n"
allow_list = allow_list_file.split("\n")

# Print allow list original
# Code made to test the execution, left commented here for academic reasons.
# print("Original allow list:", allow_list)

# First loop other remove_list and take each IP as remove_ip
# If remove_ip is in allow_list, remove. Else, do nothing.

for remove_ip in remove_list:
  if remove_ip in allow_list:
    allow_list.remove(remove_ip)


# Print new allow list
# Code made to test the execution, left commented here for academic reasons.
# print("After checking allow list:", allow_list)

# Write new allow_list into the file allow_list.txt
# By this point of exec file is close but we can check here
# print(file.closed)

# file.write only accepts string as argument so we need to parse list to string
parse_allow_list = "\n".join(allow_list)

# Open allow_list in write mode 
with open(import_file,"w") as file:
  file.write(parse_allow_list)



