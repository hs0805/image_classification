# utils.py
import os
from dotenv import load_dotenv

def load_env_variables():
    """
    Load environment variables from the .env file.
    """
    load_dotenv()

def get_database_config():
    """
    Get the MySQL database configuration as a dictionary.
    """
    load_env_variables()
    return {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DATABASE"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': os.getenv("MYSQL_HOST", "localhost"),
        'PORT': os.getenv("MYSQL_PORT", "3307"),
    }
