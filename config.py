# Example configuration settings for Flask app

# Flask app configuration
DEBUG = True  # Enable debug mode for development
SECRET_KEY = 'your_secret_key_here'  # Replace with a random secret key for session security

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False