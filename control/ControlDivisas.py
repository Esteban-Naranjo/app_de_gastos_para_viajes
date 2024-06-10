"""Import necesario para las solicitud HTTP"""
import requests

class ControlDivisas():
    """Clase que se encarga de la conversión de dolares o euros, a pesos colombianos"""
    def pasar_de_dolares_a_pesos_colombianos(self, presupuesto: float):
        try:
            response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
            try:
                response_json = response.json()
                return response_json[0]['random'] * presupuesto
            except ValueError:
                print("Ha ocurrido algo inesperado durante la petición")

        except requests.exceptions.ConnectionError:
            print("No se ha podido realizar la conexión al servidor")
            return None
        except requests.exceptions.HTTPError:
            print("No se ha podido convertir el valor")
            return None
        except requests.exceptions.Timeout:
            print("La conversión tardó demasiado en lograrse")
            return None

    def pasar_de_euros_a_pesos_colombianos(self, presupuesto: float):
        dolares = self.pasar_de_dolares_a_pesos_colombianos(presupuesto)
        if dolares is not None:
            return dolares + 200
        return None
