import os

file_name = "q50.py"

if os.path.isfile(file_name):
    print(f"{file_name} is a file.")
else:
    print(f"{file_name} is not a file.")

