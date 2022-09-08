menu = """ 
    Bienvenido al conversor de monedas🪙.
        
        > 1 - Dolares
        > 2 - Euros
        > 3 - Yenes

        Elija una de las opciones:"""

opcion = int(input(menu))
mex = float(input('Cuantos pesos mexicanos tienes? '))
def conversor(mex,divisa,texto):    
    conversion = str(round((mex / divisa) , 2 ))
    print ('Tienes: $' + conversion + texto + '✨')


if opcion == 1:
    conversor(mex,20.27,' Dolares')
elif opcion == 2:
    conversor(mex,20.67,' Euros')
elif opcion == 3:
    conversor(mex,0.15,' Yenes')
else:
    print('Ingresa una opcion correcta')
