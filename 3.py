# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def adunare2():
    print("Introduceti un numar natural cu doua cifre")
    x = int(input())
    z = x // 10
    u = x % 10
    print(z+u)


def adunare3():
    print("Introduceti numarul de gaini")
    g = int(input())
    print("Introduceti numarul de oi")
    o = int(input())
    print("Numarul de capete este ", int(g) + int(o))
    print("Numarul de picioare este ", 2 * int(g) + 4 * int(o))

def arievolumcub():
    print("Introduceti latura cubului")
    l = input()
    print("Aria cubului este ", int(l) ** 2 * 6)
    print("Volumul cubului este ", int(l) ** 3)

def numar():
    print("Scrieti un numar de 3 cifre")
    c = int(input())
    a = c // 100 * 10
    b = c % 10
    print(a+b)


def ora():
    o = int(input())
    m = int(input())
    print(" Introduceti minutele ")
    u = int(input())
    p = m + o * 60 + u

    k = p // 60
    a = p % 60
    print("Ora noua este ", k,":",a)

def globuri():
    print("inmtroduceti numarul de globuri albe")
    a = int(input())
    r = a * 2
    v = r - 3
    print("Numarul de globuri", a+r+v)


def numaranimale():

    print("Introduceti numarul de caini")
    c = int(input())
    p = c * 2
    g = p * 2
    print("Numarul de animale este", c+p+g)


def schimbare():
    cuvant = input().strip()
    print(cuvant)
    index = 0
    for caracter in cuvant:
        if caracter in 'aeiou' :
            print(caracter.upper(), "am gasit vocala" )
        else:
            print(caracter, index)
        index = index + 1


def ulimasiprima():
    index = 0
    cuvant = input().strip()
    n = ""
    for caracter in cuvant:
        if index == 0 or index==len(cuvant)-1:
            n = n + caracter.upper()
        else:
            n = n + caracter
        index = index + 1
    print(n)


def sufixprefix():
    sufix = "_"
    prefix = "#"
    cuvant = input()
    n = prefix + cuvant.strip() + sufix
    print(n)

def extragsufixprefix():
    nr = 2
    cuvant = input()
    print(cuvant[:nr], cuvant[-nr:])

def inserare():
    cuvant = input()
    n = ""
    for caracter in cuvant:
        if caracter in 'aeiouAEIOU':
            n += caracter + '#'
        else:
            n += caracter
    print(n)


def nr():
    cuvant = input()
    k = 0
    for caracter in cuvant:
        if caracter == 'a':
            k += 1

    print(k)


def lista():
    l = [234, 100, 90, 300, 111, 2, 1, 5, 0]
    jumatate = len(l) // 2
    l1 = l[:jumatate:]
    l1.sort()
    print(l1)
    l2 = l[jumatate::]
    l2.sort()
    print(l2)
    print(l)


def adunare():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a+b=", a + b)


def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b=", a - b)


def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b=", a * b)


def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a:b=", a // b)


def meniu():
    print("apasati 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire")
    opt = input().strip()
    if opt == "1":
        print("adunare")
        adunare()
    else:
        if opt == "2":
            print("scadere")
            scadere()
        else:
            if opt == "3":
                    print("inmultire")
                    inmultire()
            else:
                if opt == "4":
                    print("impartire")
                    impartire()
                else:
                    if opt == "5":
                        sir5()
                    else:
                        print("eroare")

def incadrare():
    print("introduceti o valoare pentru incadrare")
    nr = int(input())
    if nr >= 0 and nr <4000:
        print("mic")
    else:
        if nr >=4000 and nr<8000:
            print("mediu")
        else:
            print("mare")


def sir5():
    print("introduceti un sir")
    sir = input()
    k = 0
    for i in range(0, len(sir),1):
        if sir[i]=="5":
            k += 1
    print(k)



def lista5():
    print("introduceti un sir")
    l = input().split(",")
    k = 0
    for i in range(len(l)):
        if l[i]=="5":
            k += 1
    print(k)

def matrice():
    nr_coloane = int(input())
    nr_randuri = nr_coloane
    i = 0
    j = 0
    print("Introduceti elementele matricei patratice:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j]=int(input())
    sumadiagonalap = 0
    sumadiagonalas = 0

    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if i<j:
                sumadiagonalap += matrice[i][j]

            if i+j < nr_randuri - 1 :
                sumadiagonalas += matrice[i][j]
    print("Suma elementelor de sub diagonala principala:", sumadiagonalap)
    print("Suma elementelor de deasupra diagonala principala:", sumadiagonalas)


def matrice1():
    nr_coloane = int(input())
    nr_randuri = int(input())
    i = 0
    j = 0
    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j]=int(input())
            matrice[i][j]=matrice[i][j]**2

    print(matrice)

def matrice3():
    nr_coloane = int(input())
    nr_randuri = int(input())
    i = 0
    j = 0
    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]+10

    print(matrice)



def lista100():
        print("introduceti un sir")
        l = input().split(",")
        for i in range(len(l)):
            if l[i] == "100":
                print(i)

def matriceip():
    nr_coloane = int(input())
    nr_randuri = int(input())
    i = 1
    j = 1
    sumap = 0
    sumai = 0
    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())


    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if matrice[i][j]%2==0:
                sumap=sumap+matrice[i][j]
            else:
                sumai=sumai+matrice[i][j]

    print(sumap, sumai)

def matricep10():
    nr_coloane = int(input())
    nr_randuri = int(input())
    i = 1
    j = 1
    sumap = 0

    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())


    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if matrice[i][j]%2==0 and matrice[i][j]>10:
                sumap=sumap+matrice[i][j]

    print(sumap)


def listap():
        p = 1
        l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 6]
        for i in range(len(l)):
            if i > 5:
                p = p * l[i]//2
        print("Produsul jumatatilor este ",p)


def listav():
    val = int(input())
    l = [12, 14, 50, 1231, 123123, 10, 11]
    for i in range(len(l)):
        if l[i] == val:
            print(l[i] * l[i] // 2 + l[i] ** 4)

def matriceb():
    nr_coloane = int(input())
    nr_randuri = nr_coloane
    i = 1
    j = 1
    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if i-j==1 or i-j==-1:
                print(matrice[i][j] )

def matricec():
    nr_coloane = int(input())
    nr_randuri = nr_coloane
    i = 1
    j = 1
    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            if i+j==nr_coloane or i+j==nr_coloane-2:
                print(matrice[i][j] )
#doresc sa se calculeze fiecarei element peste 5 index, dupa produsul tuturor jumatatilor  ]
#in lista mea sa se faca cautarea unui element citit de la tastatrura iar daca se gaseste elementul sa se calculeze
#val *val//2 + valloare ** 4

def adunare(a,b):
    return a+b


def produs(*args):
    p = 1
    for element in args:
        p *= element
    return p

def factorial(n):
    f=1
    for e in range(1,n+1):
        f *= e

    return f




def cautare(l, c):
    for e in range(len(l)):
        if l[e]== c:
            return e

    return -1



def cautaresir(sirp, subsir):
    i = 0
    n = len(sirp) - len(subsir)
    while i <= n:
        j = 0
        while j < len(subsir):
            if sirp[i+j] != subsir[j]:
                j = j + 1
                break
            else:
                j = j + 1
        if j == len(subsir):
            return i
        i = i + j
    return -1


def adunare(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


def adunarerec(n):
    if n == 1:
        return 1
    return n + adunarerec(n-1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def fib(n):
    f = 0
    t1 = 0
    t2 = 1
    for i in range(2, n+1):
        f = t1 + t2
        t1 = t2
        t2 = f
    return f


def fibrec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibrec(n-1) + fibrec(n-2)


def aparrec(n):
    sir = str(n)
    c = 0
    if sir[len(sir)  -1]=="0":
        c = 1
    if len(sir)-1<=0:
        return c
    return c + aparrec(int(sir[:len(sir)-1]))

def nat(n):
    sir = str(n)
    c = sir[len(sir)-1]
    if len(sir)-1<=0:
        return c
    return c + ", " + nat(int(sir[:len(sir)-1]))


def spectacol(l):
    l = sorted(l, key = lambda el: el[1])
    print(l)
    final = [l[0]]
    orasfarsit = l[0][1]
    for spec in l:
        if spec[0] >= orasfarsit:
            final.append(spec)
            orasfarsit = spec[1]
    print(final)
    print(len(final))


def rucsac(bag, gmax):
    bag = sorted(bag, key = lambda k: k[1]/k[0], reverse=True)
    r = []
    g = 0
    val = 0
    for e in bag:
        if g + e[0] <= gmax:
            r.append(e)
            g = g + e[0]
            val = val + e[1]
        else:
            fract = gmax - g
            if fract + g <= gmax:
                r.append([fract, fract*e[1]//e[0]])
                g = g + fract
                val = val + fract*e[1]//e[0]
    print(r, g, val)


def masini(mas, timp_lucru):
    mas = sorted(mas, key = lambda k: k)
    final = []
    tl = 0
    for m in mas:
        if tl + m <= timp_lucru:
            tl += m
            final.append(m)
    print(final, tl)


def pr1():
    nr = int(input())
    p = 1
    k = 0
    while nr > 0:
        if nr % 10 == 8:
            k = k + 1
        if nr % 2 == 0:
            c = nr % 10
            p = p * c
        nr = nr / 10
    print(k, p)



def pr2():
        m = int(input())
        n = m
        i = 1
        j = 1
        sumap = 0
        print("Introduceti elementele matricei:")
        matrice = [[0] * m for k in range(n)]
        for i in range(n):
            for j in range(m):
                matrice[i][j] = int(input())

        for i in range(n):
                if matrice[i][i] % 2 == 1:
                    sumap = sumap + matrice[i][j]
        print(sumap)

def pr3():
    n = 1
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
    d = {}
    for i in range(len(l)):
        d[l[i]]=l[i].upper() + '-' + str(n)
        n += 1
    print(d)


def cautarematrice():
    nr_coloane = int(input())
    nr_randuri = int(input())
    i = 1
    j = 1


    print("Introduceti elementele matricei:")
    matrice = [[0] * nr_coloane for k in range(nr_randuri)]
    for i in range(nr_randuri):
        for j in range(nr_coloane):
            matrice[i][j] = int(input())
    print("Introduceti elementul care trebuie cautat in matrice")
    m = int(input())
    for nr_randuri in range(len(matrice)):
        for nr_coloane in range(len(matrice[0])):
            if matrice[nr_randuri][nr_coloane] == m:
                return 1
    return 0


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

if __name__ == '__main__':
    # exit_ = ""
    # while exit_ != "0":
    #     meniu()
    #     print("Pentru iesire tastati 0 sau orice alta tasta pentru continuare1")
    #     exit_ = input().strip()
    #print(produs(1,2,3))
    #l = ["a"]
    #print(cautare(l,"a"))
    #l = [ [1,8], [8,12], [8,10], [14,16], [12,14]]
    #inv = [[10, 200], [4, 500], [34, 250], [1, 10], [10, 10], [40, 1000]]
    #tmp = [6, 2, 4, 3, 2, 5, 10, 20, 3]
    #masini(tmp, 24)
    #pr1()
    #pr2()
    cautarematrice()
#matrice si un numar natural, functia return true daca gaseste n in matrice
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
