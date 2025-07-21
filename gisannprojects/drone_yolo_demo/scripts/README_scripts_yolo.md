# Scripts – Drone YOLO Demo

This folder contains Python scripts used to train, predict and prepare data for object detection using YOLOv8s.

---

## Files Included

### `code-xtract40images.py`
Extracts a subset of 40 aerial images containing a specific object class (e.g., airplanes) from a larger DOTA-style dataset.

- Looks for labels containing "plane"
- Copies the matched image and label file
- Outputs image list to `images.txt`

To run:
```bash
python code-xtract40images.py
```

---
### `train_yolo.py`
Trains a YOLOv8 model using a custom dataset defined in `mini_train/data.yaml`.

- Uses YOLOv8s base model
- Trains for 50 epochs
- Outputs model weights and training logs to `results/`

To run:
```bash
python train_yolo.py
```

---
### predict_yolo.py

This script confirms you have installed and  using the correct YOLO version (YOLOv8) and prints metadata about the model, including its type (`yolov8s`) and approximate performance (~28.6 GFLOPS).

```python
# Check installed YOLO version
import ultralytics
print("Ultralytics YOLO version:", ultralytics.__version__)

# Load trained YOLOv8 model and inspect details
from ultralytics import YOLO
model = YOLO(r"C:\path\to\your\best.pt")
print(model.info())
```

---
### `predict.py`
### Used in the actual demo.
Performs inference using a trained YOLOv8 model on input images and displays predictions.
- Loads model from `weights/best.pt`
- Loads input image from specified path
- Outputs annotated predictions to `results/`
- Displays image with bounding boxes ( via IPython in notebook)

To run:
```bash
python predict.py
```

---


## Notes

- All scripts use relative paths where possible for GitHub compatibility.
- `.ipynb_checkpoints/` is ignored via `.gitignore`.
- Modify paths inside scripts if your project layout differs.

