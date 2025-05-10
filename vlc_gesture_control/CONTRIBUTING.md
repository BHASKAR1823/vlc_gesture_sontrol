# Contributing to VLC Gesture Control

Thank you for your interest in contributing to VLC Gesture Control! This document explains how to contribute to this project effectively.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the expectations for all participants.

## Development Environment Setup

1. Fork the repository on GitHub
2. Clone your fork locally
   ```bash
   git clone https://github.com/yourusername/vlc-gesture-control.git
   cd vlc-gesture-control
   ```
3. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
4. Install in development mode with all development dependencies
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run tests to ensure your changes do not break existing functionality
   ```bash
   pytest
   ```
4. Format your code
   ```bash
   black src
   isort src
   ```
5. Commit your changes with a descriptive commit message
   ```bash
   git commit -m "Add feature: your feature description"
   ```
6. Push to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
7. Create a Pull Request from your fork to the main repository

## Code Style

We follow the [Black](https://black.readthedocs.io/) code style. Please ensure your code is formatted with Black before submitting a pull request.

```bash
black src
```

We also use [isort](https://pycqa.github.io/isort/) to sort imports.

```bash
isort src
```

## Testing

Write tests for all new features and bug fixes. We use [pytest](https://docs.pytest.org/) for testing.

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=vlc_gesture_control
```

## Documentation

Update the documentation when adding or changing features. This includes:

- Code docstrings
- README.md updates when applicable
- Addition of new examples if needed

## Pull Request Process

1. Update the README.md with details of changes if applicable.
2. Update the tests to cover your changes.
3. The PR should work on all supported Python versions (3.9+).
4. Your PR must pass all CI checks before it will be merged.
5. Pull requests require at least one review from a maintainer.

## Feature Requests and Bug Reports

Please use the GitHub issues page to:

- Report bugs
- Request new features
- Suggest improvements

## License

By contributing to VLC Gesture Control, you agree that your contributions will be licensed under the project's MIT License. 