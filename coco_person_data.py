import os
import requests
import zipfile
from pycocotools.coco import COCO

# Function to download COCO annotations for a specific category
def download_coco_annotations(annotations_url, save_dir, category_name):
    os.makedirs(save_dir, exist_ok=True)
    annotations_file = os.path.join(save_dir, f"annotations_{person}  trainval2017.zip")
    
    # Download annotations zip file
    print(f"Downloading COCO annotations for {person}...")
    response = requests.get(annotations_url)
    with open(annotations_file, "wb") as f:
        f.write(response.content)
    print("COCO annotations for {person} downloaded successfully!")

    # Unzip the annotations file
    with zipfile.ZipFile(annotations_file, 'r') as zip_ref:
        zip_ref.extractall(save_dir)
    print("COCO annotations for {person} unzipped successfully!")

# Function to download COCO images for a specific category
def download_coco_images(images_url, save_dir, category_name, num_images_to_download):
    person = category_name
    smallset =  num_images_to_download
    os.makedirs(save_dir, exist_ok=True)
    images_file = os.path.join(save_dir, "images_{person}_trainval2017.zip")
    
    # Download images zip file
    print("Downloading COCO images for (person}...")
    response = requests.get(images_url)
    with open(images_file, "wb") as f:
        f.write(response.content)
    print("COCO images for {person} downloaded successfully!")

    # Unzip the images file
    with zipfile.ZipFile(images_file, 'r') as zip_ref:
        zip_ref.extractall(save_dir)
    print("COCO images for {person} unzipped successfully!")

    # Limit the number of images to be downloaded (64115 maximum in COCO 2017) e.g:
    smallset = 10000

# COCO annotations and images URLs
coco_annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
coco_images_url = "http://images.cocodataset.org/zips/train2017.zip"

# Directories to save annotations and images
save_annotations_directory = "./coco_annotations"
save_images_directory = "./coco_images"

# Download COCO annotations and images for the 'person' class
download_coco_annotations(coco_annotations_url, save_annotations_directory, "person")
download_coco_images(coco_images_url, save_images_directory, "num_images_to_download", "person")

# Initialize COCO object with the downloaded annotations file
annotations_file_path = os.path.join(save_annotations_directory, "annotations/instances_person_train2017.json")
coco = COCO(annotations_file_path)

# Get the category ID corresponding to the 'person' class
person_category_id = coco.getCatIds(catNms=['person'])[0]

# Get image IDs containing instances of the 'person' class
person_image_ids = coco.getImgIds(catIds=[person_category_id])

# Get annotations for images containing 'person' instances
person_annotations = coco.loadAnns(coco.getAnnIds(imgIds=person_image_ids, catIds=[person_category_id]))

# Example: Print annotations for the first image
print("Annotations for the first image:")
print(person_annotations[0])

