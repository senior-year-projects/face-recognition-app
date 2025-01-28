from utils import load_database, save_database, get_face_encodings, load_image, capture_frame_from_webcam
import os

def register_user(name, input_type, input_path=None):
    """
    Register a user by capturing their face encoding and storing it in the database

    Args:
        name (str): Name of the user
        input_type (str): Type of input ('image', 'video', 'webcam')
        input_path (str, optional): Path to the input file (image or video). Defaults to None
    """
    database = load_database()

    if name in database:
        print(f"User '{name}' already exists in the database.")
        return False

    if input_type == 'image':
        frame = load_image(input_path)
    elif input_type == 'webcam':
        frame = capture_frame_from_webcam()
    else:
        print("Invalid input type. Choose 'image', 'video', or 'webcam'.")
        return False

    if frame is None:
        print("Failed to capture a valid frame for registration.")
        return False

    face_encodings = get_face_encodings(frame)
    if face_encodings is None or len(face_encodings) == 0:
        print("No face detected or failed to encode face. Registration aborted.")
        return False

    database[name] = face_encodings[0].tolist()
    save_database(database)
    print(f"User '{name}' successfully registered.")
    return True