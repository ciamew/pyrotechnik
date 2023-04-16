# V programe je definovaný zoznam použitých farieb, počiatočné súradnice umiestnenia káblikov a ich dĺžka (všetky kábliky sú umiestnené vodorovne pod sebou, ich hrúbka je nemenná s veľkosťou 10 px).
# Program vykreslí kábliky podľa nastavených údajov, napíše nadpis (viď ukážku), náhodne si určí správny káblik a spustí odpočítavanie času, ktoré sa zobrazuje na obrazovke.
# Hráč ovláda hru kliknutím na káblik. Ak klikne na správny káblik, čas sa zastaví a vypíše sa informácia o výhre (viď ukážku).
# Ak nestihne v časovom intervale kliknúť na správny káblik, z grafickej plochy všetko zmizne a program už nič nerobí.

import tkinter as tk
import random
win = tk.Tk()
canvas = tk.Canvas(win, height = 500, width = 600, bg = 'white')
canvas.pack()

canvas.create_text(250,25, text="Pyrotechnik", fill="blue", font="Arial 20")
canvas.create_text(250,50, text="označ správny káblik", fill="black", font="Arial 12")

colors = ["red", "yellow", "green", "blue", "purple"]
width = 300
height = 15

ux = 100
uy = 100
wires = []
explosion = 0
ftime = 50
status = True


def DrawWires():
    global wires, explosion
    for i in range(5): #len(colors)
        wires.append(canvas.create_rectangle(ux, uy+height*i, ux+width, uy+height*(i+1), fill=colors[i]))
    explosion = random.choice(wires)

def clicker(e):
    global x,y
    global status
    if ux < e.x < ux + width and uy < e.y < uy+height*5 and ftime > 0:
        colors = canvas.find_overlapping(e.x, e.y, e.x, e.y)[0]
        if colors == explosion:
            status = False
            canvas.create_text(250, 250, text="Vyhral si!", fill="black", font="Arial 25")

def changer():
    global ftime,x,y
    ftime -= 1
    canvas.itemconfig(time, text=ftime)
    if ftime > 0 and status:
        canvas.after(100, changer)
    elif status or ftime == 0: #dorobene or a text
        canvas.delete("all")
        canvas.create_text(300, 250, text="Prehral si!", fill="red", font="Arial 55")


time = canvas.create_text(475,140,text=ftime, fill="red", font="Arial 35")
canvas.bind("<Button-1>", clicker)
DrawWires()
changer()
win.mainloop()