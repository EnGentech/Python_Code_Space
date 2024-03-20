from tkinter import *
from random import randint
from time import sleep

win = Tk()

win.geometry("500x500")
win.title("Devils Basket game")

content = ['5 frog jumps', 'scratch my back for 2 minutes', 'twerk for me',
           'play with ur Gbola or pussy for 3mins', 'Kneel and tell me I LOVE YOU', 'Make me tea',
           'Suck my pussy or suck my Gbola for 2 minutes', 'suck my breast for 2 minutes',
           'profess love for me for 2 minutes', 'Suck and play with my lips for 2 minutes',
           'In 3 minutes, tie yourself gele', 'Tell me the best part of me', 'Touch the part you love most in me',
           'In 3 minutes, fuck me in doggy style', 'In 3 minutes, massage me', 'Ping my back for 3 minutes',
           'Give me a donkey ride for 3 minutes', 'Romance me in 3 minutes', 'In 3 minutes, give me missionary fuck',
           'Kiss my feet', 'Micmick me in 3 minutes', 'You lost', 'You chance is lost', 'Sorry, you lost it',
           'You lost', 'You chance is lost', 'Sorry, you lost it', 'You lost', 'You chance is lost',
           'Sorry, you lost it', 'You lost', 'You chance is lost', 'Sorry, you lost it']

def dvBk():
    ran = randint(0, len(content))
    for i in range(len(content)):
        if i == ran:
            processing()
            e.delete(0, END)
            e.insert(0, content[i])
            content.pop(i)
            break


def processing():
    """process before action"""
    write = "=== Processing ==="
    lbl_processing = Label(win, text=write)
    lbl_processing.place(x=160, y=160)
    for i in range(5, 0, -1):
        lbl_count = Label(win, text=i)
        lbl_count.place(x=180, y=190)

e = Entry(win, font=("arial", 16, "bold"), width=38)
e.place(x=20, y=70)
btn1 = Button(win, bg="pink", command=dvBk, fg='#480607', padx=50,
              text="Toss_Game", font=("arial", 16, "bold"))
btn1.place(x='135', y='320')

lbl = Label(win, fg='#708090', text="A game for\nCouples", font=("arial", 14, "italic"))
lbl.pack()

lbl_instruct = Label(win, text="Instruction: ", font=('arial', 12, 'bold'), fg='brown')
lbl_up = Label(win, text="You must do what ever you pick or loose 2 chances")
lbl_instruct.place(x=60, y=120)
lbl_up.place(x=155, y=122)



win.mainloop()