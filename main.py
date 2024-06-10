from models.Viajes import Viajes
from control.ControlViajes import ControlViajes
from control.controlArchivos import ControlArchivos
from datetime import date

control_viaje = ControlViajes()
control_archivos = ControlArchivos()

print("A donde será su viaje?")
lugar_destino = input()
print("Se encuentra fuera del país? (s/n)")
respuesta = input()
while respuesta != 's' and respuesta != 'n':
    print("Se encuentra fuera del país? (s/n)")
    respuesta = input()

valores_incorrectos = True
while valores_incorrectos:
    print("Ingrese su fecha inicial y final de su viaje: \n")
    try:
        print("Fecha inicial, año: ")
        f_inicial_año = input()
        f_inicial_año = int(f_inicial_año)
        print("Fecha inicial, mes: ")
        f_inicial_mes = input()
        f_inicial_mes = int(f_inicial_mes)
        print("Fecha inicial, dia: ")
        f_inicial_dia = input()
        f_inicial_dia = int(f_inicial_dia)
        print("Fecha final, año: ")
        f_final_año = input()
        f_final_año = int(f_final_año)
        print("Fecha final, mes: ")
        f_final_mes = input()
        f_final_mes = int(f_final_mes)
        print("Fecha final, dia: ")
        f_final_dia = input()
        f_final_dia = int(f_final_dia)
        valores_incorrectos = False

        fecha_inicial = date(f_inicial_año, f_inicial_mes, f_inicial_dia)
        fecha_final = date(f_final_año, f_final_mes, f_final_dia)
        if fecha_final < fecha_inicial:
            print("La fecha inicial es después de la final. Ingreselas nuevamente")
            valores_incorrectos = True
    except:
        print("Valores incorrectos. Ingrese una fecha válida \n")
    

print('¿Cuál será su presupuesto estimado?')
presupuesto_estimado = input()
presupuesto_incorrecto = True
while presupuesto_incorrecto:
    try:
        presupuesto_estimado = float(presupuesto_estimado)
        presupuesto_incorrecto = False
    except:
        print("Ingrese un valor que corresponda a un número")
        presupuesto_estimado = input()

viaje = Viajes(lugar_destino, presupuesto_estimado, fecha_inicial, fecha_final)
print(viaje.get_dias_viaje())

duracion = True
while duracion: 
    print("Agregue un gasto indicando su fecha, valor gastado, método de pago y tipo de gasto")
    fecha_gasto_invalida = True
    while fecha_gasto_invalida:
        print("Fecha: \n")
        try:
            print("Año: ")
            f_gasto_año = input()
            f_gasto_año = int(f_gasto_año)
            print("Mes: ")
            f_gasto_mes = input()
            f_gasto_mes = int(f_gasto_mes)
            print("Dia: ")
            f_gasto_dia = input()
            f_gasto_dia = int(f_gasto_dia)
            fecha_gasto = date(f_gasto_año, f_gasto_mes, f_gasto_dia)
            fecha_gasto_invalida = False
        except:
            print("Valores incorrectos. Ingrese una fecha válida \n")

    print("Valor gasto: \n")
    valor_gastado = input()

    print("Metodo de pago: ")
    metodo = input()

    print("Tipo de gasto: ")
    tipo = input()

    control_viaje.registrar_gasto(viaje, fecha_gasto, valor_gastado, metodo, tipo)

    print("Desea finalizar su viaje? (s/n)")
    finalizar = input()
    while finalizar != 's' and finalizar != 'n':
        print("Desea finalizar su viaje? (s/n)")
        finalizar = input()
    if finalizar == 's':
        ruta_incorrecta = True
        while ruta_incorrecta:
            print("Indique la ruta donde se guardarán los reportes.")
            ruta = input()
            control_archivos.guardar_reporte(viaje, ruta)
            ruta_incorrecta = False
        duracion = False
