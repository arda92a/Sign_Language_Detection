import random
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def visualize_random_image(img_dir: Path,
                           seed: int = None):
    random.seed(seed)
    image_path_list = list(img_dir.glob("*/*/*.jpg"))
    random_image_path = random.choice(image_path_list)

    img = Image.open(random_image_path)
    image_class = random_image_path.parent.stem

    img_as_array = np.asarray(img)

    plt.figure(figsize=(10,7))
    plt.imshow(img_as_array)
    plt.title(f"Image class: {image_class} | Image shape: {img_as_array.shape} -> [Height, Width, Color Channel]")
    plt.axis(False);

def plot_transformed_images(image_path,
                            transform,
                            n=3,
                            seed=42):
    """ 
    Selects random images from a path of images and loads/transforms them then plots the original vs the transformed version.
    """

    random.seed(seed)

    image_path_list = list(image_path.glob("*/*/*.jpg")) 

    random_image_paths = random.sample(image_path_list,k=n)

    for image_path in random_image_paths:

        with Image.open(image_path) as f:
            fig,ax = plt.subplots(nrows=1,
                                  ncols=2)
            ax[0].imshow(f)
            ax[0].set_title(f"Original\nSize : {f.size}")
            ax[0].axis(False)


            transformed_image = transform(f).permute(1,2,0) 
            ax[1].imshow(transformed_image)
            ax[1].set_title(f"Transformed\nSize: {transformed_image.shape}")
            ax[1].axis(False)   

            fig.suptitle(f"Class: {image_path.parent.stem}", fontsize=16)
        

