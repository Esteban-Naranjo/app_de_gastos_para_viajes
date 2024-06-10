from pathlib import Path
from models.Viajes import Viajes

class ControlArchivos():
    """Clase que se encarga de la creación y escrictura de archivos"""
    def guardar_reporte(self, viaje: Viajes, ruta: str):
        """Método que escribirá los reportes de gastos en una ruta especificada"""
        if ruta.find('.') > 1: 
            raise ValueError("No incluya un punto en la ruta.")

        ruta_dir = Path(ruta)
        ruta_archivo = Path(ruta + "reportes.txt")
        if ruta_dir.exists():
            dias = viaje.get_dias_viaje()
            for dia in dias:
                gastos_efectivo, gastos_tarjeta, total = dia.get_reporte_gastos_diario_por_metodo_pago()
                gastos_transporte, gastos_transporte_efectivo, gastos_transporte_tarjeta, gastos_alojamiento, gastos_alojamiento_efectivo, gastos_alojamiento_tarjeta, gastos_alimentacion, gastos_alimentacion_efectivo, gastos_alimentacion_tarjeta, gastos_entretenimiento, gastos_entretenimiento_efectivo, gastos_entretenimiento_tarjeta, gastos_compras, gastos_compras_efectivo, gastos_compras_tarjeta = dia.get_reporte_gastos_diario()

                try:
                    with ruta_archivo.open(mode='a', encoding='utf-8') as archivo:
                        archivo.write(f"Gastos para el día {dia.get_fecha()}\n")
                        archivo.write("Según su método de pago: \n")
                        archivo.write("Gastos en efectivo: {gastos_efectivo}\n")
                        archivo.write("Gastos por tarjeta: {gastos_tarjeta}\n")
                        archivo.write("Total: {total} \n --------------- \n")

                        archivo.write("Según su tipo de gasto: \n")
                        archivo.write("Gastos por transporte en efectivo: {gastos_transporte_efectivo}\n")
                        archivo.write("Gastos por transporte en tarjeta: {gastos_transporte_tarjeta}\n")
                        archivo.write("Total: {gastos_transporte}\n")

                        archivo.write("Gastos por alojamiento en efectivo: {gastos_alojamiento_efectivo}\n")
                        archivo.write("Gastos por alojamiento en tarjeta: {gastos_alojamiento_tarjeta}\n")
                        archivo.write("Total: {gastos_alojamiento}\n")

                        archivo.write("Gastos por alimentación en efectivo: {gastos_alimentacion_efectivo}\n")
                        archivo.write("Gastos por alimentación en tarjeta: {gastos_alimentacion_tarjeta}\n")
                        archivo.write("Total: {gastos_alimentacion}\n")

                        archivo.write("Gastos por entretenimiento en efectivo: {gastos_entretenimiento_efectivo}\n")
                        archivo.write("Gastos por entretenimiento en tarjeta: {gastos_entretenimiento_tarjeta}\n")
                        archivo.write("Total: {gastos_entretenimiento}\n")

                        archivo.write("Gastos por compras en efectivo: {gastos_compras_efectivo}\n")
                        archivo.write("Gastos por compras en tarjeta: {gastos_compras_tarjeta}\n")
                        archivo.write("Total: {gastos_compras}\n")
                        archivo.write("-----------------")
                except OSError: 
                    print("Error al importar los datos al archivo de reporte.")
                except IOError:
                    print("Error al intentar crear el archivo")

        else:
            print("La ruta no existe, inténtelo de nuevo")
