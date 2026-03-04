# Simple Auto Keyboard Input

Este repositório contém ferramentas de automação para pressionamento de teclas desenvolvidas em Python. O projeto oferece duas abordagens: uma simples para tarefas cotidianas de interface e uma avançada para jogos ou aplicações que exigem maior compatibilidade.

---

## 🚀 Versões do Projeto

### 1. Standard (`auto.py`)
Uma versão minimalista focada em facilidade de uso e automação de interface padrão.
* **Biblioteca:** Baseado em `pyautogui`.
* **Delay de Preparo:** Inclui um intervalo de 3 segundos antes de começar para você alternar para a janela correta.
* **Configuração:** Permite definir a tecla, o intervalo entre pressões e a quantidade total de repetições.

### 2. Advanced (`autodirect.py`)
Uma versão robusta projetada para jogos (DirectX) e tarefas que exigem controle dinâmico.
* **Biblioteca:** Utiliza `pydirectinput` para compatibilidade com DirectX e `keyboard` para capturar atalhos globais.
* **Antidetecção:** Implementa intervalos aleatórios entre as pressões para evitar comportamentos previsíveis de bot.
* **Controles em Tempo Real (Hotkeys):**
    * `F8`: Alterna o estado do script entre **LIGADO** e **PAUSADO**.
    * `F9`: Encerra o programa de forma imediata (Kill Switch).

---

## 🛠️ Instalação

Para rodar os scripts, instale as dependências necessárias via pip

