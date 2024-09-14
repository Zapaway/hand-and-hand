import tensorflow as tf
import numpy as np
# from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

# Load the model
model = tf.saved_model.load('saved_model.pb')

# Load the label map
# category_index = label_map_util.create_category_index_from_labelmap('.../label_map.pbtxt')

# Run inference on an image
image_np = "hand.jpg" # Load your image
input_tensor = tf.convert_to_tensor(image_np)
input_tensor = input_tensor[tf.newaxis, ...]
detections = model(input_tensor)

# Visualize the results
viz_utils.visualize_boxes_and_labels_on_image_array(
    image_np,
    detections['detection_boxes'][0].numpy(),
    detections['detection_classes'][0].numpy().astype(np.int32),
    detections['detection_scores'][0].numpy(),
    # category_index,
    use_normalized_coordinates=True,
    max_boxes_to_draw=200,
    min_score_thresh=.30,
    agnostic_mode=False
)

