# File Organizer 🗂️

A command-line tool that automatically sorts and organizes files in any folder by file type or by date, built with Python.

## Features
- Organize files into categorized subfolders by file type
- Organize files into subfolders by last modified date
- Supports 40+ file extensions across 7 categories
- Displays every file move in real time
- Shows total count of moved files when done
- Creates subfolders automatically if they don't exist

## File Categories
| Category  | Extensions |
|-----------|-----------|
| Images    | .jpg .jpeg .png .gif .bmp .svg .webp .avif |
| Documents | .pdf .docx .doc .txt .xlsx .csv .pptx |
| Videos    | .mp4 .mov .avi .mkv .wmv |
| Audio     | .mp3 .wav .aac .flac .ogg |
| Archives  | .zip .rar .tar .gz .7z |
| Code      | .py .js .html .css .java .cpp .ts |
| Others    | anything not listed above |

## How to Use
Run the script:

python file_organizer.py

Then follow the prompts:

Would you like to sort files by type or by date?
Enter 'T' for type
Enter 'D' for date: T
Please enter the folder path: C:/Users/YourName/Downloads

## Example Output

Organize by type:

Moved: C:/Downloads/photo.jpg to C:/Downloads/Images
Moved: C:/Downloads/report.pdf to C:/Downloads/Documents
Moved: C:/Downloads/song.mp3 to C:/Downloads/Audio
Total: 3 moved files

Organize by date:

Moved: C:/Downloads/photo.jpg to C:/Downloads/2024-3
Moved: C:/Downloads/report.pdf to C:/Downloads/2024-4
Total: 2 moved files

## Requirements
- Python 3.x
- No external libraries needed
