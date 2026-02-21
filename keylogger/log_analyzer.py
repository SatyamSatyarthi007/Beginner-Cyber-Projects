"""
Log Analyzer for Keylogger
===========================
A tool to analyze and view keylogger log files in a more readable format.
"""

import argparse
import os
from datetime import datetime
from collections import Counter


def parse_log_file(log_path):
    """
    Parses the keylogger log file and extracts keystrokes.
    
    Args:
        log_path: Path to the log file
    
    Returns:
        tuple: (header_info, keystrokes_list)
    """
    if not os.path.exists(log_path):
        print(f"[!] Error: Log file not found: {log_path}")
        return None, None
    
    keystrokes = []
    header_info = {}
    
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # Parse header (first few lines)
            if lines:
                # Check for start time
                if "Keylogger started at:" in lines[0]:
                    start_time_str = lines[0].split("Keylogger started at:")[1].strip()
                    header_info['start_time'] = start_time_str
                
                # Parse keystrokes (skip header lines)
                for line in lines[2:]:  # Skip first 2 lines (header)
                    line = line.strip()
                    if line and line.startswith('['):
                        # Extract timestamp and key
                        try:
                            # Format: [timestamp] key
                            parts = line.split('] ', 1)
                            if len(parts) == 2:
                                timestamp_str = parts[0][1:]  # Remove leading '['
                                key = parts[1]
                                keystrokes.append({
                                    'timestamp': timestamp_str,
                                    'key': key
                                })
                        except Exception as e:
                            continue
    
    except Exception as e:
        print(f"[!] Error reading log file: {e}")
        return None, None
    
    return header_info, keystrokes


def format_as_text(keystrokes):
    """
    Converts keystrokes to readable text format.
    
    Args:
        keystrokes: List of keystroke dictionaries
    
    Returns:
        str: Formatted text
    """
    text = ""
    for stroke in keystrokes:
        key = stroke['key']
        
        # Convert special keys to readable format
        if key == 'SPACE':
            text += ' '
        elif key == 'ENTER':
            text += '\n'
        elif key == 'TAB':
            text += '\t'
        elif key == 'BACKSPACE':
            # Remove last character if possible
            if text:
                text = text[:-1]
        elif key in ['SHIFT', 'CTRL', 'ALT', 'ESC']:
            # Skip modifier keys in text output
            continue
        elif key.startswith('Key.'):
            # Skip other special keys
            continue
        else:
            # Regular character
            text += key
    
    return text


def analyze_keystrokes(keystrokes):
    """
    Analyzes keystrokes and provides statistics.
    
    Args:
        keystrokes: List of keystroke dictionaries
    
    Returns:
        dict: Statistics dictionary
    """
    if not keystrokes:
        return {}
    
    stats = {
        'total_keystrokes': len(keystrokes),
        'characters': 0,
        'special_keys': 0,
        'most_common_keys': [],
        'time_span': None
    }
    
    # Count characters vs special keys
    key_counts = Counter()
    special_keys = ['SPACE', 'ENTER', 'TAB', 'BACKSPACE', 'SHIFT', 'CTRL', 'ALT', 'ESC']
    
    for stroke in keystrokes:
        key = stroke['key']
        key_counts[key] += 1
        
        if key in special_keys or key.startswith('Key.'):
            stats['special_keys'] += 1
        else:
            stats['characters'] += 1
    
    # Get most common keys (top 10)
    stats['most_common_keys'] = key_counts.most_common(10)
    
    # Calculate time span
    if len(keystrokes) > 1:
        try:
            first_time = datetime.strptime(keystrokes[0]['timestamp'], "%Y-%m-%d %H:%M:%S")
            last_time = datetime.strptime(keystrokes[-1]['timestamp'], "%Y-%m-%d %H:%M:%S")
            time_diff = last_time - first_time
            stats['time_span'] = str(time_diff)
        except:
            pass
    
    return stats


def display_analysis(log_path, show_text=False, show_stats=True, show_raw=False):
    """
    Displays log file analysis.
    
    Args:
        log_path: Path to the log file
        show_text: Whether to show formatted text
        show_stats: Whether to show statistics
        show_raw: Whether to show raw log entries
    """
    print("=" * 70)
    print("KEYLOGGER LOG ANALYZER")
    print("=" * 70)
    print(f"\n[*] Analyzing: {os.path.abspath(log_path)}\n")
    
    header_info, keystrokes = parse_log_file(log_path)
    
    if keystrokes is None:
        return
    
    if not keystrokes:
        print("[!] No keystrokes found in log file.")
        return
    
    # Display header info
    if header_info and 'start_time' in header_info:
        print(f"[*] Keylogger started: {header_info['start_time']}")
    
    # Display statistics
    if show_stats:
        print("\n" + "-" * 70)
        print("STATISTICS")
        print("-" * 70)
        stats = analyze_keystrokes(keystrokes)
        
        print(f"Total keystrokes: {stats['total_keystrokes']}")
        print(f"Characters: {stats['characters']}")
        print(f"Special keys: {stats['special_keys']}")
        
        if stats['time_span']:
            print(f"Time span: {stats['time_span']}")
        
        if stats['most_common_keys']:
            print("\nMost common keys:")
            for key, count in stats['most_common_keys']:
                print(f"  {key}: {count} times")
    
    # Display formatted text
    if show_text:
        print("\n" + "-" * 70)
        print("FORMATTED TEXT")
        print("-" * 70)
        text = format_as_text(keystrokes)
        if text.strip():
            print(text)
        else:
            print("(No readable text found)")
    
    # Display raw entries
    if show_raw:
        print("\n" + "-" * 70)
        print("RAW LOG ENTRIES")
        print("-" * 70)
        for stroke in keystrokes[:50]:  # Show first 50
            print(f"[{stroke['timestamp']}] {stroke['key']}")
        if len(keystrokes) > 50:
            print(f"\n... and {len(keystrokes) - 50} more entries")
    
    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze keylogger log files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  py log_analyzer.py                                # Interactive mode (Windows)
  python log_analyzer.py                            # Interactive mode (Linux/Mac)
  py log_analyzer.py keystrokes.log                 # Show statistics (Windows)
  py log_analyzer.py keystrokes.log --text          # Show formatted text (Windows)
  py log_analyzer.py keystrokes.log --all           # Show everything (Windows)
  python log_analyzer.py keystrokes.log --raw      # Show raw entries (Linux/Mac)
        """
    )
    
    parser.add_argument(
        'log_file',
        type=str,
        nargs='?',
        default=None,
        help='Path to the keylogger log file (optional - will prompt if not provided)'
    )
    
    parser.add_argument(
        '-t', '--text',
        action='store_true',
        help='Display formatted text from keystrokes'
    )
    
    parser.add_argument(
        '-r', '--raw',
        action='store_true',
        help='Display raw log entries'
    )
    
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='Show all information (stats, text, and raw)'
    )
    
    parser.add_argument(
        '--no-stats',
        action='store_true',
        help='Hide statistics'
    )
    
    args = parser.parse_args()
    
    # Get log file path - prompt if not provided
    log_file_path = args.log_file
    if not log_file_path:
        print("\n[*] Enter the path to the log file to analyze")
        print("[*] You can also provide the path as a command-line argument\n")
        log_file_path = input("Log file path: ").strip()
        
        if not log_file_path:
            print("\n[!] Error: No log file path provided. Exiting.")
            return
        
        # Remove quotes if user pasted a path with quotes
        if log_file_path.startswith('"') and log_file_path.endswith('"'):
            log_file_path = log_file_path[1:-1]
        elif log_file_path.startswith("'") and log_file_path.endswith("'"):
            log_file_path = log_file_path[1:-1]
        
        print()  # Add blank line for better formatting
    
    show_stats = not args.no_stats
    show_text = args.text or args.all
    show_raw = args.raw or args.all
    
    display_analysis(log_file_path, show_text, show_stats, show_raw)


if __name__ == "__main__":
    main()

