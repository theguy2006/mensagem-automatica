import pyautogui
import time
pyautogui.PAUSE = 0.5

#mandar o vídeo
pyautogui.press('win')
pyautogui.write('Brave')
pyautogui.press('enter')
pyautogui.write('https://www.youtube.com/@conanrock')
pyautogui.press('enter')
pyautogui.click(x=1862, y=38)
