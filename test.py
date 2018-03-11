from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy("COM3")
neuropy.start()

while True:
    if neuropy.meditation > 70: # Access data through object
        neuropy.stop()
    sleep(0.2) # Don't eat the CPU cycles
