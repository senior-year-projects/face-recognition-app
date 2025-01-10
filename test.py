import face_recognition
import cv2

# Load an image
image = face_recognition.load_image_file("D:\Program Files\Faces\photo1.jpg")

# Detect face locations
face_locations = face_recognition.face_locations(image)

print("Detected face locations:", face_locations)
