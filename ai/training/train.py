"""
- [ ] pd load all the data, train and val 
    -> no testing data cause that's for the demo night :)))
- [ ] how to set custom labels in yolo?
    -> check documentation
- [ ] feed the training data into the model
- [ ] check against validation
- [ ] return model & score
- [ ] data is in two forms, RGB and IR
    -> final goal is the ensemble model
    -> maybe i can combine the image?
    -> overlay the images over each other?!!?
    -> 
"""


class Train:
    import pandas as pd

    def __init__(self):
        from ultralytics import YOLO
        import os

        self.model = YOLO("yolov8n.pt")
        path = os.path.join(os.getcwd(), "data.yaml")
        if not os.path.exists(os.path.join(os.getcwd(), "data.yaml")):
            print(path)
            raise Exception("data.yaml missing, should be in the current directory")

    # Run batched inference on a list of images

    def train(self, num_epochs=50):
        # device = mps is for APPLE M series only
        self.model.train(data="data.yaml", epochs=num_epochs, imgsz=640, device="mps")

    def test(self):
        # Process results list
        results = self.model(["hands.jpg"])
        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            result.show()  # display to screen
            print(probs)


if __name__ == "__main__":
    t = Train()
    t.train(2)
    t.test()
