import pydirectinput
import time
import random
import keyboard

# Variável global para controlar o estado (ligado/desligado)
rodando = False

def alternar_script():
    global rodando
    rodando = not rodando
    if rodando:
        print("\n[+] Script LIGADO! Pressione 'F8' para pausar.")
    else:
        print("\n[-] Script PAUSADO! Pressione 'F8' para retomar ou 'Esc' para sair totalmente.")

def iniciar_macro(tecla, min_segundos, max_segundos):
    print("=== Configuração do Script ===")
    print("-> Pressione 'F8' a qualquer momento para LIGAR ou DESLIGAR.")
    print("-> Pressione 'F9' para ENCERRAR o programa definitivamente.\n")
    
    # Registra o atalho global para a função de alternância
    keyboard.add_hotkey('f8', alternar_script)
    
    contador = 0
    
    while True:
        # Condição de saída de emergência (Kill Switch total)
        if keyboard.is_pressed('f9'):
            print("\nEncerrando o programa de forma segura...")
            break
            
        if rodando:
            pydirectinput.press(tecla)
            contador += 1
            
            intervalo = random.uniform(min_segundos, max_segundos)
            print(f"Tecla '{tecla}' pressionada ({contador} vezes). Próximo em {intervalo:.2f}s...")
                       
            tempo_passado = 0
            while tempo_passado < intervalo:
                if not rodando or keyboard.is_pressed('esc'):
                    break 
                time.sleep(0.1)
                tempo_passado += 0.1
        else:
            time.sleep(0.1)

# Configurações de execução
tecla_desejada = 'f' 
intervalo_minimo = 0.688 
intervalo_maximo = 2.26 

iniciar_macro(tecla_desejada, intervalo_minimo, intervalo_maximo)