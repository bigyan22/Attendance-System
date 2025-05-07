# Face Recognition Attendance System

This is a real-time face recognition-based attendance system using Python, OpenCV, and the `face_recognition` library. It uses your webcam to detect and recognize faces from a known dataset, and logs attendance with timestamps in a CSV file automatically.

---

## 💡 Features

- Real-time face detection and recognition via webcam
- Automatic attendance marking with timestamp
- Saves daily attendance in date-wise CSV files
- Scalable: Add more images to the `faces/` folder to enroll more people

---

## 🚀 How It Works

1. Place all known face images in the `faces/` folder. Filenames should be the name of the person (e.g., `Alice.jpg`, `Bob.png`).
2. Run the Python script.
3. The system will capture video using your webcam, detect faces, and match them with the known dataset.
4. Attendance is recorded once per session per person.
5. A CSV file is created for the current date in the `CSVFILES/` folder with time logs.

---

## 🗂 Project Structure

```
attendance-system/
│
├── faces/                         # Folder containing known face images
│   ├── Ram.jpg
│   ├── Shyam.png
│   └── ...
│
├── CSVFILES/                      # Auto-generated folder for daily attendance CSVs
│   └── 2025-05-07.csv            
│
├── main.py                        # Script that contains the main code
│
├── requirements.txt               # List of required Python libraries
│
├── README.md                      # Project documentation
```

## Run the Project
- Clone or download this repository in your local machine by using the command
```bash
git clone https://github.com/bigyan22/Attendance-System.git
``` 
- Navigate to the project directory by using the command
```bash
cd Attendance-System
```
- Finally run the app using command
```bash
python main.py
```
## Contribution
Feel free to contribute.