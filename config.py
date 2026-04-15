from pathlib import Path

BASE_DIR = Path(__file__).parent

# Source folder to monitor
SOURCE_FOLDER = BASE_DIR / "sample_test_folder"

# Destination root folder inside the source folder
DESTINATION_ROOT = SOURCE_FOLDER / "Organized_Files"

# Optional features
RENAME_WITH_DATE = True
LOOP_MODE = False
LOOP_INTERVAL_SECONDS = 10

# File categories
FILE_CATEGORIES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Documents": [".doc", ".docx", ".txt", ".rtf", ".ppt", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}