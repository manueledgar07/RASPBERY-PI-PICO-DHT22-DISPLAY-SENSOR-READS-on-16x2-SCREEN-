from lcd_pico import *
from machine import Pin
from DHT22 import DHT22
from time import sleep

setupLCD()
dht_sensor=DHT22(Pin(15))

displayString(1,0,"Iniciando")
displayString(2,0,"Servicio...")
longDelay(3000)
clear_screen()
while True:
    T, H = dht_sensor.read()
    if T is None:
        displayString(1,0,"Error en el sensor!")
    else:
        displayString(1,0,"Temp. {} C".format(T))
        displayString(2,0,"Humedad {} %".format(H))
    sleep(0.5)