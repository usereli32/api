from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the API key and initial token count from environment variables
API_KEY = os.getenv('API_KEY')
INITIAL_TOKENS = int(os.getenv('INITIAL_TOKENS', 100))
current_tokens = INITIAL_TOKENS

@app.route('/api', methods=['GET'])
def get_emoji():
    global current_tokens
    
    # Check if 'api_key' parameter is provided in the request
    api_key = request.args.get('api_key')
    
    # Check if API key matches
    if api_key == API_KEY:
        # Check if the user has enough tokens
        if current_tokens > 0:
            # Decrease token count by 1 for each API call
            current_tokens -= 1
            # Return a happy emoji along with the remaining tokens
            return jsonify({'emoji': '😊', 'remaining_tokens': current_tokens})
        else:
            # Return an error message if the user has no tokens left
            return jsonify({'error': 'No tokens left!'}), 403
    else:
        # Return an error message if API key is incorrect
        return jsonify({'error': 'Invalid API key'}), 401

if __name__ == '__main__':
    app.run(debug=True)
