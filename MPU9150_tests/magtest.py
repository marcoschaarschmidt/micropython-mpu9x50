'''
Demo of MPU9150 nonblocking reads and the reading and use of correction factors.
Shows that call to get_mag() returns fast.
'''

from mpu9150 import MPU9150
import time
import utime

def testfunc(a):
    start = utime.ticks_us()
    while not a.mag_ready:
        pass
    dt = utime.ticks_diff(start,utime.ticks_us())
    print("Wait time = {:5.2f}mS".format(dt/1000))
    start = utime.ticks_us()
    xyz = a.mag.xyz
    dt = utime.ticks_diff(start,utime.ticks_us())
    print("Time to get = {:5.2f}mS".format(dt/1000))
    print("x = {:5.3f} y = {:5.3f} z = {:5.3f}".format(xyz[0], xyz[1], xyz[2]))
    print("Mag status should be not ready (False): ", a.mag_ready)
    print("Correction factors: x = {:5.3f} y = {:5.3f} z = {:5.3f}".format(
        a.mag_correction[0],
        a.mag_correction[1],
        a.mag_correction[2]))

def test():
    mpu9150 = MPU9150()
    testfunc(mpu9150)
    print()
    utime.sleep_ms(250)
    print("Repeating")
    testfunc(mpu9150)

test()

