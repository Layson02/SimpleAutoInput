import pyautogui
import time

def pressionar_tecla(tecla, intervalo_segundos, repeticoes):
    print("O script vai começar em 3 segundos...")
    time.sleep(3) # Tempo de preparo
    
    for i in range(repeticoes):
        pyautogui.press(tecla)
        print(f"Tecla '{tecla}' pressionada ({i+1}/{repeticoes})")
        time.sleep(intervalo_segundos)
        
    print("Script finalizado!")

# Configurações: Tecla, Intervalo (segundos), Vezes (x)
tecla_desejada = 'f' # Ex: 'a', 'enter', 'f5'
intervalo = 2.0 
quantidade_vezes = 5

pressionar_tecla(tecla_desejada, intervalo, quantidade_vezes)