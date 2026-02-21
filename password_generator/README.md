# Password Generator

A user-friendly password generator web application built with Flask and modern web technologies.

## Features

- **Difficulty Selection**: Choose between Easy (8 characters), Medium (12 characters), or Hard (16 characters)
- **Character Type Selection**: Customize your password by selecting which types of characters to include:
  - Alphabets (a-z, A-Z)
  - Numerical (0-9)
  - Symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
- **Password Display**: View your generated password in a clean, readable format
- **Copy to Clipboard**: Easily copy the generated password with one click
- **Generate New**: Generate a new password with the same settings
- **Start Over**: Reset and choose new options
- **Modern UI**: Beautiful, responsive web interface with smooth animations

## Requirements

- Python 3.6 or higher
- Flask (web framework)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. **Step 1**: Select the difficulty level (Easy, Medium, or Hard)
   - Easy: 8 characters
   - Medium: 12 characters
   - Hard: 16 characters
   - Click "Next" to proceed

4. **Step 2**: Select which character types to include in your password
   - Check at least one option (Alphabets, Numerical, or Symbols)
   - You can select multiple options
   - Click "Generate Password" to create your password

5. **Step 3**: View your generated password
   - The password will be displayed in a text field
   - Click "Copy" to copy it to your clipboard
   - Click "Generate New Password" to create another password with the same settings
   - Click "Start Over" to begin again with new options

## Example Workflow

1. Start the server: `python app.py`
2. Open `http://localhost:5000` in your browser
3. Select "Medium" difficulty
4. Click "Next"
5. Check "Alphabets" and "Numerical"
6. Click "Generate Password"
7. Your 12-character password containing letters and numbers will be displayed
8. Click "Copy" to copy it to clipboard

## API Endpoints

### POST /generate
Generates a password based on the provided parameters.

**Request Body (JSON):**
```json
{
  "difficulty": "easy|medium|hard",
  "include_alphabets": true|false,
  "include_numerical": true|false,
  "include_symbols": true|false
}
```

**Response (JSON):**
```json
{
  "success": true,
  "password": "generated_password_here",
  "length": 8
}
```

**Error Response:**
```json
{
  "error": "Error message here"
}
```

## Security Notes

- This tool generates random passwords using Python's `random` module
- For highly sensitive applications, consider using `secrets` module instead
- Always use strong, unique passwords for different accounts
- Never share your passwords with anyone
- The web server runs on localhost by default for security

## File Structure

```
password_generator/
├── app.py                    # Flask backend application
├── templates/
│   └── index.html           # Frontend HTML/CSS/JavaScript
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Development

The application uses:
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Styling**: Modern CSS with gradients and animations

To modify the port or host, edit the `app.run()` call in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## License

This project is open source and available for personal and educational use.
