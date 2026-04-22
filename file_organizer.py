import os
import shutil
from datetime import datetime

# Maps file extensions to category folder names
def get_file_category(extension):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp",".avif"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts"],
    }

    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    return "Others"

# Organizes files into subfolders based on file type
def organize_by_type(folder_path):
    file_list = os.listdir(folder_path)
    moved = 0
    for files in file_list:
        full_path = os.path.join(folder_path, files)
        is_file = os.path.isfile(full_path)
        if is_file:
            extension = os.path.splitext(files)[1]
            category = get_file_category(extension)
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            moved_file = shutil.move(full_path, category_folder)
            moved += 1
            print(f"Moved: {moved_file} to {category_folder}")
    print(f"Total: {moved} moved files")

# Organizes files into subfolders based on last modified date (YYYY-M format)
def organize_by_date(folder_path):

    file_list = os.listdir(folder_path)
    moved = 0
    for files in file_list:
        full_path = os.path.join(folder_path, files)
        is_file = os.path.isfile(full_path)

        if is_file:
            timestamp = os.path.getmtime(full_path)
            year = datetime.fromtimestamp(timestamp).year
            month = datetime.fromtimestamp(timestamp).month
            date_folder_name = f"{year}-{month}"
            date_folder = os.path.join(folder_path, date_folder_name)
            os.makedirs(date_folder, exist_ok=True)
            moved_file = shutil.move(full_path, date_folder)
            moved += 1
            print(f"Moved: {moved_file} to {date_folder}")
    print(f"Total: {moved} moved files")


if __name__ == "__main__":
    choice = input('''Would you like to sort files by type or by date? 
    Enter 'T' for type
    Enter 'D' for date
    : ''').upper()
    user_folder_path = input("please enter the folder path: ")

    if choice == "T":
        organize_by_type(user_folder_path)
    elif choice == "D":
        organize_by_date(user_folder_path)
    else:
        print("Invalid input. Please enter 'T' or 'D'")




