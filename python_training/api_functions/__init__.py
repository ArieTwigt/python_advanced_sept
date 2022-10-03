import os

# get a list of the current files and folders
files_folders =  os.listdir()

# if the 'data' folder is not present yet, create it
if "data" not in files_folders:
    print("The 'data' folder not present yet, creating it...")
    os.mkdir("data")
else:
    print("The 'data' folder is already present")

