from math import sqrt


# ---------------- TALLER ----------------

# Ejercicio 1 - CRUD de pasajeros con clase Pasajero + list

class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)

# --- Programa principal ---
lista = []
while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar por nombre 7.Salir")   # Agregado
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")
    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")
    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")
    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")
    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")
    elif op == "6":                                    # Agregado
        lista.sort(key=lambda p: p.nombre)
        print("Ordenado por nombre ✓")
    elif op == "7":
        break


# Ejercicio 2 - Estadísticas de una lista de notas

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Python trae todo esto:
print(f"Promedio: {sum(notas) / len(notas):.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0
for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1
print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")

# Agregado: desviación estándar
prom = sum(notas) / len(notas)
desviacion = sqrt(sum((n - prom) ** 2 for n in notas) / len(notas))
print(f"Desviación estándar: {desviacion:.2f}")


# Ejercicio 3 - Ordenar una lista (bubble sort)

def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr

# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']

# Agregado: selection sort
def selection_sort(lista):
    n = len(lista)
    arr = lista[:]
    for inicio in range(n - 1):
        pos_min = inicio
        for i in range(inicio + 1, n):
            if arr[i] < arr[pos_min]:
                pos_min = i
        arr[inicio], arr[pos_min] = arr[pos_min], arr[inicio]
    return arr


print(selection_sort(notas))


# ---------------- PROPUESTOS ----------------

# P1 - Contar apariciones de un valor
lista = [1, 3, 2, 3, 4, 3]
v = 3

# Manual
cuenta = 0
for x in lista:
    if x == v:
        cuenta = cuenta + 1
print(f"{v} aparece {cuenta} veces")

# Atajo
print(f"{v} aparece {lista.count(v)} veces")


# P2 - Invertir una lista
lista = [1, 2, 3, 4, 5]

# Manual
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Atajo
print(lista[::-1])


# P3 - Números únicos
nums = [1, 3, 2, 3, 4, 1]

# Manual
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)

# Atajo
print(list(dict.fromkeys(nums)))


# P4 - Segundo mayor
nums = [5, 2, 9, 7, 9, 3]

# Manual
mayor = float("-inf")
segundo = float("-inf")
for n in nums:
    if n > mayor:
        segundo = mayor
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n
print("Segundo mayor:", segundo)

# Atajo
print("Segundo mayor:", sorted(set(nums))[-2])


# P5 - Fusionar dos listas ordenadas
a = [1, 3, 5]
b = [2, 4, 6, 8]

# Manual
resultado = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i = i + 1
    else:
        resultado.append(b[j])
        j = j + 1
while i < len(a):
    resultado.append(a[i])
    i = i + 1
while j < len(b):
    resultado.append(b[j])
    j = j + 1
print(resultado)

# Atajo
print(sorted(a + b))