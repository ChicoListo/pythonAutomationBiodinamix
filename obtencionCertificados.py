import requests
from bs4 import BeautifulSoup
import urllib.parse

lotNumber = '33TNCY'

# URL base y parámetros del formulario
base_url = 'https://www.neogen.com/document-search/'
params = {'lotNumber': lotNumber}

# Realizar la solicitud GET al formulario
response = requests.get(base_url, params=params)

if response.status_code == 200:
    # Parsear el HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar la tabla de resultados
    table = soup.find('table', class_='table table-striped table-responsive')
    if table:
        # Iterar sobre las filas de la tabla
        for row in table.find_all('tr')[1:]:  # Empezar desde 1 para omitir la fila de encabezados
            columns = row.find_all('td')
            if len(columns) >= 2:
                lot_number = columns[1].text.strip()
                document_link = columns[1].find('a')['href']
                document_type = columns[2].text.strip()
                language = columns[3].text.strip()

                # Descargar el documento usando el enlace encontrado
                document_url = urllib.parse.urljoin(base_url, document_link)
                document_response = requests.get(document_url)

                if document_response.status_code == 200:
                    # Guardar el documento en un archivo local
                    filename = f"{lot_number}_{document_type.replace(' ', '_')}.pdf"
                    with open(filename, 'wb') as f:
                        f.write(document_response.content)
                    
                    print(f"Documento descargado: {filename}")
                else:
                    print(f"Error al descargar el documento {lot_number}: {document_response.status_code}")
    else:
        print("No se encontró la tabla de resultados en la página.")
else:
    print(f"Error al realizar la solicitud al servidor: {response.status_code}")
