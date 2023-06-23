import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import cv2
import math
import detectV1 as detect
from scipy import stats

#TEMPERATURE THRESHOLDS IN CELSIUS
thresh1 = 35
thresh2 = 40
thresh3 = 50

# maybe at some point i'll stop using this constant, but for now, this works for 0.9 to 1 m
pixel_size = 0.03848 * 0.03848

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# if using higher refresh rates yields a 'too many retries' exception,
# try decreasing this value to work with certain pi/camera combinations
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ

getFrame_output = [0] * 768
while True:
    try:
        # get frame data in Celsius
        mlx.getFrame(getFrame_output)

        # find clusters
        clusters = detect.detect(getFrame_output)

        # loop through detected objects and do what you gotta do
        for x in range(len(clusters)):
            print("Object ", x)
            print("Threshold: {thresh}".format(thresh=clusters[x][1]))
            print("Size: {size}".format(size=clusters[x][0]))
            print()

    except KeyboardInterrupt:
        print("err")
        break
