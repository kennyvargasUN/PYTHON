

#1. Desarrollar un algoritmo que calcule el promedio de un arreglo de un arreglo de reales

def promedio_arreglo(x):

    p=0
    for i in range(0,len(x)):
        p += x[i]

    return p/len(x)

print(promedio_arreglo([5,4,7,8,5]))