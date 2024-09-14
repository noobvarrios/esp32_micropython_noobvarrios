from machine import I2C, Pin
from ds1302 import DS1302
import time

ds = DS1302(Pin(18),Pin(22),Pin(21))

# ds.date_time([2024, 9, 12, 4, 19, 5, 30, 0]) # set datetime.


while True: 
    print(ds.date_time()) # returns the current datetime.
    time.sleep(1)



