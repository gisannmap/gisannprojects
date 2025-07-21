import os
import shutil

# Define paths
label_folder = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\unzipped\labelTxt_all"
image_folder = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\unzipped\images_all"
output_img_folder = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\xtract_40\images_tune"
output_label_folder = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\xtract_40"

# Ensure output folders exist
os.makedirs(output_img_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# Parameters
target_class = "plane"
max_images = 40

# Check how many have already been copied
existing_images = [
    f for f in os.listdir(output_img_folder) if f.lower().endswith(".png")
]
copied_count = len(existing_images)###################

if copied_count >= max_images:
    print(f"{copied_count} images already exist in output. Skipping copy.")
    #exit()
else:
    # Loop through label files (your existing copying loop here)
    for label_file in os.listdir(label_folder):
        if not label_file.endswith(".txt"):               #to create a text file of the image names alone
            continue

        label_path = os.path.join(label_folder, label_file)

        with open(label_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if target_class in line.lower():
                    image_name = label_file.replace(".txt", ".png")
                    src_img = os.path.join(image_folder, image_name)
                    dest_img = os.path.join(output_img_folder, image_name)

                    if os.path.exists(src_img) and not os.path.exists(dest_img):
                        shutil.copy2(src_img, dest_img)
                        print(f"Copied image: {image_name}")

                        dest_txt = os.path.join(output_label_folder, label_file)
                        shutil.copy2(label_path, dest_txt)
                        print(f"Copied label : {label_file}")

                        copied_count += 1
                    break

        if copied_count >= max_images:
            break
        # Path to save the text file
text_output_path = r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\xtract_40\images.txt"

# Get only image names (without extension)
image_names = [os.path.splitext(f)[0] for f in os.listdir(output_img_folder) if f.lower().endswith(".png")]

# Save to text file
with open(text_output_path, "w") as f:
    for name in sorted(image_names):
        f.write(name + "\n")

#print(f"\nSaved {len(image_names)} image names to:\n{text_output_path}")
