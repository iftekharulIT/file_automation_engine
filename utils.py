from pathlib import Path
from datetime import datetime


def get_category(file_extension: str, category_map: dict) -> str:
    file_extension = file_extension.lower()
    for category, extensions in category_map.items():
        if file_extension in extensions:
            return category
    return "Others"


def generate_unique_filename(destination_folder: Path, filename: str) -> str:
    base_name = Path(filename).stem
    extension = Path(filename).suffix
    candidate = filename
    counter = 1

    while (destination_folder / candidate).exists():
        candidate = f"{base_name}_{counter}{extension}"
        counter += 1

    return candidate


def rename_with_date(filename: str) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{today}_{filename}"


def is_file_ready(file_path: Path) -> bool:
    try:
        with open(file_path, "rb"):
            return True
    except (PermissionError, OSError):
        return False