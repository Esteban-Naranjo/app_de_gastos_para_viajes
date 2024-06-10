from datetime import date, timedelta
from DiasViajes import DiasViaje

class Viajes():

    def __init__(self, lugar_destino: str, presupuesto_estimado: float, 
    fecha_inicio: date, fecha_final: date):
        self.__lugar_destino = lugar_destino
        self.__presupuesto_estimado = presupuesto_estimado
        self.__fecha_inicio = fecha_inicio
        self.__fecha_final = fecha_final
        self.__dias_viaje = []
        self.asignar_dias_viaje(self.__fecha_inicio)

    def get_presupuesto_estimado(self) -> float:
        return self.__presupuesto_estimado

    def asignar_dias_viaje(self, fecha_inicio):
        fecha_inicial = fecha_inicio
        while fecha_inicial <= self.__fecha_final:
            dia = DiasViaje(fecha_inicial)
            self.__dias_viaje.append(dia)
            fecha_inicial += timedelta(days=1)

    def get_dias_viaje(self):
        return self.__dias_viaje