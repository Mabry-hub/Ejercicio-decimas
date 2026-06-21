#funciones validaciones
def validar_codigo(codigo):    #validar el codigo sin espacios
    return codigo.strip()!=""

def buscar_codigo(reservas, codigo):    #las funciones de validacion de codigo-(que no tenga espacios) y buscar el codigo-(si es que ya existe) pueden fusionarse en una sola funcion
    for reserva in reservas:
        if reserva["codigo"]==codigo:
            return None

def validar_nombre(nombre):
    return nombre.strip()!=""

#funciones opciones y funcionales

def mostrar_menu():
    print("1. Registrar reserva")
    print("2. Buscar reserva")
    print("3. Actualizar reserva")
    print("4. Eliminar reserva")
    print("5. Mostrar reservas")
    print("6. Mostrar estadísticas")
    print("7. Salir")

#OPCION 1
def registrar_reserva(reservas):
    codigo=input("Ingrese codigo de reserva: ").strip()

    if not validar_codigo(codigo):
        print("Error: El código no puede estar vacio")
        return
    if buscar_codigo(reservas, codigo) is not None:
        print("Error: El código de la reserva ya existe")

    nombre=input("ingrese nombre del huésped: ").strip()
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío")
        return
    
    try:
        noches=int(input("Ingrese la cantidad de noches de estadía:"))
        if noches<=0:
            print("Error: La cantidad ingresada tiene que ser mayor a 0.")
            return
    except ValueError:
        print("Error: ", ValueError)
        return
    


    
    
def main():

    reservas=[]

    while True:

        mostrar_menu()

        opcion=leer_opcion(reservas)

        if opcion==1:
            registrar_reserva(reservas)

        elif opcion==2:
            buscar_reserva(reservas)

        elif opcion==3:
            actualizar_reserva(reservas)

        elif opcion ==4:
            eliminar_reserva(reservas)
        
        elif opcion==5:
            mostrar_reservas(reservas)

        elif opcion==6:
            mostrar_estadisticas(reservas)
        
        elif opcion==7:
            print('*Programa finalizado*')
            break
        
main()

