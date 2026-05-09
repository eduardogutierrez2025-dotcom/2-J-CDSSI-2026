"""
Fecha   :
Grupo   :
Nombre  :


Encontrar que elementos de una lista suman cero

Escribe una clase de python que encuentre 3 elementos que sumen cero
Los elementos se encuentran en una lista y son numeros enteros +-

"""

#Codigo
class Sumacero:
    def buscar(self,lista):
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                for k in range(j+1, len(lista)):
                 if lista[i] +lista[j] + lista[k] == 0:
                     print(lista[i], lista[j], lista[k])
    
    def capturar_numeros(self, limite):
        lista=[]
        cont=0
        while limite>cont:
            cont+=1
            num=int(input(""))
            lista.append(num)
        return lista

#numeros=[-20,-30,-45,-50,-60,-15,10,20,30,8,7]   

s = Sumacero()
limite = int(input("Cuantos numeros tiene la lista? "))
lista = s.capturar_numeros(limite)
s.buscar(lista)



"""
Resutlado
-1 0 1
-1 -2 3
0 2 -2
0 -3 3
1 2 -3
"""
