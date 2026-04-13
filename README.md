# 🚗 Vehicle Detection & Speed Tracking System

A real-time vehicle detection and speed estimation system built with **YOLOv8** and **OpenCV**, with an interactive **Streamlit dashboard** for traffic analysis.

---

## 📌 Features

- Detects vehicles (cars, buses, trucks) in video footage using YOLOv8
- Tracks each vehicle with a unique ID
- Calculates speed in **km/h** using two reference lines
- Classifies direction of movement (**up** / **down**)
- Logs all detections to a CSV file
- Interactive dashboard to visualize traffic data

---

## 🗂️ Project Structure

```
vehicle-detection/
├── main.ipynb          # Main detection & tracking notebook
├── dashboard.py        # Streamlit dashboard for visualization
├── vehicle_data.csv    # Sample output data
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/vehicle-detection.git
   cd vehicle-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 model** (auto-downloads on first run)
   ```bash
   # Model used: yolov8s.pt (downloaded automatically by ultralytics)
   ```

---

## 🚀 Usage

### 1. Run Detection (Jupyter Notebook)

Open `main.ipynb` in Jupyter or Google Colab and run all cells.

- Update the video path in Cell 6:
  ```python
  cap = cv2.VideoCapture("your_video.mp4")
  ```
- The notebook will generate:
  - `output_vid.mp4` — annotated output video
  - `vehicle_data.csv` — detection log

### 2. Launch Dashboard

```bash
streamlit run dashboard.py
```

Make sure `vehicle_data.csv` and `output_vid.mp4` are in the same directory.

---

## 📊 Dashboard Preview

The Streamlit dashboard includes:
- 📋 Raw vehicle data table
- 📊 Vehicle type distribution (bar chart)
- 🔄 Traffic direction analysis (bar chart)
- 📈 Speed distribution (line chart)
- 🎬 Processed detection video playback

---

## 🧠 How Speed is Calculated

Two horizontal lines are drawn across the video frame:

```
Red Line  (y=198) ──────────────────────
Blue Line (y=268) ──────────────────────
```

When a vehicle crosses both lines, the elapsed time is recorded and speed is estimated assuming a fixed real-world distance between the lines:

```
speed (km/h) = (distance_meters / elapsed_time_seconds) × 3.6
```

---

## 📦 Requirements

```
ultralytics>=8.0.0
opencv-python>=4.8.0
pandas>=2.0.0
streamlit>=1.28.0
numpy>=1.24.0
```

---

## 📁 Output Data Format

| Column        | Description                        |
|---------------|------------------------------------|
| `timestamp`   | Unix timestamp of detection        |
| `vehicle_id`  | Unique tracker ID                  |
| `vehicle_type`| car / bus / truck                  |
| `direction`   | up / down                          |
| `speed_kmh`   | Estimated speed in km/h            |

---

## 📝 Notes

- Video file (`output_vid.mp4`) and model weights (`yolov8s.pt`) are **not included** in this repo due to file size limits.
- The notebook was developed and tested on **Google Colab**.
- Adjust `red_line_y`, `blue_line_y`, and `distance` values to match your video's scale.

---

## 🛠️ Built With

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)