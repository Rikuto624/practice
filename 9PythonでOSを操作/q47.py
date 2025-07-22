import os

for corDir, dirs, files in os.walk('.'):
    for file in files:
        full_path = os.path.join(corDir, file)
        abs_path = os.path.abspath(full_path)
        print(abs_path)

print(os.path.abspath("./q45.py"))