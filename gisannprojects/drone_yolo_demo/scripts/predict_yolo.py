predictions on all images in input directory
for file in os.listdir(input_dir):
    if file.lower().endswith(('.png')):
        input_path = os.path.join(input_dir, file)
        model.predict(source=input_path, save=True, save_txt=True, conf=0.5, project=output_dir, name='predict_output', imgsz=640)


# In[ ]:


#To spot which yolo version used

import ultralytics
print("Ultralytics YOLO version:", ultralytics.__version__)


# In[ ]:


##to identify version yolov8s as it has ~28.6GLOPS giga floating point operations per sec

model = YOLO(r"C:\Users\annni\Documents\1_Spring_2025\Projectspring\drone\mini_train\custom_output4\run4\weights\best.pt")
print(model.info())