# 📁 File Automation Engine

## Overview
A Python-based automation tool to monitor a folder and automatically organize files into structured categories such as PDFs, Images, Documents, Videos, and more. The project simulates real-world file management workflows to improve productivity and reduce manual effort.

## Features
- Monitors a source folder (sandbox/test environment)
- Detects file types based on extensions
- Automatically organizes files into categorized folders
- Handles duplicate filenames safely
- Logs file movements and errors
- Skips locked or partially downloaded files
- Optional file renaming based on date
- Supports batch processing and scalable file handling

## Tech Stack
Python, pathlib, shutil, os, logging

## Project Structure
file_automation_engine/
├── main.py
├── config.py
├── utils.py
├── generate_files.py
├── sample_test_folder/
│   ├── Organized_Files/
│   └── (generated files)
├── .gitignore
└── README.md

## How It Works
The script scans a source folder, identifies file types based on extensions, and moves them into structured category folders such as PDFs, Images, Documents, Videos, and others. It ensures duplicate filenames are handled and logs all actions for traceability.

## How to Run
Step 1: Generate sample files  
py generate_files.py  
Step 2: Run automation  
py main.py  

## Example Output
sample_test_folder/
└── Organized_Files/
    ├── PDFs/
    ├── Images/
    ├── Documents/
    ├── Spreadsheets/
    ├── Videos/
    ├── Audio/
    ├── Archives/
    └── Others/

## Business Use Cases
- Document management automation  
- Shared drive organization  
- Invoice and report sorting  
- File intake pipelines  
- Pre-processing for automation workflows  

## Data Safety
All testing is performed using synthetic files generated via script to avoid exposure of personal or business data. Repository structure is configured to prevent unintended file uploads.

## Key Learnings
- Python file handling and automation  
- Difference between os and shutil  
- Handling duplicates and file conflicts  
- Building scalable automation workflows  
- Testing using synthetic datasets  

## Author
Iftekharul Islam  
AI & Automation | Project Management | Data & Cloud