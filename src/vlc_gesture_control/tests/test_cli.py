"""
Tests for the CLI module
"""

import sys
import unittest
from unittest.mock import patch, MagicMock

from vlc_gesture_control.cli import main


class TestCLI(unittest.TestCase):
    """Test cases for the CLI module"""

    @patch('vlc_gesture_control.cli.version')
    @patch('argparse.ArgumentParser.parse_args')
    @patch('vlc_gesture_control.cli.cpu_main')
    def test_main_cpu_mode(self, mock_cpu_main, mock_parse_args, mock_version):
        """Test CLI in CPU mode calls the correct function"""
        # Setup
        mock_version.return_value = "1.0"
        mock_args = MagicMock()
        mock_args.mode = "cpu"
        mock_args.camera = 0
        mock_args.debug = False
        mock_parse_args.return_value = mock_args
        
        # Call function
        main()
        
        # Assertions
        mock_cpu_main.assert_called_once_with(camera_index=0, debug=False)
        
    @patch('vlc_gesture_control.cli.version')
    @patch('argparse.ArgumentParser.parse_args')
    @patch('vlc_gesture_control.cli.gpu_main')
    def test_main_gpu_mode(self, mock_gpu_main, mock_parse_args, mock_version):
        """Test CLI in GPU mode calls the correct function"""
        # Setup
        mock_version.return_value = "1.0"
        mock_args = MagicMock()
        mock_args.mode = "gpu"
        mock_args.camera = 1
        mock_args.debug = True
        mock_parse_args.return_value = mock_args
        
        # Call function
        main()
        
        # Assertions
        mock_gpu_main.assert_called_once_with(camera_index=1, debug=True)
        
    @patch('vlc_gesture_control.cli.version')
    @patch('argparse.ArgumentParser.parse_args')
    @patch('sys.exit')
    def test_main_import_error_gpu(self, mock_exit, mock_parse_args, mock_version):
        """Test CLI handles ImportError for GPU mode gracefully"""
        # Setup
        mock_version.return_value = "1.0"
        mock_args = MagicMock()
        mock_args.mode = "gpu"
        mock_args.debug = False
        mock_parse_args.return_value = mock_args
        
        # Create a side effect that raises ImportError
        def side_effect(*args, **kwargs):
            from_list = args[0] if args else kwargs.get('fromlist', None)
            if from_list and 'gpu_main' in from_list:
                raise ImportError("GPU dependencies not installed")
            return MagicMock()
            
        with patch('builtins.__import__', side_effect=side_effect):
            # Call function
            with patch('sys.stdout'):  # Suppress stdout for cleaner test output
                main()
            
            # Assertions
            mock_exit.assert_called_once_with(1)
            
    @patch('vlc_gesture_control.cli.version')
    @patch('argparse.ArgumentParser.parse_args')
    @patch('sys.exit')
    def test_main_keyboard_interrupt(self, mock_exit, mock_parse_args, mock_version):
        """Test CLI handles KeyboardInterrupt gracefully"""
        # Setup
        mock_version.return_value = "1.0"
        mock_args = MagicMock()
        mock_args.mode = "cpu"
        mock_args.debug = False
        mock_parse_args.return_value = mock_args
        
        # Create a side effect that raises KeyboardInterrupt
        def side_effect(*args, **kwargs):
            raise KeyboardInterrupt()
            
        with patch('vlc_gesture_control.cli.cpu_main', side_effect=side_effect):
            # Call function
            with patch('sys.stdout'):  # Suppress stdout for cleaner test output
                main()
            
            # Assertions
            mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main() 