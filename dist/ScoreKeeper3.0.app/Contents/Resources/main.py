from tkinter import *

class controls:
    score=1
    def __init__(self,main):
        self.main=main
        self.n=Button(main,text="add", command=self.k)
        self.m=Entry(main)
        self.n.grid(column=0,row=0)
        self.m.grid(column=1,row=0,columnspan=3)
    def k(self):
        m=player(self.main,self.m.get() ,self.score)
        self.score+=1

class player:
    def __init__(self, main, name, row=0, col=0):
        self.name=Label(main,text=name)
        self.score=0
        self.scoretext=Label(main,text="Score: "+str(self.score))
        self.buttonX=Button(main, text="X", command= self.kill)
        self.button1=Button(main, text="+1", command=lambda: self.scoreChange(1))
        self.button2=Button(main, text="+2", command=lambda: self.scoreChange(2))
        self.button0=Button(main, text="-1", command=lambda: self.scoreChange(-1))
        self.buttonC=Button(main, text="Clear", command= self.clr)

        self.buttonX.grid(row=row,column=col)
        col+=1
        self.button0.grid(row=row,column=col)
        col+=1
        self.name.grid(row=row,column=col)
        col+=1
        self.scoretext.grid(row=row,column=col)
        col+=1
        self.buttonC.grid(row=row,column=col)
        col+=1
        self.button1.grid(row=row,column=col)
        col+=1
        self.button2.grid(row=row,column=col)

    def scoreChange(self,x):
        self.score+=x
        self.scoretext.config(text="Score: "+str(self.score))

    def kill(self):
        self.buttonX.destroy()
        self.button0.destroy()
        self.name.destroy()
        self.scoretext.destroy()
        self.buttonC.destroy()
        self.button1.destroy()
        self.button2.destroy()

    def clr(self):
        self.score=0
        self.scoretext.config(text="Score: "+str(self.score))

main = Tk()
main.title("Scorekeeper3.0")
main.resizable(False,False)
controls(main)
main.mainloop()