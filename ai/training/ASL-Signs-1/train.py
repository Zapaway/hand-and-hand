from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8s.pt")

# Display model information (optional)
print(model.info())

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="/home/mouadtiahi/hand-and-hand/hand-and-hand/ai/training/ASL-Signs-1/data.yaml", epochs=5, imgsz=640)


# Run inference with the YOLOv8n model on the 'bus.jpg' image
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk

# results = model("hands.jpg")