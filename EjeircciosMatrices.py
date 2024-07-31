

#1. Desarrollar un algoritmo que calcule el promedio de un arreglo de un arreglo de reales

def promedio_arreglo(x):

    p=0
    for i in range(0,len(x)):
        p += x[i]

    return print(f"el promedio del arreglo es {p/len(x)}")

   

#2. Desarrolle un algoritmo que calcule el punto de dos arreglos de numeros enteros que sean de la misma longitud

def product_punto(v,w):
    
    if len (v) !=  len(w):
        
        raise ValueError ("los arreglos no son de la misma longitud")
    
    producto = sum(v1 * w1 for v1, w1 in zip(v,w))
    return print(f"el punto de los arreglos es ", producto)



def main():
    
     promedio_arreglo([5,4,7,8,5])
     
     product_punto([1,2,3],[4,5,6])
     
     
if __name__ == "__main__":
    main()