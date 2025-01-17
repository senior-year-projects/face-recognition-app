from utils import load_database, get_face_encodings, load_image, extract_frame_from_video, capture_frame_from_webcam
import face_recognition

def authenticate_user(input_type, input_path=None):
    """
    Authenticate a user by comparing their face encoding with the database

    Args:
        input_type (str): Type of input ('image', 'video', 'webcam')
        input_path (str, optional): Path to the input file (image or video). Defaults to None
    """
    database = load_database()
    if not database:
        print("The database is empty. No users to authenticate.")
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
        print("Failed to capture a valid frame for authentication.")
        return

    face_encodings = get_face_encodings(frame)
    if face_encodings is None or len(face_encodings) == 0:
        print("No face detected or failed to encode face. Authentication aborted.")
        return

    for name, stored_encoding in database.items():
        matches = face_recognition.compare_faces([stored_encoding], face_encodings[0])
        if matches[0]:
            print(f"Authentication successful. User: {name}")
            return

    print("Authentication failed. No match found.")
