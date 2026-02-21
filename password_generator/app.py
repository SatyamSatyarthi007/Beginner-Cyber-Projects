from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Difficulty to length mapping
DIFFICULTY_LENGTHS = {
    "easy": 8,
    "medium": 12,
    "hard": 16
}

# Character sets
ALPHABETS = string.ascii_letters
NUMERICAL = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_password():
    """Generate password based on user selections"""
    try:
        data = request.get_json()
        
        # Get parameters
        difficulty = data.get('difficulty')
        include_alphabets = data.get('include_alphabets', False)
        include_numerical = data.get('include_numerical', False)
        include_symbols = data.get('include_symbols', False)
        
        # Get optional custom inputs
        custom_name = data.get('custom_name', '').strip()
        custom_number = data.get('custom_number', '').strip()
        custom_symbol = data.get('custom_symbol', '').strip()
        
        # Validate inputs
        if not difficulty or difficulty not in DIFFICULTY_LENGTHS:
            return jsonify({'error': 'Invalid difficulty level'}), 400
        
        # For automatic mode, use all character types
        if not (include_alphabets or include_numerical or include_symbols):
            include_alphabets = True
            include_numerical = True
            include_symbols = True
        
        # Build character pool
        character_pool = ""
        if include_alphabets:
            character_pool += ALPHABETS
        if include_numerical:
            character_pool += NUMERICAL
        if include_symbols:
            character_pool += SYMBOLS
        
        # Get password length
        length = DIFFICULTY_LENGTHS[difficulty]
        
        # Start with custom inputs (if provided)
        password_chars = []
        
        # Add custom name characters (if provided)
        if custom_name:
            # Take characters from name, shuffle them
            name_chars = list(custom_name)
            random.shuffle(name_chars)
            password_chars.extend(name_chars)
        
        # Add custom number (if provided)
        if custom_number:
            password_chars.append(custom_number)
        
        # Add custom symbol (if provided)
        if custom_symbol:
            password_chars.append(custom_symbol)
        
        # Calculate how many more characters we need
        remaining_length = max(0, length - len(password_chars))
        
        # Add random characters to reach desired length
        if remaining_length > 0:
            random_chars = [random.choice(character_pool) for _ in range(remaining_length)]
            password_chars.extend(random_chars)
        
        # Shuffle all characters to mix custom and random
        random.shuffle(password_chars)
        
        # Take only the required length (in case custom inputs made it longer)
        password = ''.join(password_chars[:length])
        
        return jsonify({
            'success': True,
            'password': password,
            'length': len(password)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
