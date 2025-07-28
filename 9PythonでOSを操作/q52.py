import os

for corDir, dirs, files in os.walk('.'):
    for file in files:
        full_path = os.path.join(corDir, file)
        print(full_path)

