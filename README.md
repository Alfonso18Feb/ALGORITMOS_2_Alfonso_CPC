# ALGORITMOS_2_Alfonso_CPC
 link: https://github.com/Alfonso18Feb/ALGORITMOS_2_Alfonso_CPC







# *Buble sort*:
## Bubble sort es una manera para ordenar lista.
## Esto lo consigue mirando por pares de valores de la lista: ejemplo lista[1] y lista[2]
## va comparando consecutivamente hasta llegar al ultimo par que seria lista[len(lista)-2] y lista[len(lista)-1]
## LO que va mirando es si esta ordenada la lista en creciente.
## Si encuentra un valor de la lista donde al compara el primero es superior al siguiente pues lo que hace es permutar esos pares de valores.
## Si no seguiria hasta encontrar una compracion como la explicada antes.
## Cuando al recorrer la lista comprueba que todos los valores estan ordenados entonces devuelve la lista ordenada.
## He escrito el ejemplo en el codigo llamado ordenar.
# Ejemplo: [34, 7, 23, 32, 5]
## 34>7 true entonces: [7,34,23,32,5]
## 34>23 true entonces: [7,23,34,32,5]
## 34>32 true entonces: [7,23,32,34,5]
## 34>5 true entonces: [7,23,32,5,34]
# Volvemos a recorer la lista otra vez para ver si ya esta ordenada si encontramos que hay valor mayores atras pues entonces los movemos como esta escrito arriba
