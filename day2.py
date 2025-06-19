import os
import shutil
searchingpath=(r"D:\project")

newfilepath=os.path.join(r"D:\project\pdf")
newfile=os.makedirs(newfilepath, exist_ok=True)
os.chdir(searchingpath)
for file in (os.listdir(searchingpath)):
    if file.endswith(".pdf"):
        shutil.copy(file,newfilepath)
        print(f"Copied: {file}")
