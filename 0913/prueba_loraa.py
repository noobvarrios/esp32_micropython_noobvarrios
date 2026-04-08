from machine import Pin, SPI

spi = SPI(0, baudrate=5000000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

def read_reg(addr):
    cs.value(0)
    spi.write(bytearray([addr & 0x7F]))  # MSB=0 → lectura
    data = spi.read(1)
    cs.value(1)
    return data[0]

print("Version:", hex(read_reg(0x42)))
