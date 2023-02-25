import serial
from tkinter import *

menu_app = Tk()
menu_app.title("Controle de LED no Arduino")
menu_app.geometry("400x400+200+200")
menu_app["bg"] = "#BDB76B"

#FUNÇÃO PARA ENVIAR COMANDO DE LIGAR 
def liga_led():
    arduino.write('l'.encode())
    return print("LIGADO")
   
   
    

#FUNÇÃO PARA ENVIAR COMANDO DE DESLIGAR   
def desl_led(): 
    arduino.write('d'.encode())
    return print("DESLIGADO")
     
    
             

while True:
    try:
        arduino = serial.Serial('COM3', 9600)
        print("Arduino conectado")
        break
    except:
        pass

#Botão acende

botao_acende = Button(menu_app,bg="#228B22",text="Acender",command= lambda: liga_led())
botao_acende.pack()

#Botão Apaga
botao_apaga = Button(menu_app, bg="#B22222", text="Apaga",command= lambda: desl_led())
botao_apaga.pack()

arduino.flush() 
      

menu_app.mainloop()
