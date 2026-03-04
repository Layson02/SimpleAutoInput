# Simple Auto Keyboard Input

This repository contains keyboard automation tools developed in Python. The project offers two approaches: a simple one for everyday interface tasks and an advanced one for games or applications requiring higher compatibility.

---

## 🚀 Project Versions

### 1. Standard (`auto.py`)
A minimalist version focused on ease of use and standard interface automation.
* **Library:** Based on `pyautogui`.
* **Preparation Delay:** Includes a 3-second interval before starting, allowing you to switch to the target window.
* **Configuration:** Allows you to define the key, the interval between presses, and the total number of repetitions.

### 2. Advanced (`autodirect.py`)
A robust version designed for games (DirectX) and tasks requiring dynamic control.
* **Library:** Uses `pydirectinput` for DirectX compatibility and `keyboard` to capture global shortcuts.
* **Anti-detection:** Implements random intervals between presses to avoid predictable bot-like behavior.
* **Real-time Controls (Hotkeys):**
    * `F8`: Toggles the script state between **ON** and **PAUSED**.
    * `F9`: Terminates the program immediately (Kill Switch).

---

## 🛠️ Quick Installation

To install all dependencies at once and ensure the environment is ready for execution, use the `requirements.txt` file:

```bash
pip install -r requirements.txt
