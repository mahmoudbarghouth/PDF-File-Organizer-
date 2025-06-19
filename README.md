# PDF-File-Organizer-
This Python script scans a specific directory and copies all `.pdf` files into a separate subfolder.

---

##  Features

- Automatically finds all `.pdf` files in the given directory
- Creates a subfolder (named `pdf`) to store the copied files
- Avoids duplication errors using `exist_ok=True`
- Displays the names of copied files

---

##  How It Works

1. Set the base path in the variable `searchingpath`
2. A folder named `pdf` is created inside that path (if it doesn't exist)
3. The script loops through all files
4. If a file ends with `.pdf`, it is copied to the `pdf` folder
