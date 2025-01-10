import face_recognition
import cv2
import json
from utils import load_database, save_database

DATABASE_PATH = "face_database.json"

def register_user():
    """
    Register a new user by capturing their face and saving the encoding.
    Supports webcam, image, or video input.
    """
    # Load the existing database
    face_database = load_database(DATABASE_PATH)

    # Ask for the user's name
    name = input("Enter your name: ").strip()
    if name in face_database:
        print(f"User '{name}' already exists in the database. Please use a different name.")
        return

    # Choose input source
    print("Choose input source:")
    print("1. Webcam")
    print("2. Image file")
    print("3. Video file")
    choice = input("Enter your choice (1/2/3): ").strip()

    face_encoding = None

    if choice == "1":  # Webcam
        video_capture = cv2.VideoCapture(0)
        print("Press 'q' to capture your face and register.")

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Error accessing the webcam.")
                break

            face_locations = face_recognition.face_locations(frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.imshow("Registration - Press 'q' to capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if len(face_locations) == 0:
                    print("No face detected. Please try again.")
                    continue

                face_encodings = face_recognition.face_encodings(frame, face_locations)
                face_encoding = face_encodings[0]
                print("Face captured successfully.")
                break

        video_capture.release()
        cv2.destroyAllWindows()

    elif choice == "2":  # Image file
        file_path = input("Enter the path to the image file: ").strip()
        frame = cv2.imread(file_path)
        if frame is None:
            print("Error reading the image file.")
            return

        face_locations = face_recognition.face_locations(frame)
        if len(face_locations) == 0:
            print("No face detected in the image.")
            return

        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_encoding = face_encodings[0]
        print("Face captured successfully.")

    elif choice == "3":  # Video file
        file_path = input("Enter the path to the video file: ").strip()
        video_capture = cv2.VideoCapture(file_path)
        print("Press 'q' to capture your face from the video.")

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                print("End of video or error reading the file.")
                break

            face_locations = face_recognition.face_locations(frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.imshow("Registration - Press 'q' to capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if len(face_locations) == 0:
                    print("No face detected. Please try again.")
                    continue

                face_encodings = face_recognition.face_encodings(frame, face_locations)
                face_encoding = face_encodings[0]
                print("Face captured successfully.")
                break

        video_capture.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid choice. Please restart the registration process.")
        return

    # Save the encoding if successfully captured
    if face_encoding is not None:
        face_database[name] = face_encoding.tolist()
        save_database(DATABASE_PATH, face_database)
        print(f"User '{name}' registered successfully.")
    else:
        print("Registration failed. No face captured.")

if __name__ == "__main__":
    register_user()
