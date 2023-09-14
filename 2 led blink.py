import time
from machine import Pin

led1_pin = 2
led2_pin = 4

led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

def toggle_leds():
    led1.value(not led1.value())
    led2.value(not led2.value())
    
while True:
    toggle_leds()
    time.sleep(0.1)
    