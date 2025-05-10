#!/usr/bin/env python3
import os
import glob

def normalize_line_endings(directory_path):
    """Convert all CRLF line endings to LF in Python files."""
    python_files = glob.glob(f"{directory_path}/**/*.py", recursive=True)
    
    for file_path in python_files:
        with open(file_path, "rb") as file:
            content = file.read()
        
        # Replace CRLF with LF
        content = content.replace(b"\r\n", b"\n")
        
        with open(file_path, "wb") as file:
            file.write(content)
        
        print(f"Normalized line endings in {file_path}")

if __name__ == "__main__":
    src_dir = os.path.join(os.getcwd(), "src")
    normalize_line_endings(src_dir)
    print("All files processed.")
