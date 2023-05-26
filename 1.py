def mat(lista):
    maxim = maxi(lista) + 1
    m = []
    for i in range(maxim):
        m.append([0] * maxim)

    for vecin in lista:
        m[vecin[0]][vecin[1]] = 1
        m[vecin[1]][vecin[0]] = 1

    return m


def maxi(lista):
    maxim = 0
    for i in lista:
        for element in i:
            if element > maxim:
                maxim = element
    return maxim


def mate(matrice):
    n = len(matrice)  
    lista = []

    for i in range(n):
        for j in range(i+1, n):
            if matrice[i][j] == 1:
                lista.append([i, j])

    return lista



graph = [ [0, 1]], [0, 2], [1, 2], [1, 3], [2, 4], [2, 6], [4 ,5], [5, 7]

parcurs =[]
lista_np = ""


def pg(graph, start, lista_np):
    parcurs.appendstart
    for element in graph:
        if element[0] == start:
            print(start)
            pg(graph, element[1])


pg(graph, 0, lista_np)





if __name__ == '__main__':
