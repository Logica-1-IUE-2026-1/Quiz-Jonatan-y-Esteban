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
    try:
        op = int(input("¿Desea entrar o salir? \n 1. Salir \n 2. Entrar \n"))
        
        if op == 2:
            cpuerta += 1
            print(f"Personas en el super: {cpuerta}")
        elif op == 1:
            cpuerta -= 1
            print(f"Personas en el super: {cpuerta}")
        else:
            print("Ingrese una opcion valida")
        
        if cpuerta == 0:
            op1 = int(input("¿Salir y Finalizar turno? \n 1. Si \n 2. No \n"))
        
        if op1 == 1:
            jornada = False
        elif op1 == 2:
            cpuerta += 1
        else:
            print("INGRESE UNA OPCION VALIDA!!!!!!!!!")
    except:
        print("INGRESE UNA OPCION VALIDA!!!!!!!!!")

print("MIMIR TIME! 😴")