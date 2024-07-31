import os
import random
import shutil

# Set paths
voc_dir = './Pascal_dataset_test/VOC2012'
annotations_dir = os.path.join(voc_dir, 'Annotations')
images_dir = os.path.join(voc_dir, 'JPEGImages')
trainval_file = os.path.join(voc_dir, 'ImageSets', 'Main', 'trainval.txt')

# Output directories
train_annotations_dir = os.path.join(voc_dir, 'train', 'Annotations')
train_images_dir = os.path.join(voc_dir, 'train', 'JPEGImages')
val_annotations_dir = os.path.join(voc_dir, 'valid', 'Annotations')
val_images_dir = os.path.join(voc_dir, 'valid', 'JPEGImages')

# Create directories if they don't exist
os.makedirs(train_annotations_dir, exist_ok=True)
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_annotations_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)

# Read trainval file
with open(trainval_file, 'r') as f:
    file_names = f.read().strip().split()

# Shuffle and split
random.shuffle(file_names)
split_index = int(0.8 * len(file_names))  # 80% for training, 20% for validation
train_files = file_names[:split_index]
val_files = file_names[split_index:]

def copy_files(file_list, dest_annotations_dir, dest_images_dir):
    for file_name in file_list:
        annotation_file = os.path.join(annotations_dir, f"{file_name}.xml")
        image_file = os.path.join(images_dir, f"{file_name}.jpg")

        if os.path.exists(annotation_file) and os.path.exists(image_file):
            shutil.copy(annotation_file, dest_annotations_dir)
            shutil.copy(image_file, dest_images_dir)
            print(f"Copied {annotation_file} and {image_file}")
        else:
            print(f"Missing files for {file_name}: {annotation_file}, {image_file}")

# Copy files to train and valid directories
print("Copying training files...")
copy_files(train_files, train_annotations_dir, train_images_dir)
print("Copying validation files...")
copy_files(val_files, val_annotations_dir, val_images_dir)

print("Dataset split and copied successfully.")
