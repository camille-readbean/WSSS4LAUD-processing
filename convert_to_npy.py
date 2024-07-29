import pathlib
from typing import Tuple
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image

from config import train_data_dir, val_img_data_dir, test_img_data_dir, processed_dir_path, logger


def resize_image(image: Image, target_size=512, resample=Image.Resampling.BICUBIC):
    # Resize image to fit within target_size x target_size without changing aspect ratio
    w, h = image.size
    # no change if too small
    if max(h, w) <= target_size:
        return image
    scale = target_size / max(h, w)
    new_size = (int(w * scale), int(h * scale))
    logger.debug(f'{image.filename} have been resized (scaled down) from {image.size} to {new_size}')
    resized_image: Image = image.resize(new_size, resample=resample)

    return resized_image


def get_labels_from_mask(image: Image) -> Tuple[bool, bool, bool]:
    # Tumor epithelial tissue : (0, 64, 128), (label: 0)
    # Tumor-associated stroma tissue: (64, 128, 0), (label: 1)
    # Normal tissue:  (243, 152, 0), (label: 2)
    
    # Define the color mappings
    color_to_label = {
        (0, 64, 128): 0,   # Tumor epithelial tissue
        (64, 128, 0): 1,   # Tumor-associated stroma tissue
        (243, 152, 0): 2   # Normal tissue
    }
    
    # Initialize counters for each label
    label_flags = [False, False, False]

    if image.mode == 'P':
        image = image.convert('RGB')
    
    # Get the pixel data from the image
    pixels = image.load()
    
    # Iterate over each pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            color = pixels[x, y]
            if color in color_to_label:
                label = color_to_label[color]
                label_flags[label] = True
    
    if not any(label_flags):
        logger.warn(f"{image.filename} has no labels ")

    return tuple(label_flags)


def get_labels_from_filename(filename: Path) -> Tuple[bool, bool, bool]:
    """
    Used for getting labels from the train set which are in the following format
    'patient_ID'+'x_axis'+'y_axis'+'3-digit labels'.png
    1003370-11223-11698-[1, 1, 0].png
    Multi-class labels: [Tumor, Stroma, Normal]
    
    Args:
        filename (Path): The filename of the image.

    Returns:
        tuple[bool, bool, bool]: A tuple containing the multi-class labels.
    """

    # Get the filename without the extension
    filename_without_extension = filename.stem

    # Split the filename by '-' and get the last part which contains the labels
    labels_str = filename_without_extension.split('-')[-1]

    # Remove the square brackets from the labels string
    labels_str = labels_str.strip('[]')

    # Split the labels string by ',' and convert each label to an integer
    labels = tuple(bool(int(label.strip())) for label in labels_str.split(','))

    # Check if the length of the labels tuple is 3
    if len(labels) != 3:
        raise ValueError("Invalid number of labels. Expected 3 labels.")

    if not any(labels):
        logger.warn(f"{filename} has no labels")

    return labels



def save_npy(file_path: Path, split: str):
    """
    Open file at file_path, save to npz and return numpy file path and annotation
    Labels retrivel handled here
    file saves to processed_dir_path / split / original_name.npy
    e.g. WSSSLAUD-processed/val/00.png
    returns file path relative to processed_dir_path along with the annotation for this entry
    """
    og_img = Image.open(file_path)
    original_size = og_img.size

    if split == 'train':
        labels = get_labels_from_filename(file_path)
    else: # val and test
        # get file file
        filename = file_path.stem
        # go to base of that folder and get the image under the mask folder
        mask_image = Image.open(file_path.parent.parent / 'mask' / (filename + '.png'))
        labels = get_labels_from_mask(mask_image)

    img = resize_image(og_img)
    new_size = img.size
    npy_filename = Path(split) / f"{file_path.stem}.npy"
    npy_filepath = processed_dir_path / npy_filename # .stem name without suffix

    # Ensure the directory exists
    npy_filepath.parent.mkdir(parents=True, exist_ok=True)
    # the part that convert to numpy
    np.save(npy_filepath, np.array(img))

    label_names = ["tumor", "stroma", "normal"]
    formatted_labels = [f"{name}:{label}" for name, label in zip(label_names, labels)]
    label_str = "|".join(formatted_labels)

    annotation = {
        'npy_filepath': npy_filename, # relative to processed_dir_path
        'label': label_str,
        'original_size' : original_size,
        'new_size' : new_size,
        'original_file_path': file_path,
        'split': split,
    }
    
    return npy_filename, annotation



def main():

    resolutions = set()

    # headers = [npy_filepath,label,original_size,new_size,original_file_path,split]
    annotations = []

    # process training
    for file_path in train_data_dir.glob('*.png'):
        _, annotation = save_npy(file_path=file_path, split='train')
        annotations.append(annotation)
        resolutions.add(annotation['original_size'])
    logger.info("training done")

    # process val
    for file_path in val_img_data_dir.glob('*.png'):
        _, annotation = save_npy(file_path=file_path, split='val')
        annotations.append(annotation)
        resolutions.add(annotation['original_size'])
    logger.info("validation done")

    # process test
    for file_path in test_img_data_dir.glob('*.png'):
        _, annotation = save_npy(file_path=file_path, split='test')    
        annotations.append(annotation)
        resolutions.add(annotation['original_size'])
    logger.info("testing done")

    
    # Calculate the min and max width and height
    min_width = min(res[0] for res in resolutions)
    max_width = max(res[0] for res in resolutions)
    min_height = min(res[1] for res in resolutions)
    max_height = max(res[1] for res in resolutions)

    logger.info(f"{len(resolutions)}")
    # logger.info(f"{len(resolutions)} resolutions: {resolutions}")
    logger.info(f"max: {max(resolutions)} min: {min(resolutions)}")
    logger.info(f"min W: {min_width}, max W: {max_width}")
    logger.info(f"min H: {min_height}, max H: {max_height}")


    df = pd.DataFrame(annotations)
    logger.info(df.columns)
    logger.info(df.iloc[0])
    logger.info(df.iloc[-1])
    # Create CSV
    # csv_path = processed_dir_path / "annotations.csv"
    csv_path =  "annotations.csv"
    df.to_csv(csv_path, index=False)
    # with open(csv_path, mode='w', newline='') as csvfile:
        # writer = csv.writer(csvfile)
        # writer.writerow(headers)
        # writer.writerows(annotations)
        

if __name__ == "__main__":
    main()