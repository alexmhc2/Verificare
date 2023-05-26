# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def a1():
    lista_valori = [100, 50, 20, 10, 5, 2, 1]
    numar = int(input("Introduceti un numar: "))
    aparitii = [0] * len(lista_valori)

    for i, v in enumerate(lista_valori):
        while numar >= v:
            numar -= v
            aparitii[i] += 1

    print(aparitii)

def a2():
    numar = int(input("Introduceți un număr între 0 și 255: "))
    rezultat = 255 - numar
    print(rezultat)


def fib(n):
    f = [1, 1]
    if n < 2:
        print(f[:n])
    else:
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        print(f)

def minmax():
    lista_str = input()
    lista = lista_str.split()
    lista.sort()

    valoare_minima = lista[0]
    valoare_maxima = lista[-1]

    print("Valoarea minima este:", valoare_minima)
    print("Valoarea maxima este:", valoare_maxima)


def zero(numar):
    if numar == 0:
        return 0

    rest = numar % 10
    if rest == 0:
        k = 1
    else:
        k = 0

    return k + zero(numar // 10)


def cautare(lista, k):
    if k in lista:
        return k
    else:
        return None


def cautare1(lista, element):
    for i, el in enumerate(lista):
        if el == element:
            return i
    return None


def cnp(gen, an, luna, zi, jud, nnn):
    CNP = ""
    if gen == "M" or gen == "m":
        if an < 2000:
            CNP += "1"
        else:
            CNP += "5"
    else:
        if an < 2000:
            CNP += "2"
        else:
            CNP += "6"
    if an < 2000:
        CNP += str(an - 1900)
    else:
        CNP += str(an - 2000)
    if luna < 10:
        CNP += "0"
    CNP += str(luna)
    if zi < 10:
        CNP += "0"
    CNP += str(zi)
    if jud < 10:
        CNP += "0"
    CNP += str(jud)
    if nnn < 10:
       CMP += "00"
    elif nnn<100:
        CNP += "0"
    else:
        CNP += ""
    CNP += str(nnn)
    CNP += str(generareC(CNP))
    return CNP


def generareC(CNP):
    listaControl = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = 0
    for i in range(len(CNP)):
        suma += int(CNP[i])*listaControl[i]
    if suma%11 == 10:
        c = 1
    else:
        c = suma%11
    return c






    if __name__ == '__main__':

