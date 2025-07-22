import os
for corDir, dirs, files in os.walk('.'):
    for file in files:
        print(f"{corDir}/{file}")
        print(corDir)
        print(file)