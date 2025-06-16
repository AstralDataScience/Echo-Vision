# 🔍 Echo Vision: Empowering the Visually Impaired with AI

**Echo Vision** is an AI-powered object detection system built to assist **visually impaired individuals** in recognizing real-world objects through live video, static images, or uploaded footage. With a mission to promote **independent mobility and spatial awareness**, this project combines **YOLOv8**, **Streamlit**, and **Pascal VOC 2012** dataset in a seamless, user-friendly web interface.

---

## 📌 Project Highlights

- ✅ **Real-Time Object Detection** via webcam, images, and videos
- 🎯 Supports 20 object classes (e.g., person, dog, car, chair, etc.)
- 🌐 Built with **Streamlit** for rapid deployment and ease of use
- ⚡️ Powered by **YOLOv8** for high-speed, high-accuracy detection
- 🧠 Designed with the vision to integrate into wearable IoT devices (e.g., smart glasses)

---

## 🚀 Demo

> Coming soon: Voice-assisted live demo via wearable prototype (under development)

---

## 📸 Preview

![Echo Vision Screenshot](preview.png)  
_> Interface preview showing live detection results via webcam_

---

## 🛠️ Tech Stack

| Component       | Technology        |
|-----------------|-------------------|
| Frontend        | Streamlit         |
| Object Detection| YOLOv8 (Ultralytics) |
| Language        | Python            |
| Dataset         | Pascal VOC 2012   |
| Model Training  | Pre-trained YOLOv8|
| Deployment      | Localhost / Streamlit Cloud (planned) |

---

## 🎯 Object Classes Detected

`person`, `car`, `bus`, `train`, `bicycle`, `motorbike`, `dog`, `cat`, `chair`, `sofa`,  
`bird`, `cow`, `sheep`, `horse`, `bottle`, `pottedplant`, `diningtable`, `aeroplane`, `boat`, `tvmonitor`

---

## 📁 Dataset

This project uses the [Pascal VOC 2012 dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/), a benchmark in object classification and detection.

> ⚠️ Due to size constraints, the dataset is not included here.  
Please download it from the official source and place the extracted folder as:

---

## 🧠 Under Development

- 🔊 **Voice Feedback Integration** — Real-time audio descriptions of detected objects
- 🕶️ **Smart Glass Integration** — IoT prototype with micro-camera and speaker
- 📍 **GPS-Enabled Navigation** — Directional assistance for outdoor movement

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/AstralDataScience/Echo-Vision.git
   cd Echo-Vision

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run main.py

🙌 Contribution
Have ideas to improve Echo Vision?
Feel free to fork the repo, open issues, or submit a pull request.

📃 License
This project is licensed under the MIT License — free to use, modify, and distribute.
See the full license text in the LICENSE file.

👤 About the Author
Kaihkasha Parveen Mohd Nazre Alam
Aspiring data scientist and socially driven tech innovator. Passionate about building accessible AI solutions for real-world challenges.

🔗 LinkedIn
💻 GitHub

