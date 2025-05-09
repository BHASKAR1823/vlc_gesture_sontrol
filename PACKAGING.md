# VLC Gesture Control Packaging Guide

This document outlines the process for packaging, testing, and publishing the VLC Gesture Control package to PyPI.

## Package Structure

The package follows the recommended "src" layout:

```
vlc_gesture_control/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── publish.yml
├── src/
│   └── vlc_gesture_control/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── gesture_detector.py
│       ├── media_controller.py
│       ├── vlc_m_cpu.py
│       ├── vlc_m_gpu.py
│       └── tests/
│           ├── __init__.py
│           └── test_gesture_detector.py
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── pytest.ini
├── README.md
└── setup.py
```

## Development Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vlc-gesture-control.git
   cd vlc-gesture-control
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Testing

Run the tests using pytest:

```bash
pytest
```

For coverage report:

```bash
pytest --cov=vlc_gesture_control
```

## Code Quality

Format your code with Black:

```bash
black src
```

Sort imports with isort:

```bash
isort src
```

Lint with flake8:

```bash
flake8 src
```

## Building the Package

Build source and wheel distributions:

```bash
python -m build
```

This creates:
- A source distribution (`dist/*.tar.gz`)
- A wheel distribution (`dist/*.whl`)

## Local Installation

Install the built package:

```bash
pip install dist/vlc_gesture_control-0.1.0-py3-none-any.whl
```

## Publishing to PyPI

### Test PyPI

1. Register on [Test PyPI](https://test.pypi.org/account/register/)
2. Upload to Test PyPI:
   ```bash
   twine upload --repository testpypi dist/*
   ```
3. Install from Test PyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --no-deps vlc-gesture-control
   ```

### Production PyPI

1. Register on [PyPI](https://pypi.org/account/register/)
2. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## Automated Publishing

The GitHub workflow in `.github/workflows/publish.yml` automatically publishes to PyPI when a new release is created. To use it:

1. Set up PyPI API tokens as GitHub secrets:
   - `PYPI_USERNAME`
   - `PYPI_PASSWORD`

2. Create a new release on GitHub

## Version Updates

1. Update the version in `src/vlc_gesture_control/__init__.py`
2. Update the version in `pyproject.toml`
3. Create a new git tag:
   ```bash
   git tag v0.1.0
   git push --tags
   ```

## Troubleshooting

### Common Issues

1. **Import errors after installation**: Check relative imports in the package files.
2. **Build failures**: Ensure all required files are included in `MANIFEST.in`.
3. **Test failures**: Run tests with `-v` flag for more details.

### Getting Help

If you encounter issues, please:
1. Check the [GitHub Issues](https://github.com/yourusername/vlc-gesture-control/issues)
2. Create a new issue with details about the problem 