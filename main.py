"""
Hello World pour ESP32 avec MicroPython
Ce fichier s'exécute automatiquement au démarrage de l'ESP32
"""

import machine
import time

# Initialisation de la LED intégrée (GPIO 2 sur la plupart des ESP32)
led = machine.Pin(2, machine.Pin.OUT)

print("=" * 40)
print("Hello World depuis ESP32!")
print("MicroPython est en cours d'exécution")
print("=" * 40)

# Faire clignoter la LED 3 fois
for i in range(3):
    led.on()
    print(f"LED ON - clignotement {i+1}/3")
    time.sleep(0.5)
    led.off()
    print(f"LED OFF - clignotement {i+1}/3")
    time.sleep(0.5)

print("\nHello World terminé!")
print("L'ESP32 est prêt à recevoir vos commandes.")
