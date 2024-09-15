from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(source=1, show=True, conf=0.4)
