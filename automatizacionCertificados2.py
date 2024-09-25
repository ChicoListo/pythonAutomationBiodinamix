import pyautogui
import time

# Espera 1 segundo antes de comenzar para que tengas tiempo de enfocar la ventana de Chrome
time.sleep(1)

# Presiona la tecla Win (la tecla del logotipo de Windows) y selecciona la ventana 2 (suponiendo que Win+2 selecciona la ventana 2)
pyautogui.hotkey('win', '2')
time.sleep(1)

# Activa la ventana usando Alt+F5 (ajustado según tus necesidades)
pyautogui.hotkey('shift', 'f5')
time.sleep(3)

# Realiza 22 veces la acción de presionar Tabulador
for _ in range(22):
    pyautogui.press('tab')
time.sleep(2)

# Escribe el código de lote (ajustado según tu requerimiento)
pyautogui.write('33RYH9')
pyautogui.press('enter')
time.sleep(2)

# Realiza 7 veces la acción de presionar Tabulador
for _ in range(7):
    pyautogui.press('tab')

# Presiona Enter para confirmar la selección
pyautogui.press('enter')
time.sleep(2)

# Realiza 8 veces la acción de presionar Tabulador
for _ in range(8):
    pyautogui.press('tab')

# Presiona Enter para confirmar la acción
pyautogui.press('enter')
time.sleep(2)

# Realiza 2 veces la acción de presionar Tabulador
for _ in range(2):
    pyautogui.press('tab')

# Presiona Enter para finalizar
pyautogui.press('enter')

# Cierra la ventana actual con Ctrl+W
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)

for _ in range(15):
    pyautogui.press('up')

# Vuelve a activar la ventana usando Alt+F5 (ajustado según tus necesidades)
pyautogui.hotkey('shift', 'f5')
