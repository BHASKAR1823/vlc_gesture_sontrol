#!/usr/bin/env python3
"""
Run tests in a setup similar to the CI environment.
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a command and return its exit code."""
    print(f"\nRunning: {' '.join(command)}")
    process = subprocess.run(command, capture_output=False, text=True)
    return process.returncode

def main():
    """Run tests in a CI-like environment."""
    print("Running tests in a CI-like environment...")
    
    # Ensure we have pytest installed
    subprocess.run([
        sys.executable, "-m", "pip", "install", "pytest", "pytest-cov"
    ], check=True)
    
    # Run the tests
    ret = run_command([
        sys.executable, "-m", "pytest", 
        "src/vlc_gesture_control/tests",
        "--cov=src/vlc_gesture_control"
    ])
    
    return ret

if __name__ == "__main__":
    sys.exit(main()) 