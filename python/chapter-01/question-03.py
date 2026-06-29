import os

# Specific directory you want to list
directory_path = './'

# List All files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)