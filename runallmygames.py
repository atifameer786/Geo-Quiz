from tkinter.ttk import Style
import runallmygames
import os
from tkinter import *
from tkinter import ttk
def runagain():


    window = Tk()
    window.title("GAME ARENA")
    # window.minsize(width=1600, height=900)
    window.geometry('1430x900')
    my_lable = Label(text="Game Arena", font=("", 144), fg='grey')
    my_lable.config(bg='#2c2929', border=0)
    my_lable.pack()
    import sys

    sys.path.append("/Users/atif/Downloads/Solution+-+snake-game-high-score-final")
    sys.path.append("Users/atif/Downloads/pong_game")
    sys.path.append("Users/atif/Downloads/Indian_states_quiz")
    sys.path.append("/Users/atif/Downloads/us-states-game-end")
    sys.path.append("/Users/atif/Downloads/Solution+-+turtle-crossing-final")
    import run as r
    import run_pong as rp
    import run_indian_quiz as riq
    import run_usa as ru
    import run_turtle_crosing as rtc

    def forsnake():
        r.runmygame()

    def forpong():
        rp.runponggame()


    def forindian():
        riq.runindianquiz()

    def forusa():
        ru.runusagame()

    def forturtle():
        rtc.runturtlecrosing()
        refresh()



    def refresh():
        os.execl(sys.executable, sys.executable, *sys.argv)
        runagain()




    constX = 560
    diffY = 40
    primaryColor = "white"


    btn1 = Button(window, text='Snake', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                 highlightbackground=primaryColor , command=forsnake)
    btn2 = Button(window, text='Pong', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                  highlightbackground=primaryColor, command=forpong)
    btn3 = Button(window, text='IND State Quiz', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                  highlightbackground=primaryColor, command=forindian)
    btn4 = Button(window, text='Turtle Crossing', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                  highlightbackground=primaryColor,command=forturtle)
    btn5 = Button(window, text='USA State Quiz', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                  highlightbackground=primaryColor,command=forusa)
    btn6 = Button(window, text='Refresh', height=2, width=25, font=('arial', 25, 'bold'), fg="grey",
                  highlightbackground=primaryColor,command=refresh)

    btn1.place(x=constX, y=250)
    btn2.place(x=constX, y=350)
    btn3.place(x=constX, y=450)
    btn4.place(x=constX, y=550)
    btn5.place(x=constX, y=650)
    btn6.place(x=constX, y=750)

    window.config(bg='#2c2929')

    window.mainloop()

if __name__=="__main__":
    runagain()