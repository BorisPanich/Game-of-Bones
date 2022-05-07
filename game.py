from tkinter import *
import random, time


def receivingResult():
    return random.choice([
        '1.png',
        '2.png',
        '3.png',
        '4.png',
        '5.png',
        '6.png',
    ])


def throwBones(event):
    global point1, point2

    for i in range(5):
        throw1 = PhotoImage(file=(receivingResult()))
        throw2 = PhotoImage(file=(receivingResult()))
        point1['image'] = throw1
        point2['image'] = throw2
        root.update()
        time.sleep(0.2)


root = Tk()
root.geometry('750x500')
root.title("Game of bones")
# root.resizable(height=False, width=False)  # чтобы не расстягивалось окно

root.iconphoto(
    True, PhotoImage(file=('icon.png')))  # added icon of application window

font = PhotoImage(file=('fon_nebo.gif'))
Label(root, image=font).pack()  # added font for place of game

# установка меток для нахождения костей:
point1 = Label(root)
point1.place(relx=0.3, rely=0.5, anchor=CENTER)
point2 = Label(root)
point2.place(relx=0.7, rely=0.5, anchor=CENTER)

# buttom for push
root.bind('<1>', throwBones)

# для запуска многократного перебора костей
# throwBones('event')

root.mainloop()