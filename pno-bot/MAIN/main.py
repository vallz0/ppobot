import pyautogui as py
from time import sleep as delay
import random
import pytesseract
import cv2
import re
import tkinter as tk
from tkinter import messagebox


user = "Vallz"
password = "190420Vz"

dc_screen = "Images/dc.png"
reload_button = "Images/reload_button.png"
fight_button = "Images/fight_button.png"
bag_button = "Images/bag_button.png"
run_button = "Images/run_button.png"
Battle = "Images/battle.png"
pokeball_icon ="Images/pokeball_icon.png"

Pokemon = []

def add_pokemon(event=None):
    pokemon = entry_pokemon.get().strip().lower()
    if pokemon:
        listbox_pokemon.insert(tk.END, pokemon)
        Pokemon.append(pokemon)
        Pokemon.append(f"[s]{pokemon}")
        Pokemon.append(f"[e]{pokemon}")
        entry_pokemon.delete(0, tk.END)

def confirm_and_close():
    root.destroy() 
    print(Pokemon)

def show_capture_message():
    messagebox.showinfo("Captura!", f"{Poke.capitalize()} encontrado(a)!\nAgora, vá capturar!!")

# adicionar a outro arquivo e linkar a esse principal
root = tk.Tk()
root.title("Lista de Pokémon")


label_pokemon = tk.Label(root, text="Digite o nome do Pokémon:")
label_pokemon.pack()

entry_pokemon = tk.Entry(root)
entry_pokemon.pack()
entry_pokemon.bind("<Return>", add_pokemon)  

button_add = tk.Button(root, text="Adicionar Pokémon", command=add_pokemon)
button_add.pack()

listbox_pokemon = tk.Listbox(root)
listbox_pokemon.pack()

button_confirm = tk.Button(root, text="Confirmar", command=confirm_and_close)
button_confirm.pack()

root.mainloop()

rn = random.randrange(2,3)


def Check():
    try:
        global isBattle 
        try:
            VS = py.locateCenterOnScreen(Battle,confidence=0.8)
            isBattle = True
        except:
            isBattle = False 
        return isBattle
    except:
        print("erro no check()")

def PokeCheck():
    VS = py.locateCenterOnScreen(Battle,confidence=0.8)
    left,top = VS
    x = left + 48
    y = top - 15
    global output_file
    output_file = "Images/poke_check.png"
    screenshot = py.screenshot(region=(int(x), int(y), 200, 35))
    screenshot.save(output_file)
    imagem = cv2.imread(output_file)
    caminho = r"C:\Users\Public\AppData\Local\Programs\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
    global Poke
    poke = pytesseract.image_to_string(imagem)
    Poke = poke.strip().lower()

    return Poke

def Move():
    py.keyDown('a')
    delay(rn)
    py.keyUp('a')
    delay(0.5)
    py.keyDown('d')
    delay(rn)
    py.keyUp('d')

def Move2():
    py.keyDown('w')
    delay(rn)
    py.keyUp('w')
    delay(0.5)
    py.keyDown('s')
    delay(rn)
    py.keyUp('s')

def Atk():
    py.press('1')
    delay(0.5)
    py.press('1')

def Caught():
    py.press('2')
    delay(0.5)
    py.press('3')

try:
    py.click(604,457)
    
    while True:
        Check()
        if isBattle: # encapsular para fazer function disconnect 
            try:
                PokeCheck()
                if Poke in Pokemon:
                    Caught()
                    delay(0.5)
                    show_capture_message()
                    break
                else:
                    delay(0.5)
                    Atk()
                    delay(0.5)
            except:
                pass
        else: 
            Move()
except KeyboardInterrupt:
    print('\n')
    