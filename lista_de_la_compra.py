import os # Importo liberia os from system

bienvenida = "Programa lista de la compra" # defino el msg de bienvenida
print(bienvenida) # doy la bienvenida en pantalla
print("-" * len(bienvenida)) # añado "-" por el largo de msg bienvenida

lista = [] # creo la lista de la compra
articulo_nuevo = None
while True: # bucle
    articulo_nuevo = input("¿Qué desea comprar? - [Q] para salir\n"
                           "Respuesta: ")
    if articulo_nuevo == "Q": # si coloco Q, rompo el buque y no vuelvo a preguntar.
        break
    elif articulo_nuevo in lista: # si el artículo está en la lista, lo informo.
        print("¡{} ya está en la lista!".format(articulo_nuevo))
    else: # si no puse Q y no existe en la lista, lo añado a la lista y vuelvo a preguntar de comprar otro item.
        if input("¿Seguro que quieres añadir {} a la lista? [S/N]\n"
                             "Respuesta: ".format(articulo_nuevo)) == "S":
            lista.append(articulo_nuevo)
            print("¡Articulo {} añadido a la lista!".format(articulo_nuevo))

print("La lista de la compra es {}".format(lista)) # una vez roto el bucle, muestro la lista de artículos que hay en ella.