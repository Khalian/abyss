from tensorflow.keras.models import load_model
import argparse
import cv2
import numpy as np
import os
import tensorflow as tf

parser = argparse.ArgumentParser(description="A simple program with string arguments")

# Add a string argument
parser.add_argument('--image_path', type=str, help='Path of image to check')

args = parser.parse_args()

if args.image_path:
    img = cv2.imread(args.image_path)
    resize = tf.image.resize(img, (256,256))
    model = load_model(os.path.join('models','imageclassifier.h5'))
    yhat = model.predict(np.expand_dims(resize/255, 0))
    if yhat >= 0.5:
        print("The picture has a crack in it")
    else:
        print("The picture has no crack in it")
else:
    print("image_path is required argument")
