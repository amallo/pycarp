"""
Exemple d'utilisation des décorateurs d'optimisation MicroPython
@micropython.viper et @micropython.native

Ces décorateurs permettent d'optimiser le code Python sans avoir besoin
de recompiler le firmware MicroPython.
"""

import micropython

# ============================================
# Optimisation avec @micropython.viper
# ============================================
# Viper compile en bytecode optimisé
# Restrictions: types limités, pas de listes dynamiques dans certaines boucles

@micropython.viper
def fast_sum_viper(count: int) -> int:
    """Somme rapide avec viper"""
    total = 0
    i = 0
    while i < count:
        total += i
        i += 1
    return total


@micropython.viper
def fast_array_process_viper(data: ptr8, length: int) -> int:
    """Traitement de tableau avec viper (très rapide)"""
    total = 0
    for i in range(length):
        total += data[i]
    return total


# ============================================
# Optimisation avec @micropython.native
# ============================================
# Native compile en code machine natif
# Moins de restrictions que viper mais toujours des limitations

@micropython.native
def fast_loop_native(count):
    """Boucle rapide avec native"""
    total = 0
    for i in range(count):
        total += i * 2
    return total


@micropython.native
def process_list_native(data):
    """Traitement de liste avec native"""
    result = []
    for item in data:
        result.append(item * 2 + 1)
    return result


# ============================================
# Comparaison de performance
# ============================================
def benchmark():
    """Compare les performances des différentes approches"""
    import time
    
    count = 10000
    
    # Python pur
    start = time.ticks_ms()
    total_pure = sum(range(count))
    time_pure = time.ticks_diff(time.ticks_ms(), start)
    
    # Viper
    start = time.ticks_ms()
    total_viper = fast_sum_viper(count)
    time_viper = time.ticks_diff(time.ticks_ms(), start)
    
    # Native
    start = time.ticks_ms()
    total_native = fast_loop_native(count)
    time_native = time.ticks_diff(time.ticks_ms(), start)
    
    print(f"Python pur: {time_pure}ms, résultat: {total_pure}")
    print(f"Viper:      {time_viper}ms, résultat: {total_viper}")
    print(f"Native:     {time_native}ms, résultat: {total_native}")
    
    if time_pure > 0:
        speedup_viper = time_pure / time_viper if time_viper > 0 else 0
        speedup_native = time_pure / time_native if time_native > 0 else 0
        print(f"\nAccélération Viper:  {speedup_viper:.2f}x")
        print(f"Accélération Native: {speedup_native:.2f}x")


# ============================================
# Exemple d'utilisation
# ============================================
if __name__ == "__main__":
    print("Test des optimisations MicroPython")
    print("=" * 40)
    
    # Test simple
    result_viper = fast_sum_viper(100)
    result_native = fast_loop_native(100)
    
    print(f"fast_sum_viper(100) = {result_viper}")
    print(f"fast_loop_native(100) = {result_native}")
    
    print("\nBenchmark:")
    benchmark()
