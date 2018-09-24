#Versão inicial do kmeans feito por mim

#função receberá duas listas contendo valores representativos de x e y e retorna a distância euclidiana entre eles
def dist_euclid(ponto_a, ponto_b):
    dist_x = (ponto_a[0] - ponto_b[0])**2
    dist_y = (ponto_a[1] - ponto_b[1])**2
    euclidiana = (dist_x+dist_y)**(1/2)
    return euclidiana

#Classe representando um cluster. Decisão feita por maior facilidade de trabalhar com objetos.
class Cluster(object):

    def __init__(self, ponto):
        self.lista_pontos = []
        self.lista_pontos.append(ponto)
        self.centroide = ponto
        self.error = 1

    def __str__(self):
        ret_str=''
        for i in self.lista_pontos:
            ret_str = ret_str+"Ponto %s\n"%(i)
        ret_str = "Centroide do cluster %s\n"%(self.centroide)+ret_str
        return ret_str

    def __repr__(self):
        ret_str = ''
        for i in self.lista_pontos:
            ret_str = ret_str + "Ponto %s\n" % (i)
        ret_str = "Centroide do cluster %s\n" % (self.centroide) + ret_str
        return ret_str

    def alt_centroide(self, n_ponto):
        x = (self.centroide[0] + n_ponto[0])/2
        y = (self.centroide[1] + n_ponto[1])/2
        self.centroide = [x, y]

    #calculo para erro total, feito pelo soma de erro quadratico. Definimos erro como sendo a distância entre a centroide e o ponto.
    def error_check(self):
        erro_geral = 0
        for ponto in self.lista_pontos:
            erro_geral = erro_geral + dist_euclid(self.centroide, ponto)**2
        self.error = erro_geral


#Método para checagem da menor distância euclidiana, retornando o indíce e ponto.
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


#Função recebe o número de grupos desejados e lista contendo todos os pontos, em formato de lista ou tupla
def Kmeans(n_grupos, lista_pontos, min_error, n_iterations):
    #Decisão de quais pontos serão os iniciais de forma aleartória, através do index
    from random import sample
    #For para iniciar N listas dentro de uma lista maior, objetivo seria retornar a lista maior contendo N listas
    #internas, representando os clusters.
    lista_organizada = []
    lista_pontos_og = lista_pontos
    iteration = 0
    while iteration <= n_iterations:
        # Decisão de quais pontos serão os iniciais de forma aleartória, através do index
        indices_r = sample(range(0, len(lista_pontos)), n_grupos)
        #Reset da lista de pontos.
        lista_pontos = lista_pontos_og
        for aux in range(n_grupos):
            # Obtenção dos primeiros pontos e remoção destes na lista geral.
            lista_organizada.append(Cluster(lista_pontos.pop(indices_r[aux])))

        #len retorna falso caso a lista esteja vazia, e valores estão sendo removidos da mesma através de .pop()
        while len(lista_pontos) != 0:
            for cluster in lista_organizada:
                #Checagem de menor distância, adição do ponto à lista do cluster e alteração da centroíde do mesmo.
                index, pont = checagem_dist(cluster.centroide, lista_pontos)
                cluster.lista_pontos.append(lista_pontos.pop(index))
                cluster.alt_centroide(pont)

        aux_bool = True
        for cluster in lista_organizada:
            #Checagem de erro em cada cluster
            cluster.error_check()
            aux_bool = aux_bool and (cluster.error <= min_error)

        if aux_bool:
            break

        iteration += 1

    return lista_organizada