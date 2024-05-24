# * Importacion de la libreria random que se usara para generar los numeros.
import random

def quicksort(lista):
  # * Condicion de que la lista tenga mas de una posicion
  if len(lista) > 1:

    # * Definicion de los valores menores y mayores y el inicial
    first_element = lista[0]
    lowers = []
    greaters = []

    # * Cargar los valores valores adecuados a la lista
    for i in lista:
      if i > first_element:
        greaters.append(i)
      elif i < first_element:
        lowers.append(i)
    
    # * Concatenar las listas una vez que esten ordenadas
    order_list = quicksort(lowers) + [first_element] + quicksort(greaters) 
    
    # * Retornar la lista ordenada
    return order_list

  else:
    # * en caso de que no se cumpla la condicion, se devuelve la lista original
    return lista

# * Funcion para generar 20 numeros random
test_list = []
for i in range(0,20):
  n = random.randint(0, 100)
  test_list.append(n)

# * Imprimir el resultado final
print(quicksort(test_list))