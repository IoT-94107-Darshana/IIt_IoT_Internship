import os
print("Current Directory:", os.getcwd())

print("Files in directory:", os.listdir())

folder_name = "demo_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created")
else:
    print("Folder already exists")
print("Does demo_folder exist?", os.path.exists(folder_name))
