from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
print(i2c.scan()) 