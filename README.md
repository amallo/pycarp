# MicroPython ESP32 - Hello World

Projet de base pour développer avec MicroPython sur ESP32.

## Prérequis

1. **Firmware MicroPython pour ESP32**
   - Téléchargez le firmware depuis [micropython.org/download/esp32/](https://micropython.org/download/esp32/)
   - Flashez-le sur votre ESP32 avec `esptool.py`:
   ```bash
   esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
   esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-*.bin
   ```

2. **Outils nécessaires**
   - `esptool.py`: pour flasher le firmware
   - `ampy` ou `mpremote`: pour transférer les fichiers
   - Un terminal série (minicom, screen, ou l'IDE de votre choix)

## Recommandation : environnement virtuel (venv)

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

```bash
# Créer le venv à la racine du projet
python3 -m venv venv

# Activer le venv
# macOS / Linux :
source venv/bin/activate
# Windows (PowerShell) :
# .\venv\Scripts\Activate.ps1
# Windows (cmd) :
# .\venv\Scripts\activate.bat

# Installer les dépendances
pip install -r requirements.txt
```

Ensuite, utilisez `esptool`, `ampy` ou `mpremote` comme d'habitude. Pensez à activer le venv à chaque nouvelle session (`source venv/bin/activate`).

## Installation des outils (sans venv)

Si vous n'utilisez pas de venv :

```bash
pip install -r requirements.txt
# ou manuellement :
pip install esptool adafruit-ampy mpremote
```

## Transfert des fichiers vers l'ESP32

### Avec ampy:
```bash
ampy --port /dev/ttyUSB0 put main.py
ampy --port /dev/ttyUSB0 put boot.py
```

### Avec mpremote:
```bash
mpremote connect /dev/ttyUSB0 cp main.py :
mpremote connect /dev/ttyUSB0 cp boot.py :
```

## Structure du projet

- `main.py`: Point d'entrée principal, exécuté automatiquement au démarrage
- `boot.py`: Configuration système, exécuté avant main.py
- `native_modules/`: Modules natifs C/C++ et exemples d'optimisation
- `NATIVE_MODULES.md`: Guide complet sur le développement de modules natifs
- `README.md`: Ce fichier

## Utilisation

1. Connectez votre ESP32 via USB
2. Identifiez le port série (souvent `/dev/ttyUSB0` sur Linux, `/dev/tty.usbserial-*` sur macOS, `COM3` sur Windows)
3. Transférez les fichiers vers l'ESP32
4. Redémarrez l'ESP32 ou utilisez un terminal série pour voir la sortie

## Connexion au REPL

Pour accéder au REPL (Read-Eval-Print Loop) interactif:

```bash
# Avec screen
screen /dev/ttyUSB0 115200

# Avec minicom
minicom -D /dev/ttyUSB0 -b 115200

# Avec mpremote
mpremote connect /dev/ttyUSB0
```

Appuyez sur `Ctrl+D` pour redémarrer l'ESP32 depuis le REPL.

## Notes

- Le fichier `main.py` est exécuté automatiquement au démarrage
- La LED intégrée est généralement sur GPIO 2
- Utilisez `Ctrl+C` pour interrompre un programme en cours
- Utilisez `Ctrl+D` pour redémarrer l'ESP32

## Optimisation des performances

Si vous avez besoin de meilleures performances, consultez `NATIVE_MODULES.md` pour :
- Développer des modules natifs en C/C++
- Utiliser les décorateurs `@micropython.viper` et `@micropython.native`
- Intégrer des briques natives dans le firmware

## Ressources

- [Documentation MicroPython](https://docs.micropython.org/)
- [Documentation ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [Guide MicroPython ESP32](https://randomnerdtutorials.com/getting-started-micropython-esp32/)
- [Modules natifs MicroPython](https://docs.micropython.org/en/latest/develop/cmodules.html)
