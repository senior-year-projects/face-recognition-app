import cv2
import time
import os

# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces_image(image_path):
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            print("Error: Image file not found.")
            return

        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Could not load the image.")
            return

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Start timing
        start_time = time.time()

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # End timing
        end_time = time.time()

        if len(faces) == 0:
            print("No faces detected in the image.")
            return

        print(f"Face detection took {end_time - start_time:.2f} seconds.")

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the image
        cv2.imshow("Detected Faces - Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to detect faces in a video file
def detect_faces_video(video_path):
    try:
        # Check if the file exists
        if not os.path.exists(video_path):
            print("Error: Video file not found.")
            return

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Could not open the video file.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video.")
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Start timing
            start_time = time.time()

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # End timing
            end_time = time.time()

            if len(faces) == 0:
                print("No faces detected in this frame.")
                continue

            print(f"Frame processed in {end_time - start_time:.2f} seconds.")

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the frame
            cv2.imshow("Detected Faces - Video", frame)

            # Break on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to detect faces using the webcam
def detect_faces_webcam():
    try:
        # Open the webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not access the webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Start timing
            start_time = time.time()

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # End timing
            end_time = time.time()

            if len(faces) == 0:
                print("No faces detected in this frame.")
                continue

            print(f"Frame processed in {end_time - start_time:.2f} seconds.")

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the frame
            cv2.imshow("Detected Faces - Webcam", frame)

            # Break on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to choose input option
def main():
    print("Choose input option:")
    print("1. Image")
    print("2. Video")
    print("3. Webcam")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        image_path = input("Enter the path to the image: ")
        detect_faces_image(image_path)
    elif choice == '2':
        video_path = input("Enter the path to the video: ")
        detect_faces_video(video_path)
    elif choice == '3':
        detect_faces_webcam()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()