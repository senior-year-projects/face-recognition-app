import json
import os

def load_database(file_path):
    """
    Load the face database from a JSON file
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: A dictionary containing user names as keys and face encodings as values
    """
    if not os.path.exists(file_path):
        print(f"Database file '{file_path}' not found. Creating a new database.")
        return {}
    
    try:
        with open(file_path, "r") as file:
            database = json.load(file)
        print("Database loaded successfully.")
        return database
    except json.JSONDecodeError:
        print(f"Error reading the database file '{file_path}'. Creating a new database.")
        return {}

def save_database(file_path, database):
    """
    Save the face database as a JSON file
    
    Args:
        file_path (str): Path to the database file
        database (dict): The database to save
    """
    try:
        with open(file_path, "w") as file:
            json.dump(database, file, indent=4)
        print("Database saved successfully.")
    except Exception as e:
        print(f"Error saving the database: {e}")
