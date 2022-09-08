def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('Cuantos pesos ' + tipo_pesos + ' tienes? '))
    dolares = round((pesos / valor_dolar), 2)
    print ('Tienes $' + str(dolares) + ' dolares')

menu = """ 
    Bienvenido al conversor de monedas🪙.
        
        > 1 - Pesos Colombianos
        > 2 - Pesos Argentinos
        > 3 - Pesos Mexicanos

        Elija una de las opciones:"""

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875)
elif opcion ==2:
    conversor('Argentinos', 65)
elif opcion == 3:
    conversor('Mexicanos', 20.67)
else:
    print('Ingresa una opcion correcta')