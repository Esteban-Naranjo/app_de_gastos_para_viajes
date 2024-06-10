from MetodoPago import MetodoPago
from TipoGasto import TipoGasto

class Gastos():
    def __init__(self, valor_gastado: float, metodo_pago: int, tipo_gasto: int):
        self.__valor_gastado = valor_gastado
        if metodo_pago == 1:
            self.__metodo_pago = MetodoPago.EFECTIVO
        elif metodo_pago == 2:
            self.__metodo_pago = MetodoPago.TARJETA
        else:
            raise ValueError("El gasto no cuenta con un método de pago existente")
        
        if tipo_gasto == 1:
            self.__tipo_gasto = TipoGasto.TRANSPORTE
        elif tipo_gasto == 2:
            self.__tipo_gasto = TipoGasto.ALOJAMIENTO
        elif tipo_gasto == 3:
            self.__tipo_gasto = TipoGasto.ALIMENTACION
        elif tipo_gasto == 4:
            self.__tipo_gasto = TipoGasto.ENTRETENIMIENTO
        elif tipo_gasto == 5:
            self.__tipo_gasto = TipoGasto.COMPRAS
        else:
            raise ValueError("El gasto no cuenta con un tipo de gasto existente")
    
    def get_valor_gastado(self) -> float:
        return self.__valor_gastado
    
    def set_valor_gastado(self, valor_gastado):
        self.__valor_gastado = valor_gastado

    def get_metodo_pago(self) -> int:
        return self.__metodo_pago.value

    def get_tipo_gasto(self) -> int:
        return self.__tipo_gasto.value
