 Behavior-Aware Academic Integrity System

A real-time computer vision–based proctoring system that monitors examinee behavior during online exams and detects suspicious activities using behavioral analysis instead of heavy object detection.

This project focuses on explainable AI, combining face landmarks, eye gaze, head movement, and hand proximity analysis to ensure academic integrity.

 Key Features

 Live webcam monitoring

 Face presence detection

 Multiple person detection

 Eye gaze tracking (looking away)

 Head movement detection (head down / turned)

 Hand near face detection (possible phone usage)

 Time-based suspicious behavior analysis

 Alert logging for audit purposes

 Explainable, rule-based AI logic

 Why This Project Is Unique

Unlike traditional proctoring systems that rely only on object detection, this system:

Focuses on behavioral patterns

Uses simple, explainable rules

Avoids heavy deep learning models

Works efficiently on CPU

Is easy to justify in exams and interviews

This makes it suitable for academic use, demos, and research-oriented evaluation.

⚙️ Technology Stack

Python 3.10

OpenCV

MediaPipe

NumPy

Git & GitHub

 System Architecture (High-Level)
Webcam Feed
     ↓
Face & Hand Detection (MediaPipe)
     ↓
Behavior Analysis (Rules + Timers)
     ↓
Real-Time Alerts on Screen
     ↓
Alert Logging (outputs/alerts.log)

 Behaviors Detected
Behavior	Description
Normal Behavior	Single face, stable gaze
Candidate Missing	No face detected
Multiple Faces	More than one face in frame
Eye Gaze Deviation	Looking left/right repeatedly
Head Down	Possible reading or phone usage
Hand Near Face	Possible phone usage
Prolonged Suspicion	Behavior persists over time
 How to Run the Project
1️ Clone the Repository
git clone https://github.com/khadijahmujibir2006/Behavior-Aware-Academic-Integrity-System.git
cd Behavior-Aware-Academic-Integrity-System

2️ Install Dependencies
pip install -r requirements.txt

3️ Run the System
py -3.10 src/main.py


 Press Q to exit the camera window.

 Project Structure
Behavior-Aware-Academic-Integrity-System/
├── src/
│   └── main.py
├── outputs/
│   └── alerts.log   (generated at runtime)
├── data/
├── models/
├── README.md
├── requirements.txt
└── .gitignore

 Output & Logging

The system generates alerts during runtime

Alerts are stored locally in:

outputs/alerts.log


Logs are intentionally excluded from GitHub using .gitignore

This follows professional version control practices

📸 Sample Output (Recommended)

You can add screenshots of:

Normal behavior

Eye gaze alert

Hand near face alert

Place them in an assets/ folder and link them here.

 Use Cases

Online examinations

Remote proctoring systems

Academic integrity monitoring

Behavior analysis research

Computer vision demonstrations

 Future Enhancements

Eye blink frequency analysis

Emotion detection

Admin dashboard with charts

Multiple camera support

Cloud-based alert storage

 Interview & Viva Highlights

“This project uses behavior-based AI instead of pure object detection, making it explainable, efficient, and suitable for academic integrity monitoring.”

 Author

Khadijah Mujibir Rahiman
B.E. Computer Science and Engineering
St. Joseph’s Institute of Technology

GitHub: khadijahmujibir2006

 Acknowledgements

OpenCV

MediaPipe

GitHub Open Source Community


