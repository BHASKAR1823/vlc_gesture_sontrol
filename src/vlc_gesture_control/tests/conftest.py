import os
import sys
from unittest.mock import MagicMock

# Add mock for pyautogui
# This needs to be added before any imports that might use pyautogui
try:
    import pyautogui
except ImportError:
    # Create a mock module for pyautogui
    mock_pyautogui = MagicMock()
    # Add any functions/attributes that might be used in tests
    mock_pyautogui.keyDown = MagicMock()
    mock_pyautogui.keyUp = MagicMock()
    mock_pyautogui.press = MagicMock()
    mock_pyautogui.hotkey = MagicMock()
    mock_pyautogui.KEYBOARD_KEYS = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'space', 'enter', 'tab', 'shift', 'ctrl', 'alt',
        'up', 'down', 'left', 'right'
    ]
    # Add the mock to sys.modules
    sys.modules['pyautogui'] = mock_pyautogui

# Add mock for win32gui if it can't be imported
try:
    import win32gui
except ImportError:
    # Create a mock module for win32gui
    mock_win32gui = MagicMock()
    # Add functions used in the code
    mock_win32gui.FindWindow = MagicMock(return_value=12345)
    mock_win32gui.GetWindowText = MagicMock(return_value="VLC Media Player")
    mock_win32gui.SetForegroundWindow = MagicMock()
    # Add the mock to sys.modules
    sys.modules['win32gui'] = mock_win32gui

# Rest of your conftest.py content 