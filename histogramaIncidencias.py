data = {
    'Categoría': ['Roturas', 'Faltantes', 'Errores de inventario', 'Material Caducado'],
    'Cantidad': [10, 20, 30, 40]
}

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Crear un nuevo libro de Excel
wb = Workbook()

# Activar la hoja activa
ws = wb.active
ws.title = 'Incidencias'

# Escribir los encabezados
ws.append(['Categoría', 'Cantidad'])

# Escribir los datos
for i in range(len(data['Categoría'])):
    ws.append([data['Categoría'][i], data['Cantidad'][i]])

# Crear el gráfico de barras
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "Incidencias en el Almacén"
chart.x_axis.title = 'Categoría'
chart.y_axis.title = 'Cantidad'

# Definir los datos para el gráfico
data_chart = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(data['Categoría']) + 1)
categories = Reference(ws, min_col=1, min_row=2, max_row=len(data['Categoría']) + 1)

chart.add_data(data_chart, titles_from_data=True)
chart.set_categories(categories)

# Posicionar el gráfico dentro de la hoja
ws.add_chart(chart, "D2")

# Guardar el libro de Excel
wb.save("almacen_incidencias.xlsx")
