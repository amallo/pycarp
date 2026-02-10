# Développement de Modules Natifs pour MicroPython ESP32

## Introduction

Oui, vous pouvez développer des modules natifs en C/C++ pour améliorer les performances avec MicroPython. C'est particulièrement utile pour :
- Opérations critiques en temps réel
- Manipulation de GPIO à haute fréquence
- Traitement de signaux (ADC, PWM, etc.)
- Algorithmes mathématiques intensifs
- Communication série rapide

## Options pour améliorer les performances

### 1. Modules Natifs (C/C++) - Performance maximale

Les modules natifs sont compilés dans le firmware MicroPython et offrent les meilleures performances.

**Avantages :**
- Performance maximale (proche du C pur)
- Accès direct au matériel
- Pas de surcharge d'interprétation Python

**Inconvénients :**
- Nécessite de recompiler le firmware MicroPython
- Plus complexe à développer et déboguer
- Moins flexible (modifications nécessitent recompilation)

### 2. Décorateurs @micropython.viper et @micropython.native

MicroPython offre des décorateurs pour optimiser le code Python :

- `@micropython.viper` : Compile en bytecode optimisé (meilleure performance)
- `@micropython.native` : Compile en code machine natif (performance maximale en Python)

**Avantages :**
- Pas besoin de recompiler le firmware
- Facile à utiliser
- Bon compromis performance/facilité

**Limitations :**
- Moins performant que les modules C purs
- Restrictions sur les types de données

### 3. Modules Frozen (Python compilé)

Compilez vos modules Python en bytecode et intégrez-les dans le firmware.

**Avantages :**
- Pas besoin de transférer les fichiers
- Démarrage plus rapide
- Code protégé

## Structure pour développer un module natif

```
pycarpe/
├── micropython/              # Clone du repo MicroPython
│   └── ports/esp32/
│       └── modules/
│           └── mymodule.c    # Votre module natif
├── native_modules/           # Vos modules natifs
│   ├── example_module.c
│   └── example_module.h
└── build_instructions.md
```

## Exemple de module natif simple

Voici un exemple de module natif qui expose une fonction C à MicroPython :

```c
// example_module.c
#include "py/obj.h"
#include "py/runtime.h"

// Fonction C native
static int fast_add(int a, int b) {
    return a + b;
}

// Wrapper MicroPython
STATIC mp_obj_t example_fast_add(mp_obj_t a_obj, mp_obj_t b_obj) {
    int a = mp_obj_get_int(a_obj);
    int b = mp_obj_get_int(b_obj);
    return mp_obj_new_int(fast_add(a, b));
}

// Définition de la fonction pour MicroPython
STATIC MP_DEFINE_CONST_FUN_OBJ_2(example_fast_add_obj, example_fast_add);

// Définition du module
STATIC const mp_rom_map_elem_t example_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_example) },
    { MP_ROM_QSTR(MP_QSTR_fast_add), MP_ROM_PTR(&example_fast_add_obj) },
};

STATIC MP_DEFINE_CONST_DICT(example_module_globals, example_module_globals_table);

const mp_obj_module_t example_user_cmodule = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&example_module_globals,
};

MP_REGISTER_MODULE(MP_QSTR_example, example_user_cmodule);
```

## Processus de compilation

1. **Cloner MicroPython :**
```bash
git clone https://github.com/micropython/micropython.git
cd micropython
```

2. **Ajouter votre module :**
   - Placez votre `.c` dans `ports/esp32/modules/`
   - Ou ajoutez-le dans `ports/esp32/boards/` pour une carte spécifique

3. **Compiler le firmware :**
```bash
cd ports/esp32
make submodules
make BOARD=GENERIC
# ou pour une carte spécifique:
make BOARD=ESP32_DEV
```

4. **Flasher le firmware :**
```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 \
    write_flash -z 0x1000 build-ESP32_GENERIC/firmware.bin
```

## Utilisation des décorateurs d'optimisation

Exemple d'utilisation dans votre code Python :

```python
import micropython

# Optimisation viper (bon compromis)
@micropython.viper
def fast_loop(count: int) -> int:
    total = 0
    for i in range(count):
        total += i
    return total

# Optimisation native (performance maximale)
@micropython.native
def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result
```

## Quand utiliser quoi ?

| Solution | Performance | Complexité | Flexibilité |
|----------|-------------|------------|-------------|
| Python pur | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| @viper/@native | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Modules natifs C | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |

**Recommandations :**
- Commencez par Python pur
- Utilisez `@viper` ou `@native` si besoin
- Passez aux modules natifs seulement si critique

## Ressources

- [Documentation MicroPython C Modules](https://docs.micropython.org/en/latest/develop/cmodules.html)
- [MicroPython GitHub - Exemples de modules](https://github.com/micropython/micropython/tree/master/examples/usercmodule)
- [Guide de compilation ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#building-the-firmware)
- [Décorateurs viper/native](https://docs.micropython.org/en/latest/reference/speed_python.html)

## Exemple pratique : Module GPIO rapide

Pour des opérations GPIO très rapides (ex: protocoles série personnalisés), un module natif est souvent nécessaire car MicroPython a une latence trop élevée pour certaines applications temps réel.
