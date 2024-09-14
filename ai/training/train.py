import tensorflow as tf
import numpy as np
from object_detection.utils import visualization_utils as viz_utils
import cv2
import os

PATH = os.getcwd()
if os.path.exists(PATH):
    model = tf.saved_model.load(PATH)
else:
    raise Exception("Model is missing!")

image_path = "hand.jpg"
image_np = cv2.imread(image_path)
if image_np is None:
    raise Exception(f"Image {image_path} not found!")

# Convert the image to a tensor
input_tensor = tf.convert_to_tensor(image_np)
input_tensor = input_tensor[tf.newaxis, ...]  # Add batch dimension

# Get predictions from the model
detections = model(input_tensor)

# Print the detections (predicted values)
print(detections)

# Example: If you want to see specific details such as detection scores, boxes, or classes
print("Detection Boxes:", detections["detection_boxes"].numpy())
print("Detection Scores:", detections["detection_scores"].numpy())
print("Detection Classes:", detections["detection_classes"].numpy())
