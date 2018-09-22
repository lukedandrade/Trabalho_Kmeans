#Versão inicial do kmeans feito por mim
class Cluster(object):

    def __init__(self, ponto):
        self.lista_pontos = [].append(ponto)
        self.centroide = ponto

    def alt_centroide(self, n_ponto):
        x = (self.centroide[0] + n_ponto[0])/2
        y = (self.centroide[1] + n_ponto[1])/2
        self.centroide = [x, y]


def checagem_dist(ponto, lista_pontos):
    aux_index = None
    aux_eud = 0
    for i in range(len(lista_pontos)):
        if aux_eud == 0:
            aux_eud = dist_euclid(ponto, lista_pontos[i])
            aux_ponto = lista_pontos[i]
            aux_index = i

        elif dist_euclid(ponto, lista_pontos[i]) < aux_eud:
            aux_eud = dist_euclid(ponto, lista_pontos[i])
            aux_ponto = lista_pontos[i]
            aux_index = i


    return aux_index, aux_ponto


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
        # Obtenção dos primeiros pontos e remoção destes na lista geral.
        lista_organizada.append(Cluster(lista_pontos.pop(indices_r[aux])))

    while len(lista_pontos) != 0:
        for cluster in lista_organizada:
            index, pont = checagem_dist(cluster.centroide, lista_pontos)
            cluster.lista_pontos.append(lista_pontos.pop(index))
            cluster.alt_centroide(pont)

    return lista_organizada