from ultralytics import YOLO

model = YOLO("/Users/fahadfaruqi/hand-and-hand/runs/detect/train14/weights/best.pt")

result = model("fingies.jpg")  # return a list of Results objects

boxes = result[0].boxes
print(boxes.data[:, 4:6])
