from pathlib import Path
import os
import shutil

def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    print("\n📂 Files and Folders:")
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")
    print()

def createfile():
    try:
        readfileandfolder()
        name = input("📄 Enter the file name to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("📝 What do you want to write in this file? ")
                fs.write(data)
            print("✅ File created successfully!")
        else:
            print("⚠️ This file already exists.")
    except Exception as err:
        print(f"❌ Error: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("📖 Enter the file name to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                print("\n📄 File Contents:\n")
                print(fs.read())
            print("✅ Read successfully.")
        else:
            print("⚠️ The file does not exist.")
    except Exception as err:
        print(f"❌ Error: {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("✏️ Enter the file name to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1️⃣ Rename\n2️⃣ Overwrite Content\n3️⃣ Append Content")
            res = int(input("Choose an option: "))
            if res == 1:
                name2 = input("🆕 Enter new file name: ")
                p.rename(Path(name2))
                print("✅ File renamed successfully.")
            elif res == 2:
                with open(p, "w") as fs:
                    data = input("📝 New content (overwrite): ")
                    fs.write(data)
                print("✅ File content overwritten.")
            elif res == 3:
                with open(p, "a") as fs:
                    data = input("➕ Content to append: ")
                    fs.write(data)
                print("✅ Content appended.")
        else:
            print("⚠️ File not found.")
    except Exception as err:
        print(f"❌ Error: {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("🗑️ Enter the file name to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("✅ File deleted successfully.")
        else:
            print("⚠️ File not found.")
    except Exception as err:
        print(f"❌ Error: {err}")

def createfolder():
    try:
        readfileandfolder()
        name = input("📁 Enter the folder name to create: ")
        p = Path(name)
        if not p.exists():
            p.mkdir()
            print("✅ Folder created successfully.")
        else:
            print("⚠️ This folder already exists.")
    except Exception as err:
        print(f"❌ Error: {err}")

def deletefolder():
    try:
        readfileandfolder()
        name = input("🗑️ Enter the folder name to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("✅ Folder deleted successfully.")
        else:
            print("⚠️ Folder not found.")
    except Exception as err:
        print(f"❌ Error: {err}")

# Menu
print("\n📌 Welcome to File & Folder Manager CLI\n")
print("1️⃣ Create File")
print("2️⃣ Read File")
print("3️⃣ Update File")
print("4️⃣ Delete File")
print("5️⃣ Create Folder")
print("6️⃣ Delete Folder\n")

try:
    choice = int(input("🔢 Enter your choice: "))
    match choice:
        case 1: createfile()
        case 2: readfile()
        case 3: updatefile()
        case 4: deletefile()
        case 5: createfolder()
        case 6: deletefolder()
        case _: print("❌ Invalid choice.")
except ValueError:
    print("❌ Please enter a valid number.")
