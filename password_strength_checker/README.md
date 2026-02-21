# Password Strength Checker

A Flask web application that checks password strength with visual indicators, percentage scores, and estimated time-to-crack calculations.

## Features

- **Password Strength Analysis**: Comprehensive analysis based on:
  - Password length
  - Character variety (uppercase, lowercase, numbers, symbols)
  - Complexity patterns
  - Entropy calculation
  - Common pattern detection

- **Visual Feedback**:
  - Strength percentage (0-100%)
  - Color-coded indicators (Red → Orange → Green)
  - Animated progress bar
  - Strength label (Very Weak to Very Strong)

- **Time-to-Crack Estimation**: Calculates estimated time required to crack the password using brute force attacks

- **Criteria Checklist**: Shows which password requirements are met:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters

## Installation

1. Make sure you have Python 3.6+ installed

2. Install Flask:
```bash
pip install flask
```

## Usage

1. Navigate to the project directory:
```bash
cd password_strength_checker
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5001
```

4. Enter a password in the input field and click "Check Strength" or press Enter

## How It Works

The password strength checker evaluates passwords based on multiple factors:

1. **Length Scoring** (0-25 points): Longer passwords score higher
2. **Character Variety** (0-30 points): More character types increase the score
3. **Complexity** (0-20 points): Mixed case, numbers, and special characters
4. **Entropy** (0-15 points): Based on character set size and password length
5. **Pattern Detection** (penalties): Common patterns and sequential characters reduce the score

The final score (0-100) determines:
- **80-100**: Very Strong (Green)
- **60-79**: Strong (Light Green)
- **40-59**: Moderate (Orange)
- **20-39**: Weak (Deep Orange)
- **0-19**: Very Weak (Red)

## Time-to-Crack Calculation

The time-to-crack estimation assumes:
- 1 billion guesses per second (modern GPU cluster capability)
- Brute force attack method
- Average case scenario (50% of possible combinations)

## Port Configuration

The application runs on port **5001** by default. If you need to change it, modify the last line in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Security Note

This tool is for educational and personal use. The password checking is performed client-side via API calls. For production use, consider implementing rate limiting and additional security measures.
