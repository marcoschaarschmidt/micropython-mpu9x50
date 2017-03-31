# Test program for IRQ based access to MPU9250
# Note there will be small differences between the lines because
# of drift or movement occurring between the readings

from machine import Timer
import time
from mpu9250 import MPU9250
import micropython
micropython.alloc_emergency_exception_buf(100)

def cb(timer):                          # Callback: populate array members
    imu.get_gyro_irq()
    imu.get_accel_irq()
    imu.get_mag_irq()

tim = Timer.Alarm(cb, 400, periodic=True)

imu = MPU9250()

print("You should see slightly different values on each pair of readings.")
print("            Accelerometer                               Gyro                                Magnetometer")

for count in range(50):
    time.sleep_ms(400)                  # Ensure an interrupt occurs to re-populate integer values
    scale = 6.6666                      # Correction factors involve floating point
    mag = list(map(lambda x, y : x*y/scale, imu.mag.ixyz, imu.mag_correction))
    print("Interrupt:", [x/16384 for x in imu.accel.ixyz], [x/131 for x in imu.gyro.ixyz], mag)
    time.sleep_ms(100)
    print("Normal:   ", imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
    print()

tim.cancel()