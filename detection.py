import os
import sys
import json
import datetime
import numpy as np
import skimage.draw
import cv2
from mrcnn.visualize import display_instances
import matplotlib.pyplot as plt

ROOT_DIR = os.path.abspath("../../")

sys.path.append(ROOT_DIR)
from mrcnn.config import Config
from mrcnn import model as modellib, utils

COCO_WEIGHTS_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

class CustomConfig(Config):
    NAME = "building"

    IMAGES_PER_GPU = 1

    NUM_CLASSES = 1 + 1

    STEPS_PER_EPOCH = 100

    DETECTION_MIN_CONFIDENCE = 0.7
    
def color_splash(image, mask):
    black = image
    black.fill(0)
    mask = (np.sum(mask, -1, keepdims=True) >= 1)
    if mask.shape[0] > 0:
        splash = np.where(mask, 255, 0).astype(np.uint8)
    else:
        splash = black
    return splash


def detect_and_color_splash(model, image_path, output_dir):
    print("Running on {}".format(image_path))
    image = skimage.io.imread(image_path)
    r = model.detect([image], verbose=1)[0]
    splash = color_splash(image, r['masks'])
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    file_name = "splash_{}.png".format(os.path.basename(image_path), datetime.datetime.now())
    skimage.io.imsave(os.path.join(output_dir, file_name), splash)
    print("Saved to ", file_name)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Train Mask R-CNN to detect custom class.')
    parser.add_argument('--weights', required=True,
                        metavar="/path/to/weights.h5",
                        help="Path to weights .h5 file or 'coco'")
    parser.add_argument('--logs', required=False,
                        default=DEFAULT_LOGS_DIR,
                        metavar="/path/to/logs/",
                        help='Logs and checkpoints directory (default=logs/)')
    parser.add_argument('--image', required=False,
                        metavar="path or URL to image",
                        help='Image to apply the color splash effect on')
    parser.add_argument('--output', required=False,
                        metavar="path for output image",
                        help='Image to apply the color splash effect on')
    args = parser.parse_args()


    print("Weights: ", args.weights)

    class InferenceConfig(CustomConfig):
        GPU_COUNT = 1
        IMAGES_PER_GPU = 1
    config = InferenceConfig()
    config.display()

    model = modellib.MaskRCNN(mode="inference", config=config,
                                  model_dir=args.logs)
    weights_path = args.weights

    print("Loading weights ", weights_path)
    model.load_weights(weights_path, by_name=True)
    directory = args.image
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg"):
                detect_and_color_splash(model, image_path=os.path.join(directory, file), output_dir=args.output)
