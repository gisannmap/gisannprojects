# 1. Project YOLO Demo

This project contains a working demo project for object detection using YOLOv8 on aerial images. The goal is to detect airplanes in overhead images using trained weights and visualize the results.

---

## Directory Structure
```
drone_yolo_demo/
├── yolonotebooks/       # Jupyter Notebooks for inference and visualization
├── yolodata/            # Input images and data for testing
├── weights/             # Trained YOLOv8 model weights
├── results/             # Prediction outputs and annotated results
├── scripts/             # Python scripts for prediction and utilities
│   ├── predict.py
│   └── predict_yolo.py
├── environment.yml      # Environment file to recreate conda setup
├── README.md            # Project documentation
```

---

## Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/yourusername/drone_yolo_demo.git
cd drone_yolo_demo
```
2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate drone_yolo_env
```
3. Open and run the Jupyter notebooks from 
[`yolonotebooks/`](./yolonotebooks) for demo inference.

---

## Included Scripts

### `scripts/predict.py`
Runs YOLOv8 prediction on an input image using a given trained model weight and saves the output annotated images and text files.

### `scripts/predict_yolo.py`
This utility script is used to check the Ultralytics YOLO version installed and load a YOLOv8 model file to inspect its internal structure and capabilities using `model.info()`.

Useful for identifying and verifying model weights before inference or debugging model compatibility.

---

## .gitignore Highlights
- Trained weights and large image datasets excluded
- Intermediate output results not tracked
- Cache folders and Jupyter checkpoints ignored

---

## License
MIT License

---


## Scripts Overview
The `scripts/` folder contains utility and core scripts used across the project:

| Script File               | Description |
|---------------------------|-------------|
| `predict.py`              | Main script for running object detection using trained YOLOv8 weights. |
| `predict_yolo.py`         | Displays YOLO version used and prints model architecture info (`model.info()`). Useful for verifying model structure. |
| `train_yolo.py`           | Script used to train the model on a local dataset (not included in this repo). Includes configurations for image size, epochs, and paths. |
| `code-xtract40images.py`  | Utility to extract 40 sample images from the dataset for testing and demonstration. |
| `README_scripts_yolo.md`  | This markdown file documents the above scripts (for developers or future contributors). |
## Detailed Script Documentation

See the [YOLO Scripts Documentation](scripts/README_scripts_yolo.md) for a detailed breakdown of Python scripts used in this project.
# gisannprojects
Showcasing projects undertaken :)
