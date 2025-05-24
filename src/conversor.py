import json
from datetime import datetime
import random

def cargar_tasas(ruta):
    with open(ruta, "r") as archivo:
      return json.load(archivo)

def convertir(precio_usd, moneda_destino, tasas):
   tasa = tasas["USD"].get(moneda_destino)
   if not tasa:
      raise ValueError("Moneda no soportada")
   return precio_usd * tasa

def registrar_transaccion(producto, precio_convertido, moneda, ruta_log):
    with open(ruta_log, "a") as archivo:
       fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       archivo.write(f"{fecha} | {producto}: {precio_convertido:.2f} {moneda}\n")

# Ejemplo de uso
if __name__ == "__main__":
    tasas = cargar_tasas("../data/tasas.json")
    precio_usd = 100.00
    eur = convertir(precio_usd, "EUR", tasas)
    registrar_transaccion("Laptop", eur, "EUR", "../logs/historial.txt")