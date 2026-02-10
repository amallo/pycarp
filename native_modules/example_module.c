/**
 * Exemple de module natif MicroPython pour ESP32
 * 
 * Ce module expose des fonctions C optimisées à MicroPython
 * 
 * Pour compiler:
 * 1. Placez ce fichier dans micropython/ports/esp32/modules/
 * 2. Compilez le firmware: make BOARD=GENERIC
 * 3. Flashez le firmware sur l'ESP32
 * 
 * Utilisation dans MicroPython:
 * >>> import example
 * >>> result = example.fast_add(10, 20)
 * >>> print(result)
 * 30
 */

#include "py/obj.h"
#include "py/runtime.h"
#include "py/builtin.h"

// ============================================
// Fonction C native optimisée
// ============================================
static int fast_add(int a, int b) {
    return a + b;
}

static int fast_multiply(int a, int b) {
    return a * b;
}

// ============================================
// Wrappers MicroPython
// ============================================

// Wrapper pour fast_add
STATIC mp_obj_t example_fast_add(mp_obj_t a_obj, mp_obj_t b_obj) {
    int a = mp_obj_get_int(a_obj);
    int b = mp_obj_get_int(b_obj);
    return mp_obj_new_int(fast_add(a, b));
}
STATIC MP_DEFINE_CONST_FUN_OBJ_2(example_fast_add_obj, example_fast_add);

// Wrapper pour fast_multiply
STATIC mp_obj_t example_fast_multiply(mp_obj_t a_obj, mp_obj_t b_obj) {
    int a = mp_obj_get_int(a_obj);
    int b = mp_obj_get_int(b_obj);
    return mp_obj_new_int(fast_multiply(a, b));
}
STATIC MP_DEFINE_CONST_FUN_OBJ_2(example_fast_multiply_obj, example_fast_multiply);

// Fonction qui retourne une liste (exemple plus complexe)
STATIC mp_obj_t example_fibonacci(mp_obj_t n_obj) {
    int n = mp_obj_get_int(n_obj);
    if (n < 0 || n > 100) {
        mp_raise_ValueError(MP_ERROR_TEXT("n must be between 0 and 100"));
    }
    
    mp_obj_t list = mp_obj_new_list(n, NULL);
    mp_obj_list_t *list_obj = MP_OBJ_TO_PTR(list);
    
    if (n > 0) {
        list_obj->items[0] = mp_obj_new_int(0);
    }
    if (n > 1) {
        list_obj->items[1] = mp_obj_new_int(1);
    }
    
    for (int i = 2; i < n; i++) {
        int a = mp_obj_get_int(list_obj->items[i-1]);
        int b = mp_obj_get_int(list_obj->items[i-2]);
        list_obj->items[i] = mp_obj_new_int(a + b);
    }
    
    return list;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_1(example_fibonacci_obj, example_fibonacci);

// ============================================
// Définition du module
// ============================================
STATIC const mp_rom_map_elem_t example_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_example) },
    { MP_ROM_QSTR(MP_QSTR_fast_add), MP_ROM_PTR(&example_fast_add_obj) },
    { MP_ROM_QSTR(MP_QSTR_fast_multiply), MP_ROM_PTR(&example_fast_multiply_obj) },
    { MP_ROM_QSTR(MP_QSTR_fibonacci), MP_ROM_PTR(&example_fibonacci_obj) },
};

STATIC MP_DEFINE_CONST_DICT(example_module_globals, example_module_globals_table);

const mp_obj_module_t example_user_cmodule = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&example_module_globals,
};

// Enregistrement du module
MP_REGISTER_MODULE(MP_QSTR_example, example_user_cmodule);
