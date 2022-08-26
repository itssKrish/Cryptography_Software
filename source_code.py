# Importing libraries

from ctypes import sizeof
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from functools import partial
import tkinter # library for GUI
from tkinter import messagebox #library for pop-up message

global filename
button_height = 2
button_width = 25

# Browse File Button

def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=[('All files', '*.*')])
    label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

    pass_label.pack()
    password.pack()
    temp_label.pack()
    button_encrypt.pack()
    button_decrypt.pack()

# Encryption Method

def encrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as file:  original = file.read()
    encrypted = fernet.encrypt(original)

    with open(browseFiles.filename, 'wb') as encrypted_file:    encrypted_file.write(encrypted)

    status_label.configure(text="Encrypted") # Messafe after process complition
    status_label.pack()

# Decryption Method

def decrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as enc_file:  encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(browseFiles.filename, 'wb') as dec_file:  dec_file.write(decrypted)

    status_label.configure(text="Decrypted") # Messafe after process complition
    status_label.pack()


# GUI

window = Tk()

window.title('Cryptography Tool')
window.geometry("2736x1824")
window.config(background="black")

main_title = Label(window, text="File Encryption and Decryption Software", width=100, height=2, fg="white", bg="black",font =("Mistral",40))
passwd = StringVar()

submit_para_en = partial(encrypt_file, passwd)
submit_para_de = partial(decrypt_file, passwd)

credit = Label(window,text = "Developers : Krish Tomar & Krishna Thakur", bg="black",height=2,  fg = "white", font =("",15))
label_file_explorer = Label(window, text="File Name : ", width=100, height=2, fg="white", bg="black",font =("",15))
pass_label = Label(window, text="Please Enter Your Password : ", width=100, height=2, fg="white", bg="black",font =("",13))
temp_label = Label(window, text="",height=3, bg="black")

button_explore = Button(window, text="Browse File", command=browseFiles, width=button_width, height=button_height, font =("",15))

password = Entry(window, textvariable=passwd,show="")  #Pasword Box

button_encrypt = Button(window, text="Encrypt", command=submit_para_en, width=button_width, height=button_height, font =("",15)) #Encrypt Button
button_decrypt = Button(window, text="Decrypt", command=submit_para_de, width=button_width, height=button_height, font =("",15)) #Decrypt Button

def open_popup():
   top= Toplevel(window)
   top.geometry("900x350")
   top.title("How to Use?")
   Label(top, text= "                This tool is built to provide better security and to maintain the privacy of people.\n\n                                                          How to use this software?\n\n1) To start encrypting or decrypting any file, first of all, you have to select the desired file(location).\n    for selection of the file location, the 'Browse File' button is given.\n\n2) Then enter your password in the password section.\n\n3) Then in the next step, select the desired operation of 'Encryption' or 'Decryption'.\n\n                                                                      Done !!!\n\nNow you can check your encrypted or decrypted file' in the same location as the originally stored file.", font=('Futura'), justify= LEFT).place(x=5,y=5)

How_to_Use = tkinter.Button(window, text ="How to use?", command = open_popup, width=13, height=1, font =("",15))

How_to_Use.pack(side=TOP, anchor=NE)
status_label = Label(window, text="", width=100, height=4, fg="white", bg="black",font =("",17))

credit.pack()
main_title.pack()
label_file_explorer.pack()
button_explore.pack()

window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda e: window.quit()) #Exit button

window.mainloop()