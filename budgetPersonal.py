import openpyxl
from openpyxl.chart import BarChart, Reference
import matplotlib.pyplot as plt
from io import BytesIO

def create_budget_spreadsheet(filename):
    # Crear un nuevo libro de trabajo de Excel
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Budget'

    # Datos de ejemplo para el presupuesto
    categories = ['Income', 'Expenses']
    values = [1000, 700]

    # Escribir los datos en la hoja de cálculo
    sheet['A1'] = 'Categories'
    sheet['B1'] = 'Values'

    for i, (category, value) in enumerate(zip(categories, values), start=2):
        sheet[f'A{i}'] = category
        sheet[f'B{i}'] = value

    # Agregar un gráfico de barras usando matplotlib
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Amount')
    ax.set_title('Budget Overview')

    # Convertir el gráfico a bytes y luego a un archivo BytesIO
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Insertar el gráfico en la hoja de cálculo
    img = openpyxl.drawing.image.Image(img_stream)
    img.anchor = 'D1'
    sheet.add_image(img)

    # Guardar el libro de trabajo
    wb.save(filename)
    print(f"Budget spreadsheet '{filename}' created successfully.")

    # Cerrar recursos
    plt.close()
    img_stream.close()

# Ejemplo de uso
if __name__ == '__main__':
    filename = 'budget.xlsx'
    create_budget_spreadsheet(filename)

