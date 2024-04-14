from flask import Flask, request, jsonify
import os
import random
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the API key and initial token count from environment variables
API_KEY = os.getenv('API_KEY')
INITIAL_TOKENS = int(os.getenv('INITIAL_TOKENS', 100))
current_tokens = INITIAL_TOKENS

# List of random words to choose from
random_words = [
    'apple', 'banana', 'cat', 'dog', 'elephant', 'flower', 'guitar', 'hat', 'ice cream', 'jacket',
    'kite', 'lion', 'monkey', 'nest', 'ocean', 'penguin', 'quilt', 'rainbow', 'sunflower', 'tree',
    'umbrella', 'violin', 'watermelon', 'xylophone', 'yacht', 'zebra', 'airplane', 'bear', 'carrot',
    'duck', 'eggplant', 'fireworks', 'giraffe', 'hamburger', 'igloo', 'jellyfish', 'koala', 'lemon',
    'mushroom', 'ninja', 'octopus', 'piano', 'quokka', 'rocket', 'snake', 'turtle', 'unicorn',
    'volcano', 'whale', 'xylophonist', 'yak', 'zeppelin', 'acorn', 'butterfly', 'cactus', 'dolphin',
    'earrings', 'firefly', 'globe', 'hedgehog', 'igloo', 'jigsaw', 'kangaroo', 'leopard', 'mailbox',
    'noodles', 'otter', 'parrot', 'quail', 'raccoon', 'sailboat', 'tiger', 'umbrella', 'vampire',
    'waffle', 'xylophone', 'yarn', 'zebra', 'astronaut', 'bee', 'caterpillar', 'dragonfly', 'elephant',
    'flamingo', 'gorilla', 'honeycomb', 'iguana', 'jackal', 'koala', 'llama', 'moon', 'narwhal', 'owl',
    'peacock', 'quokka', 'rhinoceros', 'seahorse', 'toucan', 'unicorn', 'volcano', 'wombat', 'xylophone',
    'yak', 'zeppelin'
]

@app.route('/api', methods=['GET'])
def get_word():
    global current_tokens

    # Check if 'api_key' parameter is provided in the request
    api_key = request.args.get('api_key')

    # Check if API key matches
    if api_key == API_KEY:
        # Check if the user has enough tokens
        if current_tokens > 0:
            # Decrease token count by 1 for each API call
            current_tokens -= 1
            # Choose a random word from the list
            random_word = random.choice(random_words)
            # Return the random word along with the remaining tokens
            return jsonify({'word': random_word, 'remaining_tokens': current_tokens})
        else:
            # Return an error message if the user has no tokens left
            return jsonify({'error': 'No tokens left!'}), 403
    else:
        # Return an error message if API key is incorrect
        return jsonify({'error': 'Invalid API key'}), 401

if __name__ == '__main__':
    app.run(debug=False)
