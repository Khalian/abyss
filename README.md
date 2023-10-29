# abyss
Binary image classifier for buildings/roads with cracks or not. 

Trained on https://data.mendeley.com/datasets/5y9wdsg2zt/2

Simple CNN classifier based on this tutorial https://www.youtube.com/watch?v=jztwpsIzEGc

The project contains

1. train.py -> Run to train against the Crack dataset (which is also checked in this repo)
2. is_crack.py -> Accepts an image of a building/road and verifies if there is a crack in that image.

# Pre requisites

1. Install python 3 https://www.python.org/downloads/
2. Install [pip](https://pip.pypa.io/en/stable/installation/)https://pip.pypa.io/en/stable/installation/
3. Run in command line

```
pip install tensorflow tensorflow-gpu opencv-python matplotlib argparse
```
# Retraining

While I have already pre trained a model and checked it into the models directory, you can run train.py again to create a new model (in case you want to add or subtract training data pictures). Note this is a very slow operation without significant GPU power (it took me 40 mins to train this entire data set on an Apple M1 Pro 10 core 32 gig ram machine : https://support.apple.com/kb/SP858?locale=en_US)

# Using the classifier

Run the is_crack.py like this

```
python3 is_crack.py --image_path="./Crack/Positive/00010.jpg"
1/1 [==============================] - 0s 40ms/step
The picture has a crack in it

python3 is_crack.py --image_path="./Crack/Negative/00010.jpg"
1/1 [==============================] - 0s 40ms/step
The picture has no crack in it
```

The input --image_path is the fully qualified file path where your input image should reside. The output has two lines, one for the time taken for classification and the other output on whether there is a crack or not. 

### This is the same kind of classifier as in https://www.youtube.com/watch?v=vIci3C4JkL0, but less cool and/or funny. 

