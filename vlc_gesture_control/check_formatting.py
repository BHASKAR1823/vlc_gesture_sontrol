#!/usr/bin/env python3
"""
Check and fix code formatting with Black and isort.
This script checks and formats Python code to meet style guidelines.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command):
    """Run a command and return its exit code and output."""
    process = subprocess.run(command, capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr

def main():
    """Check and fix formatting with Black and isort."""
    src_dir = Path("src")
    
    if not src_dir.exists():
        print(f"Error: {src_dir} directory does not exist.")
        return 1
    
    # Check if tools are installed
    print("Checking for required tools...")
    black_returncode, _, _ = run_command(["black", "--version"])
    isort_returncode, _, _ = run_command(["isort", "--version"])
    
    if black_returncode != 0:
        print("Black not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "black==25.1.0"])
    
    if isort_returncode != 0:
        print("isort not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "isort==5.13.2"])
    
    # Fix mode (format the code)
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        print("\nFixing code formatting...")
        
        # Run Black to format code
        print("\nRunning Black formatter...")
        returncode, stdout, stderr = run_command(["black", str(src_dir)])
        print(stdout)
        if stderr:
            print(stderr, file=sys.stderr)
        
        # Run isort to sort imports
        print("\nRunning isort to sort imports...")
        returncode, stdout, stderr = run_command(["isort", "--profile", "black", str(src_dir)])
        print(stdout)
        if stderr:
            print(stderr, file=sys.stderr)
        
        print("\nCode formatting completed.")
    
    # Check mode (default)
    else:
        print("\nChecking code formatting...")
        errors = False
        
        # Check Black formatting
        print("\nChecking Black formatting...")
        returncode, stdout, stderr = run_command(["black", "--check", str(src_dir)])
        if returncode != 0:
            errors = True
            print(stdout)
            if stderr:
                print(stderr, file=sys.stderr)
        else:
            print("Black formatting: OK")
        
        # Check isort
        print("\nChecking import sorting...")
        returncode, stdout, stderr = run_command(["isort", "--check-only", "--profile", "black", str(src_dir)])
        if returncode != 0:
            errors = True
            print(stdout)
            if stderr:
                print(stderr, file=sys.stderr)
        else:
            print("Import sorting: OK")
        
        if errors:
            print("\nSome formatting checks failed. Run with --fix to automatically fix these issues.")
            return 1
        else:
            print("\nAll formatting checks passed!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 