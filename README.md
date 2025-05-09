# VLC Gesture Control

[![PyPI version](https://badge.fury.io/py/vlc-gesture-control.svg)](https://badge.fury.io/py/vlc-gesture-control)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/vlc-gesture-control.svg)](https://pypi.org/project/vlc-gesture-control/)

Control VLC media player using hand gestures detected through your webcam without touching your keyboard or mouse. Perfect for watching movies from a distance!

![VLC Gesture Control Demo](https://raw.githubusercontent.com/yourusername/vlc-gesture-control/main/docs/images/demo.gif)

## Features

- Control VLC media player using intuitive hand gestures
- Support for both CPU and GPU processing
- Palm-facing detection to prevent accidental triggers
- Fast-forward and rewind functionality with repeated gestures
- Real-time performance monitoring with FPS display
- Cross-platform compatibility (Windows focus)
- Multiple gesture control schemes

## Screenshots

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/yourusername/vlc-gesture-control/main/docs/images/play_pause.jpg" alt="Play/Pause Gesture" width="200"/></td>
    <td><img src="https://raw.githubusercontent.com/yourusername/vlc-gesture-control/main/docs/images/volume_up.jpg" alt="Volume Up Gesture" width="200"/></td>
    <td><img src="https://raw.githubusercontent.com/yourusername/vlc-gesture-control/main/docs/images/volume_down.jpg" alt="Volume Down Gesture" width="200"/></td>
  </tr>
  <tr>
    <td align="center"><b>Play/Pause</b><br/>(All fingers up)</td>
    <td align="center"><b>Volume Up</b><br/>(Index finger only)</td>
    <td align="center"><b>Volume Down</b><br/>(Thumb + Index finger)</td>
  </tr>
</table>

## Supported Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| All five fingers up | Play/Pause | Show an open palm with all 5 fingers extended |
| Index finger only | Volume Up | Show only your index finger pointing up |
| Thumb + Index finger | Volume Down | Show thumb and index finger (like an "L" shape) |
| Index + Middle fingers | Forward 10 seconds | Show index and middle fingers together (peace sign) |
| Thumb + Index + Middle fingers | Backward 10 seconds | Show thumb, index and middle fingers |
| Index + Middle + Ring fingers | Toggle Subtitles | Show index, middle and ring fingers |
| All fingers except thumb | Change Audio Track | Show all fingers except thumb |
| Left hand thumb only (pointing right) | Next Video | Show only thumb on left hand pointing to the right |
| Right hand thumb only (pointing left) | Previous Video | Show only thumb on right hand pointing to the left |

## Requirements

- Python 3.9+ 
- VLC Media Player
- Webcam
- Windows OS

## Installation

### Via pip (Recommended)

```bash
# Basic installation (CPU mode)
pip install vlc-gesture-control

# With GPU support (if you have compatible NVIDIA GPU)
pip install vlc-gesture-control[gpu]

# For development
pip install vlc-gesture-control[dev]
```

### From source

```bash
# Clone the repository
git clone https://github.com/yourusername/vlc-gesture-control.git
cd vlc-gesture-control

# Install in development mode
pip install -e .
```

## Usage

### Quick Start

1. First, open VLC media player and start playing a video
2. In a command prompt or terminal, run one of the following commands:

```bash
# Use CPU mode (recommended for most users)
vlc-gesture-control-cpu

# Use GPU mode (if you have compatible hardware)
vlc-gesture-control-gpu

# Or use the universal command with options
vlc-gesture-control --mode cpu --camera 0
```

3. Position your hand in front of the webcam with palm facing the camera
4. Use the gestures listed in the table above to control VLC
5. Press 'q' to quit the application

### Command-line Options

```bash
vlc-gesture-control --help
```

This will display all available command-line options:

```
usage: vlc-gesture-control [-h] [--version] [--mode {cpu,gpu}] [--camera CAMERA] [--debug]

Control VLC media player using hand gestures detected through your webcam.

options:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  --mode {cpu,gpu}   Processing mode: CPU (default) or GPU if supported
  --camera CAMERA    Camera index to use (default: 0)
  --debug            Enable debug mode with additional logging
```

## How It Works

The application uses MediaPipe's hand tracking to detect hand landmarks in real-time:

1. Your webcam captures video frames
2. MediaPipe's hand tracking detects 21 landmark points on your hand
3. The application analyzes the configuration of fingers to recognize specific gestures
4. When a consistent gesture is detected, the corresponding keyboard command is sent to VLC
5. To prevent accidental commands, a gesture must be detected multiple times consistently

The palm-facing detection ensures that gestures are only recognized when your palm is facing the camera, preventing accidental triggers when the back of your hand is visible.

## Troubleshooting

### Common Issues

#### "VLC not found" error

- Make sure VLC is running before starting the gesture control application
- If VLC is running and you still get this error, try restarting both VLC and the gesture control application

#### Poor gesture recognition

- Ensure there is good lighting in your room
- Keep your hand at a reasonable distance from the camera (about 1-2 feet)
- Make clear, deliberate gestures with your palm facing the camera
- Adjust your position if the application shows "Palm not facing camera"

#### Camera issues

- If your webcam isn't detected, make sure it's properly connected
- Try specifying a different camera index: `vlc-gesture-control --camera 1`
- Check if another application is using your camera

#### High CPU usage

- CPU mode can be resource-intensive; try lowering your camera resolution
- If you have a compatible GPU, try using GPU mode: `vlc-gesture-control --mode gpu`

#### GPU mode not working

- Make sure you installed with GPU support: `pip install vlc-gesture-control[gpu]`
- Ensure you have compatible NVIDIA GPU drivers installed
- Check that CUDA and cuDNN are properly installed

### Reporting Issues

If you encounter any issues not covered in this section, please report them on the [GitHub issues page](https://github.com/yourusername/vlc-gesture-control/issues).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MediaPipe](https://developers.google.com/mediapipe) for hand tracking technology
- [VideoLAN](https://www.videolan.org) for VLC media player
- All contributors who have helped improve this project 