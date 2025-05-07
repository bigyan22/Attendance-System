import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_cap = cv2.VideoCapture(0)

known_face_encodings=[]
known_face_names=[]

#Loading the known faces
faces_folder = 'faces'
for filename in os.listdir(faces_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        path = os.path.join(faces_folder, filename)
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)
        
        if encoding:  # Only proceed if face is detected
            known_face_encodings.append(encoding[0])
            name = os.path.splitext(filename)[0]  # "Ram.jpg" -> "Ram"
            known_face_names.append(name)
        else:
            print(f"[!] No face found in {filename}")



# list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
folder_path = 'CSVFILES'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
f= open(f"{folder_path}/{current_date}.csv", 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    _ , frame = video_cap.read()
    
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name + ' Presented at ' + current_time + '.'])

        # Scale back up face locations since the frame was scaled down to 1/4
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw rectangle around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.putText(
                    frame,
                    name + ' Present',
                    (left, top - 10),  
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )
    cv2.imshow('Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_cap.release()
cv2.destroyAllWindows()

