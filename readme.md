# VLC Gesture Control

A computer vision application that allows you to control VLC media player using hand gestures.

![VLC Gesture Control Demo](path_to_demo_image.jpg) <!-- You can add a demo image/gif later -->

## Features

- Control VLC media player without touching your keyboard/mouse
- Support for both CPU and GPU processing
- Palm-facing detection to prevent accidental triggers
- Fast-forward and rewind functionality with repeated gestures
- Real-time performance monitoring with FPS display

### Supported Gestures

| Gesture | Action |
|---------|--------|
| All five fingers up | Play/Pause |
| Index finger only | Volume Up |
| Thumb + Index finger | Volume Down |
| Index + Middle fingers | Forward 10 seconds (Fast-forward when repeated) |
| Thumb + Index + Middle fingers | Backward 10 seconds (Fast-rewind when repeated) |
| Index + Middle + Ring fingers | Toggle Subtitles |
| All fingers except thumb | Change Audio Track |
| Left hand thumb only (pointing right) | Next Video |
| Right hand thumb only (pointing left) | Previous Video |

## Requirements

- Python 3.7+
- VLC Media Player
- Webcam

### Dependencies

```
opencv-python
mediapipe
pyautogui
pywin32
numpy
pytest (for testing)
black (for code formatting)
isort (for import sorting)
tensorflow (for GPU version)
torch (for GPU version)
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/vlc-gesture-control.git
cd vlc-gesture-control
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Open VLC media player and start playing a video
2. Run the application with either CPU or GPU mode:

```bash
# For CPU mode
python vlc_m_cpu.py

# For GPU mode (if supported by your hardware)
python vlc_m_gpu.py
```

3. Position your hand in front of the webcam and use the gestures to control VLC

4. Press 'q' to quit the application

## How It Works

The application uses MediaPipe's hand tracking to detect hand landmarks in real-time. It analyzes the configuration of fingers to recognize specific gestures, then sends the corresponding keyboard commands to VLC. The system includes a consistency check that requires a gesture to be detected multiple times before triggering an action, which prevents accidental commands.

The application also checks if your palm is facing the camera, ignoring gestures when the back of your hand is visible. This allows you to adjust your hair or move around without accidentally triggering commands.

For directional gestures like next/previous video navigation, the application uses thumb-only gestures that are specific to which hand is being used (left hand thumb for next, right hand thumb for previous), making the controls more intuitive.

## Development

The codebase includes two versions:
- `vlc_m_cpu.py`: Optimized for CPU processing
- `vlc_m_gpu.py`: Utilizes GPU acceleration for improved performance

### Code Formatting and Quality

We maintain code quality using Black and isort. You can check and fix code formatting using the included script:

```bash
# Check code formatting
python check_formatting.py

# Fix code formatting issues automatically
python check_formatting.py --fix
```

### Testing

To run the test suite:

```bash
# Run all tests
pytest src/vlc_gesture_control/tests

# Run tests with coverage report
pytest --cov=src/vlc_gesture_control src/vlc_gesture_control/tests
```

The project includes GitHub Actions workflows that automatically check code formatting and run tests on each pull request and push to main.

Check [suggestions.md](suggestions.md) for future development ideas and potential improvements.

## Troubleshooting

- **VLC not detected**: Make sure VLC is running and a video is playing before starting the application
- **Low frame rate**: Try the GPU version if your hardware supports it, or reduce your webcam resolution
- **Gestures not recognized**: Ensure proper lighting and position your hand clearly in front of the camera

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MediaPipe](https://developers.google.com/mediapipe) for hand tracking technology
- [VideoLAN](https://www.videolan.org) for VLC media player