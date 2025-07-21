# predict.py (inside scripts/)
from ultralytics import YOLO
import os

def run_prediction(model_path, image_path, output_dir, conf=0.4, imgsz=640):
    model = YOLO(model_path)

    results = model.predict(
        source=image_path,
        save=True,
        save_txt=True,
        project=output_dir,
        name='predict_output',
        imgsz=imgsz,
        conf=conf
    )

    return results
