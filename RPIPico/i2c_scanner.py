from machine import Pin, I2C

# I2C0 con GP4 = SDA, GP5 = SCL
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

print('I2C SCANNER')
devices = i2c.scan()

if not devices:
    print("No I2C device found")
else:
    print("I2C devices found:", [hex(dev) for dev in devices])
