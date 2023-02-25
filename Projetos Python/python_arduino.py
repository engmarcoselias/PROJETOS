import serial
from tkinter import *

menu_app = Tk()
menu_app.title("Acender LED")
menu_app.geometry("400x400+200+200")

def liga_led(valor):
    return
    
                   

while True:
    try:
        arduino = serial.Serial('COM3', 9600)
        print("Arduino conectado")
        break
    except:
        pass

#Botão acende

botao_acende = Button(menu_app, text="Acender",command= lambda: liga_led(arduino.write('l'.encode())))
botao_acende.pack()

#Botão Apaga
botao_apaga = Button(menu_app, text="Apaga",command= lambda: liga_led(arduino.write('d'.encode())))
botao_apaga.pack()

arduino.flush()
       

menu_app.mainloop()