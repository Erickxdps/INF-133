
#metodo burbuja

def burbuja(v, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

#metodo seleccion

def seleccion(v, n):
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if v[j] < v[k]:
                k = j
        v[k], v[i] = v[i], v[k]

#metodo insercion

def seleccion(v, n):
    for i in range(n - 1):
        tmp = v[i]
        j = i-1
        while(v[j] > tmp and j >= 0):
            v[j+1] = v[j]
            j-=1
        v[j+1] = tmp

# Merge Sort
def combinar(resp, izq, der):
    i, j = 0, 0
    for k in range(len(resp)):
        if i >= len(izq):
            resp[k] = der[j]
            j += 1
            continue
        if j >= len(der):
            resp[k] = izq[i]
            i += 1
            continue
        resp[k] = izq[i] if izq[i] < der[j] else der[j]
        if izq[i] < der[j]:
            i += 1
        else:
            j += 1

def ordenacionCombinacion(v):
    n = len(v)
    if n <= 1:
        return
    mitad = n // 2
    izq = v[0:mitad]
    der = v[mitad:n]
    ordenacionCombinacion(izq)
    ordenacionCombinacion(der)
    combinar(v, izq, der)


# Shell Sort

def ordenacionShell(v):
    n = len(v)
    incremento = n 
    # Emulando do-while en Python
    while True:
        incremento = incremento // 2
        for k in range (incremento):
            i=incremento+k
            for i in range(n):
                j = i
                while( j - incremento >= 0 and v[j]<v[j-incremento]):
                    tmp = v[j]
                    v[j] = v[j-incremento]
                    v[j-incremento] = tmp
                    j -= incremento
        if incremento > 1 :
            break

# Quick Sort

def ordenacionRapida(v):
    n = len(v)
    quickSort(v,0,n-1)
    
def quickSort(v,inicio,fin):
    if(inicio>=fin):
        return
    pivote = v[inicio]
    izq = inicio + 1
    der = fin
    while(izq <= der):
        while(izq <= fin and v[izq] < pivote):
            izq +=1
        while(der > inicio and v[der] >= pivote):
            der -=1
        if(izq<der):
            tmp = v [izq]
            v[izq] = v[der]
            v[der] = tmp
    if(der>inicio):
        tmp = v[inicio]
        v[inicio] = v[der]
        v[der] = tmp
    quickSort(v,inicio,der-1)
    quickSort(v,der+1,fin)

# Ejemplo de uso
V = [5, 3, 4, 1, 2, 6]
n = len(V)

# burbuja(V, n)
# print("Burbuja:", V)

#seleccion(V,n)
#print("Seleccion:", V)

#seleccion(V,n)
#print("insercion:", V)

#ordenacionCombinacion(V)
#print("Merge Sort",V)

#ordenacionShell(V)
#print("Shell Sort",V)

#ordenacionRapida(V)
#print("Quick Sort", V)



 