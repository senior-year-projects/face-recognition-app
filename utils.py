import json
import os
import cv2
import face_recognition

DATABASE_PATH = "face_database.json"

def load_database():
    """
    Load the face database from a JSON file.
    """
    if not os.path.exists(DATABASE_PATH):
        return {}
    with open(DATABASE_PATH, "r") as file:
        return json.load(file)

def save_database(data):
    """
    Save the face database to a JSON file.
    """
    with open(DATABASE_PATH, "w") as file:
        json.dump(data, file)

def validate_file_path(file_path):
    """
    Validate if a given file path exists and is accessible
    """
    if not os.path.exists(file_path):
        return False, f"File '{file_path}' does not exist."
    return True, None

def validate_image_format(file_path):
    """
    Validate if the given file path is valid
    """
    valid_extensions = [".jpg", ".jpeg", ".png", ".bmp"]
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in valid_extensions:
        return False, f"Invalid image format '{ext}'. Supported formats: {', '.join(valid_extensions)}."
    return True, None

def display_error(message):
    """
    Print an error message to the console.
    This will later be replaced with GUI popups.
    """
    print(f"Error: {message}")

def capture_frame_from_webcam():
    """
    Capture a single frame from the webcam
    """
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        display_error("Webcam could not be opened.")
        return None
    print("Capturing from webcam. Press 'q' to capture and exit.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            display_error("Failed to capture frame from webcam.")
            break
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return frame

def load_image(image_path):
    """
    Load an image from a file
    """
    valid, error = validate_file_path(image_path)
    if not valid:
        display_error(error)
        return None
    valid, error = validate_image_format(image_path)
    if not valid:
        display_error(error)
        return None
    return cv2.imread(image_path)

def get_face_encodings(frame):
    """
    Detect faces in a frame and return their encodings
    """
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) == 0:
        display_error("No faces detected in the input.")
        return None
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    if len(face_encodings) == 0:
        display_error("Failed to encode face.")
        return None
    return face_encodings
