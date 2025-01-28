import cv2
import main
import time

def detect_faces(input_source="webcam", file_path=None):
    """
    Detect faces from the specified input source
    
    Params:
        input_source (str): "webcam", "image", or "video"
        file_path (str): Path to the image or video file
    
    Returns:
        List of face locations and the processed frame
    """
    if input_source == "webcam":
        video_capture = cv2.VideoCapture(0)
        print("Press 'q' to exit.")
        
        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Error accessing the webcam.")
                break

            face_locations = main.face_locations(frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.imshow("Webcam Face Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
        return face_locations, frame

    elif input_source == "image" and file_path:
        frame = cv2.imread(file_path)
        face_locations = main.face_locations(frame)
        return face_locations, frame

    else:
        raise ValueError("Invalid input source or missing file path.")

def measure_detection_time(input_source="webcam", file_path=None):
    """
    Measure time taken
    
    Params:
        input_source (str): "webcam", "image", or "video"
        file_path (str): Path to the image or video file 
    
    Returns:
        Detection time in seconds
    """
    start_time = time.time()
    detect_faces(input_source, file_path)
    end_time = time.time()
    detection_time = end_time - start_time
    print(f"Face detection completed in {detection_time:.2f} seconds.")
    return detection_time
