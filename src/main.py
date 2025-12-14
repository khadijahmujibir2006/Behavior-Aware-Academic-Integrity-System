import cv2
import mediapipe as mp
import math
import os
import time
from datetime import datetime

# ================= PATH SETUP =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "alerts.log")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================= LOG FUNCTION =================
def log_alert(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

# ================= MEDIAPIPE =================
mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

face_mesh = mp_face.FaceMesh(refine_landmarks=True)
hands = mp_hands.Hands(max_num_hands=2)

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
print("✅ Camera started. Press Q to quit.")

# ================= TIMERS =================
gaze_start = None
head_start = None

# ================= MAIN LOOP =================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_result = face_mesh.process(rgb)
    hand_result = hands.process(rgb)

    suspicious = False
    status = "✅ Normal Behavior"
    color = (0, 255, 0)

    # ================= FACE & EYE ANALYSIS =================
    if face_result.multi_face_landmarks:
        landmarks = face_result.multi_face_landmarks[0].landmark

        # Nose landmark
        nose = landmarks[1]
        nose_x, nose_y = int(nose.x * w), int(nose.y * h)

        # Eye landmarks
        left_eye = landmarks[33]
        right_eye = landmarks[263]

        eye_center_x = int((left_eye.x + right_eye.x) / 2 * w)
        face_center_x = nose_x

        # ---------- Eye Gaze ----------
        if abs(eye_center_x - face_center_x) > 30:
            if gaze_start is None:
                gaze_start = time.time()
            elif time.time() - gaze_start > 2:
                suspicious = True
                status = "👁️ Looking Away (Eye Gaze)"
                color = (0, 0, 255)
                log_alert("Eye gaze deviation detected")
        else:
            gaze_start = None

        # ---------- Head Down ----------
        if nose_y > h * 0.6:
            if head_start is None:
                head_start = time.time()
            elif time.time() - head_start > 2:
                suspicious = True
                status = "⬇️ Head Down (Possible Reading)"
                color = (0, 0, 255)
                log_alert("Head down detected")
        else:
            head_start = None

        # Draw nose
        cv2.circle(frame, (nose_x, nose_y), 5, (255, 0, 0), -1)

    else:
        suspicious = True
        status = "❌ Candidate Missing"
        color = (0, 0, 255)
        log_alert("Candidate missing")

    # ================= HAND ANALYSIS =================
    if hand_result.multi_hand_landmarks and face_result.multi_face_landmarks:
        for handLms in hand_result.multi_hand_landmarks:
            for lm in handLms.landmark:
                hx, hy = int(lm.x * w), int(lm.y * h)
                if math.dist((hx, hy), (nose_x, nose_y)) < 120:
                    suspicious = True
                    status = "📱 Hand Near Face (Possible Phone)"
                    color = (0, 0, 255)
                    log_alert("Hand near face detected")
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    # ================= DISPLAY =================
    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Behavior-Aware Academic Integrity System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
