bloqueo_puerta = True
cpuerta = 0
aire = False
luz = False
op = 0
op1 = 0
jornada = False

while bloqueo_puerta == True:
    
    try:
        cpuerta = int(input("¿Entrar e iniciar turno? \n 0. No \n 1. Si \n"))
    except:
        print("mongolo")
    
    if cpuerta == 1:
        bloqueo_puerta = False
        jornada = True
    if cpuerta > 2 or cpuerta < 0:
        print("Ingrese una opcion valida sapo")
    
while bloqueo_puerta == False and jornada == True and cpuerta >= 0:
    op1 = 0
    aire = True
    luz = True
    print(f"Personas en el super: {cpuerta}")
    print(f"Luz en estado: {luz}")
    print(f"Aire acondicionado en estado: {aire}")
    print(f"bloqueo de puerta: {bloqueo_puerta}")
    try:
        op = int(input("¿Desea entrar o salir? \n 1. Salir \n 2. Entrar \n"))
        
        if op == 2:
            cpuerta += 1
        elif op == 1:
            cpuerta -= 1
        else:
            print("Ingrese una opcion valida")
        
        if cpuerta == 0:
            op1 = int(input("No es posible dejar el supermercado solo, eche pa' entro a no ser... que desee finalizar turno: \n 1. Finalizar turno. \n 2. Seguir chambeando \n"))
                
            if op1 == 2:
                cpuerta += 1
                
            elif op1 == 1:
                aire = False
                luz = False
                bloqueo_puerta = True
                
            else:
                print("INGRESE UNA OPCION VALIDA!!!!!!!!!")
    except:
        print("INGRESE UNA OPCION VALIDA!!!!!!!!!")

print("MIMIR TIME! 😴")
print(f"Personas en el super: {cpuerta}")
print(f"Luz en estado: {luz}")
print(f"Aire acondicionado en estado: {aire}")
print(f"bloqueo de puerta: {bloqueo_puerta}")