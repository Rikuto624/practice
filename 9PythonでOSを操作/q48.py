import os

for corDir, dirs, files in os.walk('.'):
    for file in files:
        full_path = os.path.join(corDir, file)
        file_name = os.path.basename(full_path)
        print(file_name)

