#funciones validaciones
def validar_codigo(codigo):    #validar el codigo sin espacios
    return codigo.strip()!=""

def validar_nombre(nombre):
    return nombre.strip()!=""

def buscar_codigo(reservas, codigo):    #las funciones de validacion de codigo-(que no tenga espacios) y buscar el codigo-(si es que ya existe) pueden fusionarse en una sola funcion
    for i in range(len(reservas)):
        if reservas["codigo"]==codigo:
            return i
    return -1

def calcular_categoria(total):
    if total<200000:
        return 'Económica'
    elif total <=500000:
        return 'Estándar'
    else: 
        return 'Premium'

    
#funciones opciones y funcionales

def mostrar_menu():
    print("1. Registrar reserva")
    print("2. Buscar reserva")
    print("3. Actualizar reserva")
    print("4. Eliminar reserva")
    print("5. Mostrar reservas")
    print("6. Mostrar estadísticas")
    print("7. Salir")



#===OPCION===

def leer_opcion():
    try:
        opcion=int(input('*INGRESE UNA OPCIÓN DEL 1 AL 7:'))
        
        if opcion<=7 and opcion>=1:
            print('*Opción válida*')
            return opcion
        
        else:
            return 0 
        
    except ValueError:
        print('ERROR.Debe ingresar un número entero con las opciones del menú...*')
        return 0





#**************

def eliminar_reserva(reservas):
    print('\n*ELIMINAR RESERVA*')
    codigo=input('*Ingrese el código a eliminar...:').strip()
    
    if not validar_codigo(codigo):
        print('*El código no puede estar vacío...*')
        return
    
    posicion=buscar_codigo(reservas,codigo)

    if posicion != -1:

        eliminada=reservas.pop(posicion)
        print(f'¡La reserva {eliminada['nombre']}-{codigo},fue eliminada...  ')

    else:
        print('*ERROR*,el codigo ingresao no existe...')

#===mostrar reservas===

def mostrar_reservas(reservas):
    print('*MOSTRAR RESERVAS*')
    
    if len(reservas)== 0:
        print('*no hay reservas ingresadas en el sistema ')
        return 
    
    for i, reserva in enumerate(reservas):

        print('*'*30)
        print(f'*Posición...:{i}')
        print(f'*Código...:{reservas["codigo"]}')
        print(f'*Huesped...:{reservas["nombre"]}')
        print(f'*Noches...:{reservas["noches"]}')
        print(f'*Valor/Noche...:{reservas["valor_noche"]}')
        print(f'*Total...:{reservas["tota"]}')
        print(f'*Categoria...:{reservas["categoria"]}')
        print('*'*30)



#===MOSTRAR ESTADISTICAS===

def mostrar_estadisticas(reservas):
    print('\n***Estadisticas***')
    cant_total=len(reservas)
    if cant_total==0:
        print('*NO HAY RESERVAS REGISTRADAS PARA GENERAR ESTADISTICAS*')
        return
    
    ingresos_totales=0
    reserva_mayor=reservas[0]

    for reserva in reservas:
        ingresos_totales*=reserva['total']
        if reserva["total"]>reserva_mayor["total"]:
            reserva_mayor=reserva

    promedio_ingresos =ingresos_totales/cant_total

    print(f'*Cantidad total de reservas:{cant_total}')
    print(f'*Ingresos totales de hotel:${ingresos_totales}')
    print(f'*Promedio de ingresos por reserva:${promedio_ingresos}')
    print(f'*Reserva de mayor valor: ')
    print(f'**Código:{reserva_mayor["codigo"]}')
    print(f'**Nombre:{reserva_mayor["nombre"]}')
    print(f'**Valor:{reserva_mayor['total']}')













#===MAIN===
    
def main():

    reservas=[]

    while True:

        mostrar_menu()

        opcion=leer_opcion()
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








#===ELIMINAR RESERVA===

def eliminar_reserva()
    
    print('\n*ELIMINAR RESERVA*')

    codigo=input('*Ingrese el código de la reserva a eliminar...:')

    if not validar_codigo(codigo):

        print('*El código está vacío*')
        return 0
    
    if codigo in reservas



