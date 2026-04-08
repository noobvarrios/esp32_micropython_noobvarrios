from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(4), scl=Pin(5))
print(i2c.scan()) 