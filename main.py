from tkinter import *
from tkinter import messagebox
import base64
#window
window=Tk()
window.title("Secret Note")
color0="#533D07"
window.config(background="#533D07")
window.minsize(1000,800)


# Import Image
photo=PhotoImage(file="image1.png")
photo.config(width=1500,height=300)
image_label=Label(window,image=photo)
image_label.place(x=0,y=-50)

#Function
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def saveandenc():
   title= text1.get()
   message= text2.get("1.0", END)
   master_secret =text3.get()

   if len(title)==0 or len(message)==0 or len(master_secret)==0:
       messagebox.showinfo(title="ERROR",message="Please enter your info")
   else:
        message_encrypted= encode(master_secret,message)


        try:

            with open("mysecret.txt","a") as datafile:
               datafile.write(f"{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'{title}\n{message_encrypted}')

        finally:
           text1.delete(0,END)
           text3.delete(0,END)
           text2.delete("1.0" ,END)


def decrypt_notes():
    message_encrypted = text2.get("1.0", END)
    master_secret = text3.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            text2.delete("1.0", END)
            text2.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")
#Labels
color1="#D7B971"
font1=("Segoe Script",20,'normal')
label1=Label(text="Please enter Title:")
label1.config(background=color0,fg=color1,font=font1)
label1.place(x=100,y=300)

label2=Label(text="Please enter Text:")
label2.config(background=color0,fg=color1,font=font1)
label2.place(x=110,y=400)

label3=Label(text="Please enter Password:")
label3.config(background=color0,fg=color1,font=font1)
label3.place(x=50,y=650)

# Text and entry
color3="#453103"
text1=Entry(width=47)
text1.config(background=color1,fg=color3)
text1.place(x=400,y=310)

text2=Text(width=35,height=10)
text2.config(background=color1,fg=color3)
text2.place(x=400,y=410)

text3=Entry(width=47)
text3.config(background=color1,fg=color3)
text3.place(x=400,y=660)

#Button
button1=Button(text="Save & Encrypt",bg=color1,fg=color3,command=saveandenc)
button1.config(width=16,font=("Arial",10,'bold'))
button1.place(x=400,y=700)

button2=Button(text="Decrypt",bg=color1,fg=color3,command=decrypt_notes)
button2.config(width=16,font=("Arial",10,'bold'))
button2.place(x=550,y=700)














window.mainloop()