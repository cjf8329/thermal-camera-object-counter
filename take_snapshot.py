import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import cv2
import math

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# if using higher refresh rates yields a 'too many retries' exception,
# try decreasing this value to work with certain pi/camera combinations
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ

scalar = 20  
w = scalar * 32
h = scalar * 24
getFrame_output = [0] * 768
final_frame = np.zeros([h, w, 3])
while True:
    try:
        mlx.getFrame(getFrame_output)
        #scaling factor
        s = 10

        img = np.array(getFrame_output)
        img.shape = (24, 32)

        maxVal = math.floor(np.amax(img))
        minVal = math.ceil(np.amin(img))

        norm_img = img - minVal
        norm_img = img * 255/(maxVal - minVal)
        norm_imgGray = norm_img.astype(np.uint8)
        norm_img = cv2.applyColorMap(norm_imgGray, cv2.COLORMAP_JET)


        print("done.", end="")
        print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))

        final = cv2.resize(img, (img.shape[1] * s, img.shape[0] * s))

        cv2.imshow("final", final)
        cv2.waitKey(50)
    except KeyboardInterrupt:
        print("err")
        break

print(getFrame_output)

cv2.destroyAllWindows()
