import sqlite3
import tkinter
import time
import random
from tkinter import ttk


db = sqlite3.connect("dorogi.db")
cur = db.cursor()

a = cur.execute("SELECT * FROM dorogi")

dorogi = a.fetchall()

print(dorogi)

root = tkinter.Tk(className="Road and ball")
root.config(width=600, height=700)

canva = tkinter.Canvas(root, width=600, height=700, background="green")

a = cur.execute("SELECT * FROM road_controll")
road_controll = a.fetchall()
print(road_controll)
canva.create_rectangle(road_controll[0][1] + 25, road_controll[0][2] + 25, road_controll[0][1] - 25, road_controll[0][2] - 25, fill="lightgreen")

a = cur.execute("SELECT * FROM peshehod")
peshehod = a.fetchall()

canva.create_oval(peshehod[0][1] - 25, peshehod[0][2] - 25, peshehod[0][1] + 25, peshehod[0][2] + 25, fill = "white")
canva.create_line(dorogi[0][1], dorogi[0][2], dorogi[0][3], dorogi[0][4], width = 10)
canva.create_line(dorogi[1][1], dorogi[1][2], dorogi[1][3], dorogi[1][4], width = 10)
canva.create_line(dorogi[2][1], dorogi[2][2], dorogi[2][3], dorogi[2][4], width = 10)
rand = random.randint(0, 1)
canva.pack()

cnopka = ttk.Button(text="Переключение режима")
cnopka.pack()

start_stop = ttk.Button(text="Старт и стоп обучения")
start_stop.pack()

def move(dorogi):
    roads = dorogi
    start_p = random.choice(roads)
    kx, ky = 0, 0

    if start_p == roads[2] and rand == 1:
        car = canva.create_oval(start_p[3] - 25, start_p[4] - 25, start_p[3] + 25, start_p[4] + 25, fill = "red")
    else:
        car = canva.create_oval(start_p[1] - 25, start_p[2] - 25, start_p[1] + 25, start_p[2] + 25, fill = "red")

    end = 0
    cross = 0
    cross_go = random.randint(0, 1)
    up = 0

    while end != 1:
        cords = canva.coords(car)

        if cords[0] + 25 == 300 and -1 < cords[1] + 25 < 500 and up == 0:
            kx, ky = 0, 1
        elif cords[0] + 25 == 400 and -1 < cords[1] + 25 < 500 and up == 0:
            kx, ky = 0, 1

        elif cords[1] + 25 == 500 and -1 < cords[0] + 25 < 600 and rand == 0:
            if cords[0] + 25 == 300 and -1 < cords[1] + 25 < 501 and cross_go == 1:
                kx, ky = 0, -1
                up = 1
            elif cords[0] + 25 == 400 and -1 < cords[1] + 25 < 500 and cross_go == 1:
                kx, ky = 0, -1
                up = 1
            else:
                kx, ky = 1, 0
        elif cords[1] + 25 == 500 and -1 < cords[0] + 25 < 601 and rand == 1:
            if cords[0] + 25 == 300 and -1 < cords[1] + 25 < 501 and cross_go == 1:
                kx, ky = 0, -1
                up = 1
            elif cords[0] + 25 == 400 and -1 < cords[1] + 25 < 500 and cross_go == 1:
                kx, ky = 0, -1
                up = 1
            else:
                kx, ky = -1, 0

        if cords[0] + 25 == 300 and cords[1] + 25 == 500:
            cross = 1
        if cords[0] + 25 == 400 and cords[1] + 25 == 500:
            cross = 1

        print(kx, ky)
        canva.move(car, kx, ky)
        canva.update()
        time.sleep(0.01)
        print(cords)

        if cross == 1 and cords[0] + 25 == 300 and cords[1] + 25 == 0:
            end = 1
        elif cross == 1 and cords[0] + 25 == 400 and cords[1] + 25 == 0:
            end = 1
        elif cross == 1 and cords[0] + 25 == 0 and cords[1] + 25 == 500:
            end = 1
        elif cross == 1 and cords[0] + 25 == 600 and cords[1] + 25 == 500:
            end = 1
        print(cross_go)


move(dorogi)

root.mainloop()