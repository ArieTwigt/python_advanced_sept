import os

# get a list of the current files and folders
files_folders =  os.listdir()

# if the 'data' folder is not present yet, create it
if "data" not in files_folders:
    print("The 'data' folder not present yet, creating it...")
    os.mkdir("data")
else:
    print("The 'data' folder is already present")

# check if the license folder exists
files_folders_data = os.listdir("data")

if "license" not in files_folders_data:
    print("The 'license' folder not present yet, creating it...")
    os.makedirs("data/license")
else:
    print("The 'license' folder is already present")