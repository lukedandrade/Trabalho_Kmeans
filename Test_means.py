import Kmeans

def iris_f(nome_arq):
    data = open(nome_arq, 'r')
    datalist = data.readlines()
    ret_list = []
    for line in datalist:
        aux = line.split(',')
        ret_list.append([float(aux[0]), float(aux[1])])
    data.close()
    return ret_list

lista_pon = iris_f('iris.txt')

clusters = Kmeans.Kmeans(3, lista_pon)

print(clusters)