from tkinter import *
from tkinter import messagebox
import subprocess

from psutil import users

############### FUNCTIONS ###############

def getDetails():
    info = subprocess.run('ifconfig', shell=True, capture_output=True)
    return info    

def showNet(net_info):
    messagebox.showinfo(net_info)

############### GUI ###############
app = Tk()
app.title("NIV")
app.geometry("400x300")
Label(app, text="Network Information Viewer").pack()

net_info = getDetails()
Button(app, text="Run", command=showNet(net_info)).pack(pady=20)

Button(app, text="Exit", command=app.quit).pack(side=BOTTOM, pady=20)

app.mainloop()

# PONER EXTENSION .pyw PARA QUE AL HACER DOBLE CLICK SOBRE EL ARCHIVO SE ABRA AUTOMATICAMENTE