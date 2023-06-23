import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import cv2
import math
import detect
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


# returns the (approximate) size of the target in meters squared
def findSize(pixels):
    return pixels * pixel_size


getFrame_output = [0] * 768
while True:
    try:
        # get frame data in Celsius
        mlx.getFrame(getFrame_output)

        # find contours and detect the pixels inside of them
        temps = detect.detect(getFrame_output)

        # loop through detected objects and do what you gotta do
        for x in range(len(temps)):
            print("Object ", x)
            print("Mean: {mean}, Median: {median}, Mode: {mode}".format(mean=np.mean(temps[x]), median=np.median(temps[x]), mode=stats.mode(temps[x])))
            print("Size: {size}".format(size=findSize(len(temps[x]))))
            print()

    except KeyboardInterrupt:
        print("err")
        break
