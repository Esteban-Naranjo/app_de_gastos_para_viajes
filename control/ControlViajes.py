from models.Viajes import Viajes
from models.Gastos import Gastos
from datetime import date

class ControlViajes():
    def buscar_dia_segun_fecha(self, viaje: Viajes, fecha: date):
        dias_viaje = viaje.get_dias_viaje().get_fecha()
        for dia in dias_viaje:
            if dia.fecha == fecha:
                return dia
        return None

    def buscar_fecha(self, viaje: Viajes, fecha: date):
        dias_viaje = viaje.get_dias_viaje()
        for dia in dias_viaje:
            if dia.get_fecha() == fecha:
                return True
        return False

    def calcular_diferencia_presupuesto(self, viaje: Viajes, fecha: date) -> float:
        gasto_diario = 0
        fecha_existe = self.buscar_fecha(viaje, fecha)
        if fecha_existe:
            dia = self.buscar_dia_segun_fecha(viaje, fecha)
            for gasto in dia.get_gastos():
                gasto_diario += gasto.get_valor_gastado()
            return viaje.get_presupuesto_estimado() - gasto_diario
        else:
            print("La fecha indicada no hace parte del viaje en curso")
            return 0

    def registrar_gasto(self, viaje: Viajes, fecha: date, gasto: float, metodo_pago: int, tipo_gasto: int):
        fecha_existe = self.buscar_fecha(viaje, fecha)
        if fecha_existe:
            try:
                gasto_a_registrar = Gastos(gasto, metodo_pago, tipo_gasto)
            except ValueError:
                return

            dia = self.buscar_dia_segun_fecha(viaje, fecha)
            if dia is not None:
                gastos = dia.get_gastos()
                gastos.append(gasto_a_registrar)
                print(self.calcular_diferencia_presupuesto(viaje, fecha))
            else:
                print("No se ha podido registrar el gasto")
        else:
            print("La fecha indicada no hace parte del viaje en curso")

    def imprimir_reportes_diarios(self, viaje: Viajes):
        dias = viaje.get_dias_viaje()
        for dia in dias:
            gastos_efectivo, gastos_tarjeta, total = dia.get_reporte_gastos_diario_por_metodo_pago()
            print(f"Gastos para el día {dia.get_fecha()}\n")
            print("Según su método de pago: \n")
            print("Gastos en efectivo: {gastos_efectivo}\n")
            print("Gastos por tarjeta: {gastos_tarjeta}\n")
            print("Total: {total} \n --------------- \n")

            gastos_transporte, gastos_transporte_efectivo, gastos_transporte_tarjeta, gastos_alojamiento, gastos_alojamiento_efectivo, gastos_alojamiento_tarjeta, gastos_alimentacion, gastos_alimentacion_efectivo, gastos_alimentacion_tarjeta, gastos_entretenimiento, gastos_entretenimiento_efectivo, gastos_entretenimiento_tarjeta, gastos_compras, gastos_compras_efectivo, gastos_compras_tarjeta = dia.get_reporte_gastos_diario()

            print("Según su tipo de gasto: \n")
            print("Gastos por transporte en efectivo: {gastos_transporte_efectivo}\n")
            print("Gastos por transporte en tarjeta: {gastos_transporte_tarjeta}\n")
            print("Total: {gastos_transporte}\n")

            print("Gastos por alojamiento en efectivo: {gastos_alojamiento_efectivo}\n")
            print("Gastos por alojamiento en tarjeta: {gastos_alojamiento_tarjeta}\n")
            print("Total: {gastos_alojamiento}\n")

            print("Gastos por alimentación en efectivo: {gastos_alimentacion_efectivo}\n")
            print("Gastos por alimentación en tarjeta: {gastos_alimentacion_tarjeta}\n")
            print("Total: {gastos_alimentacion}\n")

            print("Gastos por entretenimiento en efectivo: {gastos_entretenimiento_efectivo}\n")
            print("Gastos por entretenimiento en tarjeta: {gastos_entretenimiento_tarjeta}\n")
            print("Total: {gastos_entretenimiento}\n")

            print("Gastos por compras en efectivo: {gastos_compras_efectivo}\n")
            print("Gastos por compras en tarjeta: {gastos_compras_tarjeta}\n")
            print("Total: {gastos_compras}\n")
            print("-----------------")