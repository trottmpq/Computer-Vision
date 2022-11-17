import face_recognition
import picamera2
from pathlib import Path

# Create a filepath to the image from task 1
image_file = Path.home().joinpath("Hacklab/Computer Vision/test.jpg")

if image_file.exists():
    print("We found the file")

my_image = face_recognition.load_image_file(image_file)
my_image_encodings = face_recognition.face_encodings(my_image)[0]

face_locations = []
face_encodings = []

camera = picamera2.Picamera2()
capture_config = camera.create_still_configuration()

camera.start(show_preview=True)

while True:
    print("Capturing Image")
    output = camera.switch_mode_and_capture_array(capture_config, "main")

    face_locations = face_recognition.face_locations(output)
    print(f"found {len(face_locations)} in the image")
    face_encodings = face_recognition.face_encodings(output, face_locations)

    for face_encodeing in face_encodings:
        comparison = face_recognition.compare_faces([my_image_encodings], face_encodeing)
        name = "Unknown Person"

        if comparison[0]:
            name = "ME!"

        print(f"I see someone named {name}")