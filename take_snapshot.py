import time
import board
import busio
import adafruit_mlx90640
import numpy as np
import cv2

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
count = 0
while True:
    try:
        mlx.getFrame(getFrame_output)
        if count == 16:
            break
        count += 1
    except ValueError:
        print("val_error")
        continue

print(getFrame_output)
final_frame = np.array(getFrame_output).reshape(24,32) * 255

cv2.imshow("snapshot", final_frame)
print(final_frame.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
