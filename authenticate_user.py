from utils import load_database, get_face_encodings, load_image, capture_frame_from_webcam
import face_recognition

def authenticate_user(input_type, input_path=None):
    """
    Authenticate a user by comparing their face encoding with the database

    Args:
        input_type (str): Type of input ('image', 'video', 'webcam')
        input_path (str, optional): Path to the input file (image or video) Defaults to None
    Returns:
        str: Name of the authenticated user if successful, None otherwise
    """
    database = load_database()
    if not database:
        print("The database is empty. No users to authenticate.")
        return None

    if input_type == 'image':
        frame = load_image(input_path)
    elif input_type == 'webcam':
        frame = capture_frame_from_webcam()
    else:
        print("Invalid input type. Choose 'image', 'video', or 'webcam'.")
        return None

    if frame is None:
        print("Failed to capture a valid frame for authentication.")
        return None

    face_encodings = get_face_encodings(frame)
    if face_encodings is None or len(face_encodings) == 0:
        print("No face detected or failed to encode face. Authentication aborted.")
        return None

    for name, stored_encoding in database.items():
        matches = face_recognition.compare_faces([stored_encoding], face_encodings[0])
        if matches[0]:
            print(f"Authentication successful. User: {name}")
            return name

    print("Authentication failed. No match found.")
    return None
