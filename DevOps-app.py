from flask import Flask, render_template
import requests
import uuid
from datetime import datetime, timezone
import logging
import threading
import time

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_random_string():
    """Function to log a random string and timestamp every 5 seconds."""
    while True:
        random_string = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()
        app.logger.info(f"{random_string} | {timestamp}")
        time.sleep(5)  # Sleep for 5 seconds before logging again

def get_quote():
    """Function to fetch a random quote from ZenQuotes API."""
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            return response.json()[0]['q']  # Returns the quote
        else:
            return "It will be fixed!"  # Fallback quote if API call fails
    except Exception as e:
        return "Do somethig nice today!"  # Fallback quote in case of error

@app.route('/')
def home():
    quote = get_quote()  # Fetch quote from API
    return render_template('index.html', message="We love you - Enjoy you day!", quote=quote)

if __name__ == '__main__':
    # Start the logging thread
    logging_thread = threading.Thread(target=log_random_string)
    logging_thread.daemon = True  # Daemon thread will shut down with the main program
    logging_thread.start()

    # Run the Flask application on port 8081
    app.run(debug=True, port=8081)  # Add port=8081 here
