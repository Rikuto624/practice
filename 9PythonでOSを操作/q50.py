import os

directory_name = "xyz"

if os.path.isdir(directory_name):
    print(f"{directory_name} is a directory.")
else:
    print(f"{directory_name} is not a directory.")

print(os.path.exists(directory_name))
print(os.path.exists("q44.py"))