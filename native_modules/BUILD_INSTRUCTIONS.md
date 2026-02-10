# Instructions de compilation pour modules natifs

## Prérequis

```bash
# Installer les outils de compilation
sudo apt-get install build-essential libffi-dev pkg-config

# Installer l'ESP-IDF (nécessaire pour compiler MicroPython pour ESP32)
# Suivez: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/
```

## Méthode 1: Module natif dans le firmware

### Étape 1: Cloner MicroPython

```bash
git clone https://github.com/micropython/micropython.git
cd micropython
git submodule update --init
```

### Étape 2: Ajouter votre module

```bash
# Copier votre module natif
cp /path/to/pycarpe/native_modules/example_module.c ports/esp32/modules/

# Ou créer un lien symbolique
ln -s /path/to/pycarpe/native_modules/example_module.c ports/esp32/modules/
```

### Étape 3: Compiler le firmware

```bash
cd ports/esp32

# Pour ESP32 générique
make BOARD=GENERIC

# Pour une carte spécifique (ex: ESP32-DevKitC)
make BOARD=ESP32_DEV
```

### Étape 4: Flasher le firmware

```bash
# Identifier le port série
ls /dev/ttyUSB*  # Linux
ls /dev/tty.usbserial-*  # macOS
ls /dev/tty.*  # macOS alternative

# Eraser et flasher
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 \
    write_flash -z 0x1000 build-ESP32_GENERIC/firmware.bin
```

### Étape 5: Tester

```bash
# Se connecter au REPL
mpremote connect /dev/ttyUSB0

# Dans le REPL:
>>> import example
>>> example.fast_add(10, 20)
30
>>> example.fibonacci(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Méthode 2: Utiliser les décorateurs d'optimisation

Cette méthode ne nécessite PAS de recompiler le firmware.

### Transférer le fichier optimisé

```bash
mpremote connect /dev/ttyUSB0 cp native_modules/optimized_example.py :
```

### Utiliser dans votre code

```python
from optimized_example import fast_sum_viper, fast_loop_native

result = fast_sum_viper(1000)
print(result)
```

## Structure recommandée pour développement

```
pycarpe/
├── micropython/              # Clone du repo MicroPython (optionnel)
│   └── ports/esp32/
│       └── modules/
│           └── example_module.c
├── native_modules/           # Vos modules natifs
│   ├── example_module.c
│   ├── optimized_example.py
│   └── BUILD_INSTRUCTIONS.md
└── main.py
```

## Débogage

### Activer les messages de débogage

Dans `ports/esp32/mpconfigport.h`, ajoutez:
```c
#define MICROPY_DEBUG_PRINTER (&mp_stderr_print)
```

### Utiliser GDB (avancé)

```bash
# Compiler avec support GDB
make BOARD=GENERIC DEBUG=1

# Lancer GDB
xtensa-esp32-elf-gdb build-ESP32_GENERIC/firmware.elf
```

## Conseils de performance

1. **Mesurez d'abord** : Utilisez `time.ticks_ms()` pour mesurer les performances
2. **Commencez simple** : Essayez `@micropython.viper` avant de créer un module C
3. **Profiling** : Identifiez les goulots d'étranglement avant d'optimiser
4. **Documentation** : Consultez [docs.micropython.org](https://docs.micropython.org) pour les meilleures pratiques

## Ressources

- [MicroPython C Modules Documentation](https://docs.micropython.org/en/latest/develop/cmodules.html)
- [ESP-IDF Getting Started](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/)
- [MicroPython ESP32 Port](https://github.com/micropython/micropython/tree/master/ports/esp32)
