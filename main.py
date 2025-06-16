import streamlit as st
import cv2
from PIL import Image
from ultralytics import YOLO
import numpy as np
import tempfile

# Load YOLOv8 model
model_path = r"C:\\Users\\K KASHA\\OneDrive - Vidyalankar School of Information Technology\\Desktop\\SEM 6 project\\runs\\detect\\train15\\weights\\best.pt"
model = YOLO(model_path)

# Custom CSS for modern UI
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        width: 100%;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stSlider {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("🚀 EchoVision Interface")
    st.write("### Detect objects using state-of-the-art YOLOv8 model")

    # Sidebar for better organization
    st.sidebar.title("🔧 Settings")
    confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.05)
    detection_mode = st.sidebar.selectbox("Choose Detection Mode", [
        "Upload Image for Detection", "Use Live Camera for Detection", "Upload Video for Detection"
    ])

    # Main Content UI
    if detection_mode == "Upload Image for Detection":
        st.subheader("📷 Upload an Image for Detection")
        uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Convert image to OpenCV format
            image_cv = np.array(image.convert("RGB"))
            
            # Run YOLO inference
            results = model.predict(image_cv, conf=confidence_threshold)
            annotated_image = results[0].plot()

            st.image(annotated_image, caption="Detection Result", use_column_width=True)

    elif detection_mode == "Use Live Camera for Detection":
        st.subheader("🎥 Live Camera Object Detection")
        start_camera = st.button("Start Camera")
        stop_camera = st.button("Stop Camera")

        if start_camera:
            cap = cv2.VideoCapture(0)
            stframe = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to open camera.")
                    break

                # Run YOLO inference
                results = model.predict(frame, conf=confidence_threshold)
                annotated_frame = results[0].plot()

                # Convert to RGB for Streamlit display
                frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                stframe.image(frame_rgb, channels="RGB", use_column_width=True)

                if stop_camera:
                    cap.release()
                    cv2.destroyAllWindows()
                    st.success("Camera Stopped.")
                    break

    elif detection_mode == "Upload Video for Detection":
        st.subheader("🎬 Upload a Video for Detection")
        uploaded_video = st.file_uploader("Choose a video", type=["mp4", "avi", "mov", "mkv"], label_visibility="collapsed")

        if uploaded_video is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_video.read())
            
            cap = cv2.VideoCapture(tfile.name)
            stframe = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = model.predict(frame, conf=confidence_threshold)
                annotated_frame = results[0].plot()

                frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                stframe.image(frame_rgb, channels="RGB", use_column_width=True)
            
            cap.release()

if __name__ == "__main__":
    main()


