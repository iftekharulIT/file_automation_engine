import os
import random
from pathlib import Path

# Target folder
BASE_FOLDER = Path(r"C:\Users\Temp\OneDrive - Emmi\Desktop\file_automation_engine\sample_test_folder")

# File categories and extensions
FILE_TYPES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".png"],
    "Documents": [".txt", ".docx"],
    "Spreadsheets": [".csv", ".xlsx"],
    "Audio": [".mp3"],
    "Videos": [".mp4"],
    "Archives": [".zip"]
}

# Sample file name prefixes
FILE_NAMES = [
    "invoice", "report", "summary", "data", "image",
    "contract", "notes", "backup", "presentation", "analysis"
]

def create_dummy_file(file_path: Path):
    """
    Create a file with some dummy content.
    """
    try:
        with open(file_path, "w") as f:
            f.write("This is a sample file for automation testing.\n")
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")

def generate_files(num_files=20):
    BASE_FOLDER.mkdir(parents=True, exist_ok=True)

    for i in range(num_files):
        category = random.choice(list(FILE_TYPES.keys()))
        extension = random.choice(FILE_TYPES[category])
        name = random.choice(FILE_NAMES)

        filename = f"{name}_{i}{extension}"
        file_path = BASE_FOLDER / filename

        create_dummy_file(file_path)

    print(f"✅ {num_files} sample files created in {BASE_FOLDER}")

if __name__ == "__main__":
    generate_files(4000)