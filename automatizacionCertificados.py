import pyautogui
import time

# Espera 5 segundos antes de comenzar para que tengas tiempo de enfocar la ventana de Chrome
time.sleep(1)

# Presiona la tecla Win (la tecla del logotipo de Windows)
pyautogui.press('win')
time.sleep(1)

# Escribe "chrome" y presiona Enter para abrir Chrome
pyautogui.write('chrome')
pyautogui.press('enter')

# Espera a que Chrome se abra (ajusta el tiempo según sea necesario)
time.sleep(2)

# Presiona Ctrl + Shift + O para abrir la configuración de Chrome
pyautogui.hotkey('ctrl', 'shift', 'o')

# Espera un momento para que la configuración se abra (ajusta el tiempo según sea necesario)
time.sleep(1)

# Realiza tres veces la acción de presionar Tabulador
for _ in range(3):
    pyautogui.press('tab')

# Presiona la tecla de flecha abajo una vez
pyautogui.press('down')

# Presiona Enter para confirmar la selección
pyautogui.press('enter')
time.sleep(3)

# Realiza 22 veces la acción de presionar Tabulador
for _ in range(22):
    pyautogui.press('tab')

time.sleep(3) 

# Escribe codigo de lote
pyautogui.write('3000003718')
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
