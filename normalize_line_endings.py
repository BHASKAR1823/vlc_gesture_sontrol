#!/usr/bin/env python3
"""
Normalize line endings in Python files to LF.
This script converts Windows CRLF line endings to Unix-style LF line endings
in all Python files in the src directory.
"""

import os
import glob

def normalize_line_endings(file_path):
    """Convert CRLF to LF in the given file."""
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # Convert CRLF to LF
    content = content.replace(b'\r\n', b'\n')
    
    with open(file_path, 'wb') as f:
        f.write(content)
    
    print(f"Normalized line endings in {file_path}")

def main():
    """Find and normalize Python files."""
    for py_file in glob.glob('src/**/*.py', recursive=True):
        normalize_line_endings(py_file)
    
    print("All Python files normalized.")

if __name__ == "__main__":
    main() 