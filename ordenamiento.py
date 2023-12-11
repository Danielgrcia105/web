import random
import time
 
random.seed(0)
ST = sorted([random.randint(1, 100) for _ in range(15)])
ABC = random.choice(ST)  
 
def busqueda_lineal(li, elemento):
    for i, valor in enumerate(li):
        if valor == elemento:
            return i
    return -1
 
def busqueda_binaria(lista, item):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == item:
            return medio
        elif lista[medio] < item:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
 
inicio = time.time()
IL = busqueda_lineal(ST, ABC)
TI = time.time() - inicio
 
inicio = time.time()
B = busqueda_binaria(ST, ABC)
tB1 = time.time() - inicio
 
print("Lista ordenada:", ST)
print("Elemento a buscar:", ABC)
 
if IL != -1:
    print(f"Búsqueda Lineal: Elemento encontrado en la posición {IL} (Tiempo: {TI} segundos)")
else:
    print("Búsqueda Lineal: Elemento no encontrado")
 
if B != -1:
    print(f"Búsqueda Binaria: Elemento encontrado en la posición {B} (Tiempo: {tB1} segundos)")
else:
    print("Búsqueda Binaria: Elemento no encontrado")
