# Trabajando con fechas y horas en Python

from datetime import date, datetime, timedelta
from os import system
if system !=("clear"): system("cls")
import locale
locale.setlocale(locale.LC_ALL,'es_AR.UTF-8') # Cambia el idioma a español (Argentina)


#1 - Obtener la fecha y hora actual
fecha_actual=datetime.now()
print("Fecha y hora actual:", fecha_actual)

#2 - Obtener fecha y hora especifica
specific_date= datetime(2025, 1, 12, 18, 37, 40)
print("\nFecha especifica:", specific_date)

#3 - Formatear fechas 
# Metodo strftime() para formatear fechas
# Pasarle el objeto datetime y el formato especificado
# formato: https://docs.python.org/3/library/datetime.html
format_date = specific_date.strftime("%A %B/%Y %H:%M:%S")
print("\nFecha formateada:",format_date)

#4 - Operaciones con fechas (sumar/restar dias,fechas,horas,meses,años, etc)

yesterday= fecha_actual - timedelta(days=1)
print("\nAyer fue:", yesterday)

tomorrow = fecha_actual + timedelta(days=1)
print("\nMañana será:", tomorrow)

hours12_later = fecha_actual + timedelta(hours=12) # = timedelta(days=0.5) #12 horas
print("\nDentro de 12 horas será:", hours12_later)  

#5 - Obtener componentes individuales de una fecha

year = fecha_actual.year
month = fecha_actual.month

print(f"\nAño: {year} y Mes: {month}")

#6 - Calcular diferencia entre fechas

date1 = datetime.now()
date2 = datetime(2025, 6, 22)
difference = date2 -date1 
print("\nDiferencia entre fechas:", difference)


















