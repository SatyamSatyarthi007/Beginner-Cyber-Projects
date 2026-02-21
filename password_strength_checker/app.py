from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)

def calculate_password_strength(password):
    """
    Calculate password strength based on various factors:
    - Length
    - Character variety (uppercase, lowercase, numbers, symbols)
    - Common patterns
    - Entropy
    """
    if not password:
        return {
            'strength': 0,
            'percentage': 0,
            'label': 'No Password',
            'color': '#9e9e9e'
        }
    
    score = 0
    feedback = []
    
    # Length scoring (0-25 points)
    length = len(password)
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    elif length >= 6:
        score += 8
    elif length >= 4:
        score += 4
    else:
        score += 1
    
    # Character variety scoring (0-30 points)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password))
    
    variety_count = sum([has_lower, has_upper, has_digit, has_special])
    score += variety_count * 7.5  # 7.5 points per variety type
    
    # Complexity scoring (0-20 points)
    # Check for mixed case
    if has_lower and has_upper:
        score += 5
    
    # Check for numbers and letters
    if (has_lower or has_upper) and has_digit:
        score += 5
    
    # Check for special characters
    if has_special:
        score += 5
    
    # Check for no consecutive identical characters
    consecutive = False
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            consecutive = True
            break
    if not consecutive:
        score += 5
    
    # Entropy-based scoring (0-15 points)
    # Calculate character set size
    charset_size = 0
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32  # Common special characters
    
    if charset_size > 0:
        entropy = length * math.log2(charset_size)
        # Normalize entropy score (max entropy for 20 chars with all types ~= 130)
        entropy_score = min(15, (entropy / 130) * 15)
        score += entropy_score
    
    # Pattern detection penalties (0-10 points deduction)
    # Common patterns
    common_patterns = [
        r'12345',
        r'abcde',
        r'qwerty',
        r'password',
        r'admin',
        r'letmein',
        r'welcome',
        r'monkey',
        r'123456',
        r'password123'
    ]
    
    password_lower = password.lower()
    pattern_penalty = 0
    for pattern in common_patterns:
        if re.search(pattern, password_lower):
            pattern_penalty += 2
    
    score -= min(10, pattern_penalty)
    
    # Sequential characters penalty
    sequential_count = 0
    for i in range(len(password) - 2):
        if (ord(password[i+1]) == ord(password[i]) + 1 and 
            ord(password[i+2]) == ord(password[i]) + 2):
            sequential_count += 1
    
    if sequential_count > 0:
        score -= min(5, sequential_count * 2)
    
    # Ensure score is between 0 and 100
    score = max(0, min(100, score))
    
    # Determine strength label and color
    if score >= 80:
        label = 'Very Strong'
        color = '#4caf50'  # Green
    elif score >= 60:
        label = 'Strong'
        color = '#8bc34a'  # Light Green
    elif score >= 40:
        label = 'Moderate'
        color = '#ff9800'  # Orange
    elif score >= 20:
        label = 'Weak'
        color = '#ff5722'  # Deep Orange
    else:
        label = 'Very Weak'
        color = '#f44336'  # Red
    
    return {
        'strength': score,
        'percentage': round(score),
        'label': label,
        'color': color,
        'length': length,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special
    }

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    """Check password strength"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        result = calculate_password_strength(password)
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
