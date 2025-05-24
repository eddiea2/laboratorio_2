import random
import json
from datetime import datetime

def cargar_tasas(ruta):
    with open(ruta, "r") as archivo:
      return json.load(archivo)

def convertir(precio_usd, moneda_destino, tasas):
    tasa = tasas["USD"].get(moneda_destino)
    if not tasa:
        raise ValueError("Moneda no soportada")
    return round(precio_usd * tasa, 2)

def registrar_transaccion(producto, precio_convertido, moneda, ruta_log):
    with open(ruta_log, "a") as archivo:
       fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       archivo.write(f"{fecha} | {producto}: {precio_convertido:.2f} {moneda}\n")

def actualizar_tasas(ruta):
    # Simular API: Cambiar tasas aleatoriamente ±2%
    with open(ruta, "r+") as archivo:
       tasas = json.load(archivo)
       
       # Redondear las tasas a 2 decimales antes de guardarlas
       for moneda in tasas["USD"]:
            tasas["USD"][moneda] = round(tasas["USD"][moneda] * (0.98 + (0.04 * random.random())), 2)
       
       tasas["actualizacion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
       # Asegurarse de escribir correctamente el archivo
       archivo.seek(0)  # Mover el cursor al inicio del archivo
       json.dump(tasas, archivo, indent=2)
       archivo.truncate()  # Recortar cualquier contenido extra después del nuevo JSON

# Ejemplo de uso
if __name__ == "__main__":
    actualizar_tasas("data/tasas.json")
    tasas = cargar_tasas("data/tasas.json")
    precio_usd = 100.00
    eur = convertir(precio_usd, "EUR", tasas)
    registrar_transaccion("Laptop", eur, "EUR", "logs/historial.txt")