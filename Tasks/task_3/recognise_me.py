import face_recognition
import picamera2
from pathlib import Path

# Create a filepath to the image from task 1
image_file = Path.home().joinpath("Hacklab/Computer Vision/test.jpg")

if image_file.exists():
    print("We found the file")

my_image = face_recognition.load_image_file(image_file)


face_locations = []
face_encodings = []

camera = picamera2.Picamera2()
capture_config = camera.create_still_configuration()

camera.start(show_preview=True)

while True:
    print("Capturing Image")
    output = camera.switch_mode_and_capture_array(capture_config, "main")

    