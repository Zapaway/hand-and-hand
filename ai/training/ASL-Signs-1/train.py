from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
print(model.info())

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="/home/mouadtiahi/hand-and-hand/hand-and-hand/ai/training/ASL-Signs-1/data.yaml", epochs=50, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image

results = model("path/to/bus.jpg")