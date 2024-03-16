import pyautogui as py
import sys
from time import sleep as delay
import customtkinter
from PIL import Image


# variaveis 

fight_button = "Images/fight_button.png"
bag_button = "Images/bag_button.png"
run_button = "Images/run_button.png"
username1 = "Images/username1.png"



# sistema de click

def click(imagem_arquivo, confianca=0.8):
    try:
        imagem = py.locateCenterOnScreen(imagem_arquivo, confidence=confianca)
        
        if imagem is not None:
            
            py.click(imagem)
            
        else:
            print("Imagem não encontrada.")
    except:
        pass

# sistema de reconhecimento de batalha

def Check(name,cofidence=0.8):
    while True:
        
        global isBattle 
        isBattle = False
        try:
            username = py.locateCenterOnScreen(name,confidence=cofidence)
            isBattle = True
            
        except:
            isBattle = False
        return isBattle


    

# sistema de movimentação

def Move():

    print('Moving..')
    py.keyDown('left')
    delay(2)
    py.keyUp('left')
    py.keyDown('right')
    delay(2)
    py.keyUp('right')
  
    

# sistema de ataque

def Atk():
    
    click(fight_button)
    delay(0.5)
    py.click()

def Run():
    click(run_button)

# fazer aplicação web e aplicativo
print('teste')

# MAIN

try:
    print('teste')
    while True:
       
        Check(username1)
       
        if isBattle == True:
            Atk()

except KeyboardInterrupt:
    print('\n')

