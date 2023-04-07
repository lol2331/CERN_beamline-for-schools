import smbus
import time
from openpyxl import load_workbook
import datetime
import math
from datetime import date
import os
import sys

import dateutil.utils

# MPU-6050 register addresses
PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

# Define constants for unit conversion
ACCEL_SCALE = 16384.0  # LSB/g
GYRO_SCALE = 131.0  # LSB/(deg/s)

# Initialize I2C bus and MPU-6050
bus = smbus.SMBus(1)
bus.write_byte_data(0x68, PWR_MGMT_1, 0)
bus.write_byte_data(0x68, PWR_MGMT_2, 0)
bus.write_byte_data(0x68, CONFIG, 0x03)
bus.write_byte_data(0x68, GYRO_CONFIG, 0x10)
bus.write_byte_data(0x68, ACCEL_CONFIG, 0x10)

wb = load_workbook('C:\\Users\\Andrei\\OneDrive\\Documente\\imu\\imu.xlsx')
sheet1 = wb["Sheet1"]
sheet2 = wb["Sheet2"]


# Function to read 16-bit word from I2C device
def read_word_2c(addr):
    high = bus.read_byte_data(0x68, addr)
    low = bus.read_byte_data(0x68, addr + 1)
    val = (high << 8) + low

    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


# Function to convert raw accelerometer values to units of g
def convert_accel(raw):
    return raw / ACCEL_SCALE


# Function to convert raw gyroscope values to units of degrees per second
def convert_gyro(raw):
    return raw / GYRO_SCALE


try:
    # Read and print accelerometer and gyroscope data
    while True:
        accel_x = convert_accel(read_word_2c(ACCEL_XOUT_H))
        accel_y = convert_accel(read_word_2c(ACCEL_YOUT_H))
        accel_z = convert_accel(read_word_2c(ACCEL_ZOUT_H))
        gyro_x = convert_gyro(read_word_2c(GYRO_XOUT_H))
        gyro_y = convert_gyro(read_word_2c(GYRO_YOUT_H))
        gyro_z = convert_gyro(read_word_2c(GYRO_ZOUT_H))

        now = datetime.datetime.now().time()

        print(now)
        print("accelerometer (x,y,z): ({:.2f}g,{:.2f}g,{:.2f}g)".format(accel_x, accel_y, accel_z))
        print("gyroscope (x,y,z): ({:.2f}deg/s,{:.2f}deg/s,{:.2f}deg/s)".format(gyro_x, gyro_y, gyro_z))

        row1 = (now, accel_x, accel_y, accel_z)
        row2 = (now, gyro_x, gyro_y, gyro_z)
        sheet1.append(row1)
        sheet1.append(row2)
        sheet2.append(sys.getsizeof(row1))
        sheet2.append(sys.getsizeof(row2))

        wb.save('C:\\Users\\Andrei\\OneDrive\\Documente\\imu\\imu.xlsx')
        time.sleep(5)


finally:
    wb.save('C:\\Users\\Andrei\\OneDrive\\Documente\\imu\\imu.xlsx')
    print("Goodbye:)")
