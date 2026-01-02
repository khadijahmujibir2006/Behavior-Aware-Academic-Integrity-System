#  Behavior-Aware Academic Integrity System

##  Overview
The **Behavior-Aware Academic Integrity System** is an advanced **computer vision–based monitoring framework** designed to detect and analyze **suspicious behaviors during academic examinations**.

Unlike traditional proctoring systems that rely only on object detection or screen monitoring, this system performs **behavioral analysis** by combining **object detection, tracking, classification, and temporal behavior modeling** to ensure exam integrity in both **offline and online examination environments**.

---

##  Problem Statement
Academic institutions face increasing challenges in maintaining exam integrity due to:
- Cheating using mobile phones or external devices
- Impersonation and multiple-person presence
- Abnormal head and eye movements
- Lack of intelligent, automated monitoring systems

Conventional proctoring solutions are often **static**, **rule-based**, and fail to understand **human behavior patterns**.

---

##  Proposed Solution
This project introduces a **behavior-aware vision system** that continuously monitors a student through a camera feed and intelligently identifies **potential integrity violations**.

The system does not merely detect objects—it **understands behavior over time** by tracking movements, analyzing posture, and classifying actions as **normal or suspicious**.

---

##  System Architecture
Camera Input
↓
Face & Person Detection
↓
Object Detection (Phone, Multiple Persons)
↓
Object & Head Movement Tracking
↓
Behavior Classification Engine
↓
Integrity Risk Assessment & Alerts

yaml
Copy code

---

##  Key Features
- Real-time face and person detection
- Mobile phone detection during exams
- Multi-person presence detection
- Head movement and gaze direction tracking
- Behavioral classification (Normal / Suspicious)
- Temporal behavior analysis across frames
- Visual alerts and integrity status indicators

---

##  Computer Vision Tasks Used
### 🔹 Image Classification
Classifies observed behavior patterns as **normal** or **suspicious**.

### 🔹 Object Detection
Detects:
- Face
- Person
- Mobile phone
- Unauthorized objects

### 🔹 Object Tracking
Tracks:
- Student head movement
- Face position across frames
- Detected objects over time

### 🔹 Behavioral Analysis
Uses temporal patterns to detect:
- Frequent looking away
- Repeated downward gaze
- Presence of multiple individuals
- Suspicious object usage

---

##  Core Computer Science Concepts
- Computer Vision and Image Processing
- Machine Learning–based Classification
- Temporal Data Analysis
- Data Structures for Tracking (IDs, queues)
- System Design and Real-Time Processing
- Ethical AI and Responsible Monitoring

---

##  Technologies Used
- Python 3.x
- OpenCV
- NumPy
- Deep Learning models (CNN-based)
- Tracking algorithms (CSRT / DeepSORT)
- Streamlit / Flask (for dashboard visualization)

---

##  How the System Works
1. Captures live video feed
2. Detects faces, persons, and objects
3. Tracks movements frame-by-frame
4. Analyzes behavior patterns over time
5. Flags suspicious activities
6. Displays alerts and integrity status

---

##  Applications
- Online examination proctoring
- University and school exam halls
- Remote assessments
- Certification platforms
- Secure testing environments

---

##  Why This Project Is Unique
- Focuses on **behavioral intelligence**, not just detection
- Integrates multiple CV tasks into a single system
- Real-world ethical and educational impact
- Highly relevant to current online education challenges
- Strong balance of **AI + system design**

---

##  Ethical Considerations
- Designed strictly for academic integrity
- No biometric data stored permanently
- Operates under institutional guidelines
- Emphasizes responsible AI usage

---

##  Author
**Khadijah Mujibir Rahiman**  
B.E. Computer Science and Engineering  

---

##  Conclusion
The Behavior-Aware Academic Integrity System demonstrates how advanced computer vision and behavioral analysis can be responsibly applied to strengthen academic integrity. By understanding *how* students behave rather than merely *what* they do, the system provides a more intelligent, adaptive, and ethical approach to exam monitoring.
