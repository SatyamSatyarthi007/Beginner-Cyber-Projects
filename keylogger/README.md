# Simple Keylogger - Educational Project

A beginner-friendly keylogger implementation for cybersecurity education.

## What is a Keylogger?

A keylogger is a type of surveillance software that records every keystroke made on a computer keyboard. While keyloggers can be used maliciously, they also have legitimate uses such as:

- System monitoring (on your own systems)
- Parental control software
- Employee monitoring (with proper disclosure)
- Security research and education

## Features

- Logs all keystrokes with timestamps
- Handles special keys (Enter, Space, Tab, etc.)
- Saves logs to a text file
- Easy to stop (press ESC)
- Simple and educational code structure

## Requirements

- Python 3.6 or higher
- `pynput` library

## Installation

1. Install Python dependencies:
pip install pynput

Or use the requirements file:
pip install -r requirements.txt

### Basic Usage

1. Run the keylogger with default settings:

py keylogger.py

python keylogger.py
You can specify a custom location for the log file using the `-o` or `--output` option:


py keylogger.py -o logs/my_keylog.txt

py keylogger.py --output C:\Users\YourName\Documents\logs\keystrokes.log

py keylogger.py -o my_custom_log.txt
python keylogger.py -o logs/my_keylog.txt

python keylogger.py -o /home/username/logs/keystrokes.log

python keylogger.py -o my_custom_log.txt

### Usage Steps

1. Run the keylogger (with or without custom path)
2. The keylogger will start monitoring keystrokes
3. All keystrokes will be logged to the specified file (or `keystrokes.log` by default)
4. Press **ESC** to stop the keylogger

## Log Analyzer Tool

The project includes a log analyzer tool (`log_analyzer.py`) to help you analyze and view captured keystrokes in a more readable format.

### Using the Log Analyzer

The log analyzer supports two modes: **interactive mode** (prompts for file path) and **command-line mode** (file path as argument).

#### Interactive Mode (Recommended for Beginners)

**Windows:**
```bash
# Run without arguments - will prompt for log file path
py log_analyzer.py

# With options
py log_analyzer.py --text    # Will prompt for file, then show formatted text
py log_analyzer.py --all     # Will prompt for file, then show everything
```

**Linux/Mac:**
```bash
# Run without arguments - will prompt for log file path
python log_analyzer.py

# With options
python log_analyzer.py --text    # Will prompt for file, then show formatted text
python log_analyzer.py --all     # Will prompt for file, then show everything
```

#### Command-Line Mode

**Windows:**
```bash
# Show statistics (default)
py log_analyzer.py keystrokes.log

# Show formatted text (what was actually typed)
py log_analyzer.py keystrokes.log --text

# Show raw log entries
py log_analyzer.py keystrokes.log --raw

# Show everything (stats, text, and raw)
py log_analyzer.py keystrokes.log --all
```

**Linux/Mac:**
```bash
# Show statistics (default)
python log_analyzer.py keystrokes.log

# Show formatted text (what was actually typed)
python log_analyzer.py keystrokes.log --text

# Show raw log entries
python log_analyzer.py keystrokes.log --raw

# Show everything (stats, text, and raw)
python log_analyzer.py keystrokes.log --all
```

### Analyzer Features

- **Statistics**: Total keystrokes, character count, special key count, time span, most common keys
- **Formatted Text**: Converts keystrokes back to readable text
- **Raw View**: Shows all log entries with timestamps
- **Flexible Output**: Choose what information to display

## How It Works

1. **Keyboard Listener**: Uses `pynput` library to create a keyboard listener
2. **Event Callbacks**: 
   - `on_press()`: Called when a key is pressed, logs the keystroke
   - `on_release()`: Called when a key is released, checks for ESC to stop
3. **Logging**: Writes each keystroke with timestamp to a log file
4. **Special Keys**: Handles special keys like Enter, Space, Tab, etc.

## Code Structure

- `on_press(key)`: Handles key press events and logs them
- `on_release(key)`: Handles key release events, stops on ESC
- `start_keylogger()`: Initializes and starts the keylogger
- Main execution: Entry point that starts the program

## Log File Format

The log file (`keystrokes.log`) contains entries like:
```
[2024-01-15 14:30:25] h
[2024-01-15 14:30:25] e
[2024-01-15 14:30:25] l
[2024-01-15 14:30:25] l
[2024-01-15 14:30:25] o
[2024-01-15 14:30:25] SPACE
[2024-01-15 14:30:25] w
[2024-01-15 14:30:25] o
[2024-01-15 14:30:25] r
[2024-01-15 14:30:25] l
[2024-01-15 14:30:25] d
[2024-01-15 14:30:25] ENTER
```

## Learning Objectives

By studying this code, you can learn:

1. How keyboard input monitoring works
2. Event-driven programming concepts
3. File I/O operations
4. Exception handling
5. Security concepts and vulnerabilities
6. Ethical hacking principles

## Defensive Measures

Understanding keyloggers helps you defend against them:

- **Antivirus Software**: Most antivirus programs detect keyloggers
- **Keystroke Encryption**: Some security software encrypts keystrokes
- **Virtual Keyboards**: Use virtual keyboards for sensitive input
- **Two-Factor Authentication**: Reduces impact of stolen passwords
- **Regular System Scans**: Scan for malware regularly

## Disclaimer

This software is provided "as is" for educational purposes only. The authors and contributors are not responsible for any misuse of this software. Users are solely responsible for ensuring they comply with all applicable laws and regulations.

## License

Educational use only. See legal warnings above.

