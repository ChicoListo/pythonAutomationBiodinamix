import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

# Configuración de Tesseract OCR (puedes necesitar ajustar según tu instalación)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ruta a tesseract.exe en Windows

# Función para procesar una imagen de etiqueta
def procesar_etiqueta(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para obtener una imagen binaria
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Aplicar erosión y dilatación para eliminar ruido
    kernel = np.ones((1, 1), np.uint8)
    binaria = cv2.erode(binaria, kernel, iterations=1)
    binaria = cv2.dilate(binaria, kernel, iterations=1)
    
    # Mostrar la imagen binaria
    plt.imshow(binaria, cmap='gray')
    plt.title('Imagen binaria')
    plt.show()
    
    # Aplicar OCR para reconocer texto
    texto = pytesseract.image_to_string(binaria, lang='eng')  # Puedes ajustar el idioma según sea necesario
    
    return texto.strip()

# Cargar imagen de ejemplo (reemplaza con tu propia imagen)
ruta_imagen = 'ejemplo_etiqueta.jpg'
imagen = cv2.imread(ruta_imagen)

# Procesar la imagen de la etiqueta
texto_etiqueta = procesar_etiqueta(imagen)

# Mostrar el texto reconocido
print('Texto de la etiqueta:')
print(texto_etiqueta)
