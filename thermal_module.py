import time
import board
import busio
import adafruit_mlx90640
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# if using higher refresh rates yields a 'too many retries' exception,
# try decreasing this value to work with certain pi/camera combinations
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

getFrame_output = [0] * 768
final_frame = np.zeros((24, 32), dtype=float)
while True:
    try:
        mlx.getFrame(getFrame_output)
    except ValueError:
        print("val_error")
        continue

    for h in range(24):
        for w in range(32):
            pixel = getFrame_output[h*32 + w]
            final_frame[h][w] = pixel
        print()
    print()
