# VLC Gesture Control

Control VLC Media Player with hand gestures using your webcam.

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

VLC Gesture Control allows you to control VLC Media Player using hand gestures detected through your webcam. It uses computer vision and machine learning to recognize various hand gestures and translate them into VLC control commands.

## Features

- **Intuitive Gesture Controls**: Control playback, volume, and navigation with natural hand gestures
- **GPU Acceleration**: Optional GPU acceleration for improved performance
- **Camera Feedback**: Real-time visual feedback with FPS display
- **Robust Detection**: Ignores back-of-hand gestures to prevent accidental triggers
- **Multi-Monitor Support**: Controls VLC even when it's not in focus

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
| ✋ All five fingers up | Play/Pause | Show all five fingers |
| ☝️ Index finger only | Volume Up | Raise only your index finger |
| 👍 Thumb + index finger | Volume Down | Show only thumb and index finger |
| ✌️ Index + middle fingers | Forward 10 sec | Peace sign |
| 👌 Thumb + index + middle fingers | Backward 10 sec | Show thumb, index, and middle finger |
| 🤟 Index + middle + ring fingers | Toggle Subtitle | Show index, middle, and ring fingers |
| 🖖 All fingers except thumb | Change Audio Track | Show all fingers except thumb |
| 👍 Left hand thumb only | Next Video | Show only thumb on left hand |
| 👍 Right hand thumb only | Previous Video | Show only thumb on right hand |

## Advanced Features

- **Fast Forward/Backward**: When repeating the forward/backward gesture 4+ times in a row, it activates fast forward/backward mode.
- **Palm Detection**: The system only recognizes gestures when your palm is facing the camera, allowing you to move your hand freely without triggering unwanted actions.

## Command Line Options

```
usage: vlc-gesture-control [-h] [--version] [--mode {cpu,gpu}] [--camera CAMERA] [--debug]

Control VLC media player using hand gestures detected through your webcam.

options:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  --mode {cpu,gpu}     Processing mode: CPU (default) or GPU if supported
  --camera CAMERA      Camera index to use (default: 0)
  --debug              Enable debug mode with additional logging
```

## Troubleshooting

- **No VLC window found**: Make sure VLC is running and a video is playing.
- **Camera not detected**: Check your webcam connection and try a different camera index with `--camera 1`.
- **Low FPS**: Try running with GPU mode using `--mode gpu` or close other applications using the webcam.
- **Gestures not recognized**: Ensure good lighting conditions and position your hand clearly in the camera view.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies (`pip install -e ".[dev]"`)
4. Make your changes
5. Run tests (`pytest`)
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe for hand tracking technology
- OpenCV for computer vision capabilities
- VLC Media Player for being an awesome open-source media player 