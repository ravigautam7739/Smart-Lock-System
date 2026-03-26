# 🔒 Smart Lock System (Face Detection | Python + OpenCV)

A Python-based **Smart Lock System** that automatically locks your computer when no face is detected for a few seconds.

This project uses **computer vision** to enhance security by ensuring that your system is locked when you are not present.

---

# 🚀 Features

✔ Real-time face detection using webcam
✔ Detects user presence continuously
✔ Automatically locks system after inactivity
✔ Mirror camera effect for better interaction
✔ Lightweight and efficient

---

# 🛠 Technologies Used

* Python
* OpenCV
* Haar Cascade Classifier
* OS module (system locking)

---

# 📂 Project Structure

```id="z8n2ps"
smart-lock-system
│
├── smart_lock.py
└── README.md
```

---

# ⚙️ Installation

1️⃣ Install **Python 3.x**

2️⃣ Install OpenCV:

```bash id="2k2m4q"
pip install opencv-python
```

---

# ▶️ How to Run

```bash id="3s1wyy"
git clone https://github.com/ravigautam7739/smart-lock-system.git
cd smart-lock-system
python smart_lock.py
```

---

# 🧠 How It Works

1. The webcam starts capturing live video.
2. The program detects faces using **Haar Cascade**.
3. If a face is detected → system stays active
4. If no face is detected for **5 seconds**:

   * The system automatically locks
5. Uses Windows command to lock the workstation

---

# 💻 Example Output

```id="z9n7qh"
User Present
User Present
No Face Detected...
No Face Detected...

Locking System 🔒
```

---

# ⚠️ Important Notes

* Works on **Windows systems only** (uses `LockWorkStation`)
* Requires webcam access
* Good lighting improves face detection accuracy

---

# 🎯 Use Cases

* Personal computer security
* Smart office systems
* Privacy protection
* AI-based automation projects

---

# 🔮 Future Improvements

* Face recognition (specific user detection)
* Adjustable timeout duration
* Cross-platform support
* GUI interface
* Mobile alerts

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly post **Python, AI, and automation projects** on social media.

Stay tuned 🚀
