#Versão inicial do kmeans feito por mim


#função receberá duas listas contendo valores representativos de x e y e retorna a centroide entre eles
def ret_centroide(ponto_a, ponto_b):
    centroide = [(ponto_a[0]+ponto_b[0])/2, (ponto_a[1]+ponto_b[1])/2]
    return centroide

#função receberá duas listas contendo valores representativos de x e y e retorna a distância euclidiana entre eles
def dist_euclid(ponto_a, ponto_b):
    dist_x = (ponto_a[0] - ponto_b[0])**2
    dist_y = (ponto_a[1] - ponto_b[1])**2
    euclidiana = (dist_x+dist_y)**(1/2)
    return euclidiana

#Função recebe o número de grupos desejados e lista contendo todos os pontos, em formato de lista ou tupla
def Kmeans(n_grupos, lista_pontos):
    #Decisão de quais pontos serão os iniciais de forma aleartória, através do index
    from random import sample
    indices_r = sample(range(0, len(lista_pontos)), n_grupos)

    #For para iniciar N listas dentro de uma lista maior, objetivo seria retornar a lista maior contendo N listas
    #internas, representando os clusters.
    lista_organizada = []
    for aux in range(n_grupos):
        lista_organizada.append([])
        #Obtenção dos primeiros pontos e remoção destes na lista geral.
        lista_organizada[aux].append(lista_pontos.pop(indices_r[aux]))

