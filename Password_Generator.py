from tkinter import *
import customtkinter as ct
import pyperclip 
import random

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

root = ct.CTk()
root.geometry("700x450")
root.title('PASSWORD GENERATOR')
password=""

def generate():
    global password
    c = []
    pwdList = []
    password=""
    try:
        lene, caps, small, spc, num, sym = int(e.get()), cpl.get(), sml.get(), space.get(), n.get(), symb.get()

        x=[caps,small,spc,num,sym]
        for i in range(len(x)):
            if x[i] != 0:
                c.append(i+1)

        rec = { 1 : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 
                2 : ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                3 : [' '],
                4 : ['1','2','3','4','5','6','7','8','9','0'],
                5 : ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "/", "?","<",">", ",", ".", "'", '"', '\\'] }
        
        if lene >= len(c):
            for i in range(0,len(c)):
                pwdList.append(random.choice(rec[c[i]]))
                lene = lene - 1

        while(lene > 0):
            pwdList.append(random.choice(rec[random.choice(c)]))
            lene = lene - 1
            if lene == 0:
                break

        random.shuffle(pwdList)   
        password = "".join(pwdList)

        output2.delete(0, END)
        output.delete(0, END)
        output.insert(0, password)
    
    except:
        output.delete(0, END)
        output2.delete(0, END)
        output2.insert(0, "INVALID!")
    
def copyClipboard():
    pyperclip.copy(password)  

frame1 = ct.CTkFrame(root, fg_color="transparent", width=150, height= 50)
frame2 = ct.CTkFrame(root, fg_color="transparent", width=150, height= 50)
frame3 = ct.CTkFrame(root, fg_color="transparent", width=150, height= 50)
frame4 = ct.CTkFrame(root, fg_color="transparent", width=150, height= 50)
frame5 = ct.CTkFrame(root, fg_color="transparent", width=150, height= 50)
frame1.pack(side=TOP, pady=40)
frame2.pack(side=TOP, pady=20)
frame3.pack(side=TOP, pady=10)
frame4.pack(side=TOP)
frame5.pack(side=TOP, pady=20)

label = ct.CTkLabel(frame1,text="Password Length:", font=('Verdana', 35, 'bold'))  
label.pack(side=LEFT,padx=5)
e = ct.CTkEntry(frame1,width=100, height=40, corner_radius = 5, font=('Bookman Old Style', 25, 'bold'))
e.pack(side = LEFT, padx=5, pady=(5,0))

cpl = IntVar()
sml = IntVar()
space = IntVar()
n = IntVar()
symb = IntVar()

letter_caps = ct.CTkCheckBox(frame2, text='Uppercase',font=('Verdana', 15, 'bold'), variable=cpl, hover_color="#990000", checkmark_color="white",fg_color="#990000",command=generate).pack(side=LEFT,padx = 10)
letter_small = ct.CTkCheckBox(frame2, text='Lowercase',font=('Verdana', 15, 'bold'), variable=sml,command=generate).pack(side = LEFT,padx = 10)
letter_numbers = ct.CTkCheckBox(frame2, text='Numbers',font=('Verdana', 15, 'bold'), variable=n,  hover_color="#990000", checkmark_color="white",fg_color="#990000",command=generate).pack(side = LEFT,padx = 10)
letter_symbols = ct.CTkCheckBox(frame2, text='Symbols',font=('Verdana', 15, 'bold'), variable=symb,command=generate).pack(side = LEFT,padx = 10)
letter_space = ct.CTkCheckBox(frame2, text='Blank Space',font=('Verdana', 15, 'bold'), variable=space, hover_color="#990000", checkmark_color="white",fg_color="#990000",command=generate).pack(side = LEFT,padx = 10)

label = ct.CTkLabel(frame3,text="Your Password:", font=('Verdana', 25, 'bold'))
label.pack(side=LEFT,padx=5)

output = ct.CTkEntry(frame3, width=300, height= 40, corner_radius=5, text_color="White", font=('Verdana', 20, 'bold'))
output.pack(side = LEFT, padx=5, pady=(5,0))

output2 = ct.CTkEntry(frame4, width=120, height= 40, corner_radius=5, text_color="Red", font=('Verdana', 20, 'bold'), fg_color="transparent", border_width=0)
output2.pack(ipadx=0, ipady=0)

bre = ct.CTkButton(frame5, text="Regenerate", width=200, height= 50, font=('Verdana', 20, 'bold'), corner_radius=35, fg_color="#990000", hover_color="#6b0000", command=generate)
bre.pack(side=LEFT, padx = 20)

b2 = ct.CTkButton(frame5, text="Copy", width=200, height= 50, font=('Verdana', 20, 'bold'), corner_radius=35, command=copyClipboard)
b2.pack(side=LEFT, padx = 20)

root.mainloop()