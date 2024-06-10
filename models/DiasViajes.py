from datetime import date

class DiasViaje():
    """Clase que representa """
    def __init__(self, fecha):
        self.__fecha = fecha
        self.__gastos = []

    def get_fecha(self) -> date:
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_gastos(self):
        return self.__gastos

    def get_reporte_gastos_diario(self):
        gastos_transporte = 0
        gastos_transporte_efectivo = 0
        gastos_transporte_tarjeta = 0
        gastos_alojamiento = 0
        gastos_alojamiento_efectivo = 0
        gastos_alojamiento_tarjeta = 0
        gastos_alimentacion = 0
        gastos_alimentacion_efectivo = 0
        gastos_alimentacion_tarjeta = 0
        gastos_entretenimiento = 0
        gastos_entretenimiento_efectivo = 0
        gastos_entretenimiento_tarjeta = 0
        gastos_compras = 0
        gastos_compras_efectivo = 0
        gastos_compras_tarjeta = 0
        for gasto in self.__gastos:
            valor_gastado = gasto.get_valor_gastado()
            tipo_gasto = gasto.get_tipo_gasto()
            metodo_pago = gasto.get_metodo_pago()
            if tipo_gasto == 1:
                gastos_transporte += valor_gastado
                if metodo_pago == 1:
                    gastos_transporte_efectivo += valor_gastado
                else:
                    gastos_transporte_tarjeta += valor_gastado

            elif tipo_gasto == 2:
                gastos_alojamiento += valor_gastado
                
                if metodo_pago == 1:
                    gastos_alojamiento_efectivo += valor_gastado
                else:
                    gastos_alojamiento_tarjeta += valor_gastado

            elif tipo_gasto == 3:
                gastos_alimentacion += valor_gastado
                if metodo_pago == 1:
                    gastos_alimentacion_efectivo += valor_gastado
                else:
                    gastos_alimentacion_tarjeta += valor_gastado

            elif tipo_gasto == 4:
                gastos_entretenimiento += valor_gastado
                if metodo_pago == 1:
                    gastos_entretenimiento_efectivo += valor_gastado
                else:
                    gastos_entretenimiento_tarjeta += valor_gastado
            else:
                gastos_compras += valor_gastado
                if metodo_pago == 1:
                    gastos_compras_efectivo += valor_gastado
                else:
                    gastos_compras_tarjeta += valor_gastado
        return gastos_transporte, gastos_transporte_efectivo, gastos_transporte_tarjeta, gastos_alojamiento,
        gastos_alojamiento_efectivo, gastos_alojamiento_tarjeta, gastos_alimentacion, gastos_alimentacion_efectivo,
        gastos_alimentacion_tarjeta, gastos_entretenimiento, gastos_entretenimiento_efectivo, gastos_entretenimiento_tarjeta,
        gastos_compras, gastos_compras_efectivo, gastos_compras_tarjeta

    def get_reporte_gastos_diario_por_metodo_pago(self):
        gastos_efectivo = 0
        gastos_tarjeta = 0
        for gasto in self.__gastos:
            valor_gastado = gasto.get_valor_gastado()
            metodo_pago = gasto.get_metodo_pago()
            if metodo_pago == 1:
                gastos_efectivo += valor_gastado
            else:
                gastos_tarjeta += valor_gastado
        total = gastos_efectivo + gastos_tarjeta
        return gastos_efectivo, gastos_tarjeta, total