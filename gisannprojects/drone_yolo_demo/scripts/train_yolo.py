#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os

# === Paths ===
base_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train"
full_json_path = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\xtract_40\DOTA_1.0.json"
train_images_folder = os.path.join(base_dir, "images", "train")
val_images_folder = os.path.join(base_dir, "images", "val")
annotations_folder = os.path.join(base_dir, "annotations")

# Output files
train_json_output = os.path.join(annotations_folder, "instances_train.json")
val_json_output = os.path.join(annotations_folder, "instances_val.json")

#####safe EXIT
if os.path.exists(train_json_output) and os.path.exists(val_json_output):
    print("Split JSON files already exist. Skipping split process.")
else:
    # Run only if files don't exist
    extract_split(train_images_folder, train_json_output, "Training")
    extract_split(val_images_folder, val_json_output, "Validation")
    #########


# Make sure output folder exists
os.makedirs(annotations_folder, exist_ok=True)

# === Load original full JSON ===
with open(full_json_path, 'r') as f:
    coco_data = json.load(f)

# === Helper function to extract split ===
def extract_split(image_folder, output_json_path, split_name):
    image_files = {f for f in os.listdir(image_folder) if f.lower().endswith('.png')}

    # Filter images
    split_images = [img for img in coco_data['images'] if img['file_name'] in image_files]
    split_image_ids = {img['id'] for img in split_images}

    # Filter annotations
    split_annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] in split_image_ids]

    # Assemble split JSON
    output = {
        'info': coco_data.get('info', {}),
        'licenses': coco_data.get('licenses', []),
        'images': split_images,
        'annotations': split_annotations,
        'categories': coco_data.get('categories', [])
    }

    # Save
    with open(output_json_path, 'w') as f:
        json.dump(output, f, indent=4)

    print(f" {split_name} JSON saved to: {output_json_path} ({len(split_images)} images, {len(split_annotations)} annotations)")

# === Run for both splits ===
extract_split(train_images_folder, train_json_output, "Training")
extract_split(val_images_folder, val_json_output, "Validation")


# In[ ]:


import os
import json

# === Paths ===
base_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train"

# Define input COCO-style JSONs
splits = {
    "train": os.path.join(base_dir, "annotations", "instances_train.json"),
    "val": os.path.join(base_dir, "annotations", "instances_val.json")
}

# Output label folders
label_base = os.path.join(base_dir, "labels")
os.makedirs(label_base, exist_ok=True)

for split, json_path in splits.items():
    # Create label subfolder
    label_dir = os.path.join(label_base, split)
    os.makedirs(label_dir, exist_ok=True)

    # Load JSON
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Build image_id to file name and size map
    image_info = {
        img["id"]: {
            "file_name": img["file_name"],
            "width": img["width"],
            "height": img["height"]
        } for img in data["images"]
    }

    # Group annotations by image
    annotations_by_image = {}
    for ann in data["annotations"]:
        img_id = ann["image_id"]
        annotations_by_image.setdefault(img_id, []).append(ann)

    # Process each image
    for img_id, anns in annotations_by_image.items():
        info = image_info[img_id]
        img_name = os.path.splitext(info["file_name"])[0]
        label_file = os.path.join(label_dir, f"{img_name}.txt")

        with open(label_file, "w") as f_out:
            for ann in anns:
                category_id = ann["category_id"]
                bbox = ann["bbox"]  # COCO format: [x, y, width, height]

                # Convert to YOLO format
                x_center = (bbox[0] + bbox[2] / 2) / info["width"]
                y_center = (bbox[1] + bbox[3] / 2) / info["height"]
                width = bbox[2] / info["width"]
                height = bbox[3] / info["height"]

                # YOLO format: <class_id> <x_center> <y_center> <width> <height>
                f_out.write(f"{category_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

    print(f"{split} labels saved to: {label_dir}")


# In[ ]:


import os

# === Folders ===
label_dirs = [
    r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train\labels\train",
    r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train\labels\val"
]

# === Replace class IDs with 0 ===
for label_dir in label_dirs:
    for filename in os.listdir(label_dir):
        if filename.endswith(".txt"):
            path = os.path.join(label_dir, filename)
            with open(path, "r") as f:
                lines = f.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    parts[0] = "0"  # overwrite class ID
                    updated_lines.append(" ".join(parts) + "\n")

            with open(path, "w") as f:
                f.writelines(updated_lines)

print(" All class IDs changed to 0.")


# In[5]:


from PIL import Image
import os

image_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train\images\val"
sizes = set()

for file in os.listdir(image_dir):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(image_dir, file)
        with Image.open(path) as img:
            sizes.add(img.size)

print("Unique image sizes:", sizes)


# In[ ]:


from PIL import Image, ImageOps
import os

# === Paths ===
base_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train\images"
train_input_dir = os.path.join(base_dir, "train")
val_input_dir = os.path.join(base_dir, "val")

train_output_dir = os.path.join(base_dir, "train_resized")
val_output_dir = os.path.join(base_dir, "val_resized")

target_size = (640, 640)

# === Resize function with padding ===
def resize_images(input_dir, output_dir, set_name):
    os.makedirs(output_dir, exist_ok=True)
    count = 0

    for file in os.listdir(input_dir):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            try:
                with Image.open(input_path) as img:
                    padded_img = ImageOps.pad(img, target_size, color=(114, 114, 114))
                    padded_img.save(output_path)
                    count += 1
            except Exception as e:
                print(f"  Failed to process {file}: {e}")

    print(f" {set_name} set: {count} images resized to {target_size} and saved to: {output_dir}")

# === Run for both sets ===
resize_images(train_input_dir, train_output_dir, "Training")
resize_images(val_input_dir, val_output_dir, "Validation")


# In[ ]:


from ultralytics import YOLO
import os

# Paths
input_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\springproject\data\input_images"
output_dir = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\springproject\results_0.4"
model_path = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\springproject\weights2\best.pt"

# Load model
model = YOLO(model_path)

# Run