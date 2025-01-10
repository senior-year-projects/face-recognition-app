import face_recognition
import cv2
import numpy as np
from utils import load_database

DATABASE_PATH = "face_database.json"

def authenticate_user():
    """
    Authenticate a user by matching their face with stored encodings
    Supports webcam, image, or video input
    """
    # Load the face database
    face_database = load_database(DATABASE_PATH)

    if not face_database:
        print("No registered users found in the database.")
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
        print("Press 'q' to authenticate.")

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Error accessing the webcam.")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

            cv2.imshow("Authentication - Press 'q' to capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if len(face_locations) == 0:
                    print("No face detected. Please try again.")
                    continue

                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
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

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        if len(face_locations) == 0:
            print("No face detected in the image.")
            return

        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        face_encoding = face_encodings[0]
        print("Face captured successfully.")

    elif choice == "3":  # Video file
        file_path = input("Enter the path to the video file: ").strip()
        video_capture = cv2.VideoCapture(file_path)
        print("Press 'q' to authenticate.")

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                print("End of video or error reading the file.")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

            cv2.imshow("Authentication - Press 'q' to capture", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if len(face_locations) == 0:
                    print("No face detected. Please try again.")
                    continue

                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                face_encoding = face_encodings[0]
                print("Face captured successfully.")
                break

        video_capture.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid choice. Please restart the authentication process.")
        return

    # Compare the captured face encoding with stored encodings
    if face_encoding is not None:
        for name, stored_encoding in face_database.items():
            matches = face_recognition.compare_faces([np.array(stored_encoding)], face_encoding)
            face_distance = face_recognition.face_distance([np.array(stored_encoding)], face_encoding)

            if matches[0]:
                print(f"Authentication successful! Welcome, {name}.")
                print(f"Match confidence: {1 - face_distance[0]:.2%}")
                return

        print("Authentication failed. No match found.")
    else:
        print("Authentication failed. No face captured.")

if __name__ == "__main__":
    authenticate_user()
