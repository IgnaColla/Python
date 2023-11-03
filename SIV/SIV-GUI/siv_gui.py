import subprocess

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def gather_info():
    #print("Test")
    info = subprocess.run(["systeminfo"], capture_output=True, text=True, check=True)
    print(info.stdout)

f1 = customtkinter.CTkFrame(master=root)
f1.pack(pady=20, padx=60, fill="both", expand=True)

l1 = customtkinter.CTkLabel(master=f1, text="System Information Viewer")
l1.pack(pady=12, padx=10)

b1 = customtkinter.CTkButton(master=f1, text="Run", command=gather_info)
b1.pack(pady=12, padx=10)

tb1 = customtkinter.CTkTextbox(master=f1)
tb1.pack()

root.mainloop()
