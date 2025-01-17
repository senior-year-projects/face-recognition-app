from utils import load_database, save_database, get_face_encodings, load_image, extract_frame_from_video, capture_frame_from_webcam
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
        return

    if input_type == 'image':
        frame = load_image(input_path)
    elif input_type == 'video':
        frame = extract_frame_from_video(input_path)
    elif input_type == 'webcam':
        frame = capture_frame_from_webcam()
    else:
        print("Invalid input type. Choose 'image', 'video', or 'webcam'.")
        return

    if frame is None:
        print("Failed to capture a valid frame for registration.")
        return

    face_encodings = get_face_encodings(frame)
    if face_encodings is None or len(face_encodings) == 0:
        print("No face detected or failed to encode face. Registration aborted.")
        return

    database[name] = face_encodings[0].tolist()
    save_database(database)
    print(f"User '{name}' successfully registered.")