#!/usr/bin/env python3
"""
Development installation script for VLC Gesture Control.

This script installs the package in development mode and all required dependencies.
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a command and return its exit code."""
    process = subprocess.run(command, capture_output=True, text=True)
    print(process.stdout)
    if process.stderr:
        print(process.stderr, file=sys.stderr)
    return process.returncode

def main():
    """Install the package and its dependencies."""
    print("Installing VLC Gesture Control in development mode...")
    
    # Install basic dependencies
    print("\nInstalling basic dependencies...")
    ret = run_command([
        sys.executable, "-m", "pip", "install", "--upgrade", "pip"
    ])
    if ret != 0:
        print("Failed to upgrade pip")
        return ret
    
    # Install development dependencies
    print("\nInstalling development dependencies...")
    ret = run_command([
        sys.executable, "-m", "pip", "install", 
        "black==25.1.0", "isort==5.13.2", "pytest==7.4.4", 
        "pytest-cov==4.1.0", "flake8==7.0.0"
    ])
    if ret != 0:
        print("Failed to install development dependencies")
        return ret
    
    # Install runtime dependencies
    print("\nInstalling runtime dependencies...")
    ret = run_command([
        sys.executable, "-m", "pip", "install",
        "pyautogui==0.9.54", "pywin32==306", "numpy==1.24.4",
        "opencv-python==4.8.1.78", "mediapipe==0.10.9"
    ])
    if ret != 0:
        print("Failed to install runtime dependencies")
        return ret
    
    # Install optional GPU dependencies if requested
    if len(sys.argv) > 1 and sys.argv[1] == "--with-gpu":
        print("\nInstalling optional GPU dependencies...")
        ret = run_command([
            sys.executable, "-m", "pip", "install",
            "tensorflow==2.12.0", "torch==2.0.1", "torchvision==0.15.2"
        ])
        if ret != 0:
            print("Failed to install GPU dependencies")
            return ret
    
    # Change to the package directory
    if os.path.exists("vlc_gesture_control"):
        os.chdir("vlc_gesture_control")
    
    # Install the package in development mode
    print("\nInstalling the package in development mode...")
    ret = run_command([
        sys.executable, "-m", "pip", "install", "-e", "."
    ])
    if ret != 0:
        print("Failed to install the package in development mode")
        return ret
    
    print("\nInstallation complete!")
    print("\nTo run the tests, use: pytest src/vlc_gesture_control/tests")
    print("To check code formatting, use: python check_formatting.py")
    print("To fix code formatting, use: python check_formatting.py --fix")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 