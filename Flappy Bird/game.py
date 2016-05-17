# -*- coding: cp936 -*-
from Tkinter import *
from random import *
from time import *
from birdandpipe import Birdandpipe
from tkFont import *


def game():
    def callback_exit(event):
        root.destroy()

    def callback_about(event):
        root2 = Tk()
        root2.title('About')
        c2 = Canvas(root2, width=200, height=10)
        Label(root2,text='Flappy Bird by').pack()
        Label(root2,text='Jijun Xiao').pack()
        c2.pack()

    def callback_birdFlap(event):
        bap.updateSpeed()

    def callback_start(event):
        c.delete(pic1)
        c.delete(pic3)
        t = 0
        flag = True
        while flag:
            t += 0.005
            time = c.create_text(148, 10, text = "Score: %d"%(bap.score))
            if bap.getSpeed() < 0:
                c.move(bir, 0, bap.updatebird(-18, 7, 3))
                c.update()
            else:
                c.move(bir, 0, bap.updatebird(0, 8.5, 2))
                c.update()
            bap.updatepipe()
            for i in range(100):
                c.move(allpipe[i][0], -1, 0)
                c.move(allpipe[i][1], -1, 0)
                c.move(allpipe[i][2], -1, 0)
                c.move(allpipe[i][3], -1, 0)
                c.update()
            flag = bap.flag1()
            sleep(0.005)
            c.delete(time)
            c.bind("<ButtonPress-1>", callback_birdFlap)

        c.create_text(100, 85, text = "Score: %d"%(bap.score))
        p2 = PhotoImage(file = "C:\Flappy Bird Picture\over.gif")
        pic2 = c.create_image(100, 50, image = p2)
        c.bind("<ButtonPress-1>", callback_restart)
        p4 = PhotoImage(file = "C:\Flappy Bird Picture\click.gif")
        pic4 = c.create_image(100, 150, image = p4)

        if bap.bypos < 300:
            c.delete(bir)
        while bap.bypos < 300:
            if bap.getSpeed() < 0:
                bap.updatebird(-18, 7, 3)
            else:
                bap.updatebird(0, 8.5, 2)
            c.update()
            kot = PhotoImage(file="C:\Flappy Bird Picture\kotori.gif")
            c.create_image(50, bap.bypos - 10, image=kot)
            sleep(0.005)
        root.mainloop()

    root = Tkinter.Tk()  #original: = Tk()
    root.title('Flappy Bird')
    c = Canvas(root, width=200, height=300, bg='white')
    bkg = PhotoImage(file = "C:\Flappy Bird Picture\day.gif")
    c.create_image(100, 150, image = bkg)
    c.pack()
    m = Menu(root)
    root.config(menu = m)

    filemenu = Menu(m)
    m.add_cascade(label = "File", menu = filemenu)
    filemenu.add_command(label = "Exit", command = callback_exit)
    helpmenu = Menu(m)
    m.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "About",command = callback_about)

    kot = PhotoImage(file = "C:\Flappy Bird Picture\kotori.gif")
    bir = c.create_image(50, 140, image = kot)

    bap = Birdandpipe()
    bap.initlisth()
    bap.initlistx()
    allpipe = []
    for i in range(100):
        x0, y0, x1, y1 = bap.pgetXlist(i), 0, bap.pgetXlist(i) + 25, bap.pgetHlist(i) - 15
        x0s, y0s, x1s, y1s = bap.pgetXlist(i) - 5, bap.pgetHlist(i) - 15, bap.pgetXlist(i) + 30, bap.pgetHlist(i)
        x2, y2, x3, y3 = bap.pgetXlist(i), y1 + 85, bap.pgetXlist(i) + 25, 400
        x2s, y2s, x3s, y3s = bap.pgetXlist(i) - 5, y1 + 70, bap.pgetXlist(i) + 30, y1 + 85
        brick1 = c.create_rectangle(x0, y0, x1, y1, fill='ForestGreen')
        brick1s = c.create_rectangle(x0s, y0s, x1s, y1s, fill='ForestGreen')
        brick2 = c.create_rectangle(x2, y2, x3, y3, fill='ForestGreen')
        brick2s = c.create_rectangle(x2s, y2s, x3s, y3s, fill='ForestGreen')
        allpipe += [(brick1, brick2, brick1s, brick2s)]

    p1 = PhotoImage(file = "C:\Flappy Bird Picture\go.gif")
    pic1 = c.create_image(100,50,image = p1)
    p3 = PhotoImage(file = "C:\Flappy Bird Picture\click.gif")
    pic3 = c.create_image(100,150,image = p3)
    c.bind("<ButtonPress-1>", callback_start)

    def callback_restart(event):
        c.destroy()
        root.destroy()
        game()
    root.mainloop()
 
game()
