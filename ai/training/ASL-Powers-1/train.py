from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
print(model.info())

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(
    data="/Users/fahadfaruqi/hand-and-hand/ai/training/ASL-Powers-1/data.yaml",
    epochs=1,
    imgsz=640,
    device="mps",
)

# Run inference with the YOLOv8n model on the 'bus.jpg' image

results = model(
    "/Users/fahadfaruqi/hand-and-hand/ai/training/ASL-Powers-1/test/images/Screenshot-2024-09-15-00-00-01_png.rf.82534085fe74c699bd712be920c47555.jpg"
)
