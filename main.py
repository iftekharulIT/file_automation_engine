import logging
import shutil
import time
from pathlib import Path

from config import (
    SOURCE_FOLDER,
    DESTINATION_ROOT,
    FILE_CATEGORIES,
    RENAME_WITH_DATE,
    LOOP_MODE,
    LOOP_INTERVAL_SECONDS,
)
from utils import (
    get_category,
    generate_unique_filename,
    rename_with_date,
    is_file_ready,
)

logging.basicConfig(
    filename="file_mover.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_category_folders() -> None:
    print("Creating destination root:", DESTINATION_ROOT)
    DESTINATION_ROOT.mkdir(parents=True, exist_ok=True)

    all_categories = list(FILE_CATEGORIES.keys()) + ["Others"]
    for category in all_categories:
        folder_path = DESTINATION_ROOT / category
        folder_path.mkdir(parents=True, exist_ok=True)
        print("Created/checked folder:", folder_path)

def process_files() -> None:
    print("Scanning source folder:", SOURCE_FOLDER)

    for item in SOURCE_FOLDER.iterdir():
        print("Found item:", item.name)

        if not item.is_file():
            print("Skipped (not a file):", item.name)
            continue

        if DESTINATION_ROOT in item.parents:
            print("Skipped (already organized):", item.name)
            continue

        if item.suffix.lower() in [".crdownload", ".part", ".tmp"]:
            print("Skipped temp file:", item.name)
            continue

        try:
            if not is_file_ready(item):
                print("Skipped locked file:", item.name)
                logging.warning(f"Skipped locked or busy file: {item.name}")
                continue

            category = get_category(item.suffix, FILE_CATEGORIES)
            destination_folder = DESTINATION_ROOT / category

            new_filename = item.name
            if RENAME_WITH_DATE:
                new_filename = rename_with_date(new_filename)

            new_filename = generate_unique_filename(destination_folder, new_filename)
            destination_path = destination_folder / new_filename

            shutil.move(str(item), str(destination_path))
            print(f"Moved: {item.name} -> {destination_path}")
            logging.info(f"Moved: {item.name} -> {destination_path}")

        except Exception as e:
            print(f"Failed to move {item.name}: {e}")
            logging.error(f"Failed to move {item.name}: {e}")

def main() -> None:
    print("=== SCRIPT STARTED ===")
    print("SOURCE_FOLDER =", SOURCE_FOLDER)
    print("SOURCE EXISTS =", SOURCE_FOLDER.exists())
    print("DESTINATION_ROOT =", DESTINATION_ROOT)
    print("LOOP_MODE =", LOOP_MODE)

    create_category_folders()
    logging.info("File Automation Engine started.")

    if LOOP_MODE:
        while True:
            process_files()
            time.sleep(LOOP_INTERVAL_SECONDS)
    else:
        process_files()

if __name__ == "__main__":
    main()