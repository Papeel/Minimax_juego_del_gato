import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter.tix import Select


def isFinal(state):
    if((state[0][0]==-1 or state[0][0]==1)and state[0][0]==state[1][1] and state[1][1]==state[2][2]):return True
    if ((state[2][0]==-1 or state[2][0]==1)and state[2][ 0] == state[1][ 1] and state[1][ 1] == state[0][2]): return True

    for row in state:
        if( (row[0]==-1 or row[0]==1)and row[0]==row[1]and row[1]==row[2]): return True

    for i in range(3):

        if( (state[0][i]==-1 or state[0][i]==1)and state[0][i]==state[1][i]and state[1][i]==state[2][i]): return True

    for row in state:
        for n in row:

            if(n==0):return False

    return True



def valida(state):
    if((state[0][0]==-1 or state[0][0]==1)and state[0][0]==state[1][1] and state[1][1]==state[2][2]):
        if(state[0][0]==-1):return 1
        return -1
    if ( (state[2][0]==-1 or state[2][0]==1)and state[2][0] == state[1][ 1] and state[1][ 1] == state[0][2]):
        if(state[2][0]==-1):return 1
        return -1
    for row in state:
        if((row[0]==-1 or row[0]==1)and row[0]==row[1]and row[1]==row[2]):
            if(row[0]==-1):return 1
            return -1
    for i in range(3):
        if( (state[0][i]==-1 or state[0][i]==1)and state[0][i]==state[1][i]and state[1][i]==state[2][i]):
            if (state[0][ i] == -1): return 1
            return -1


    return 0



def minimax( n , state,actionn):
    num=1
    vp=0
    1
    if (isFinal(state)): return [valida(state),""]
    for key, value in actionn.items():



        new_state=copy(state)
        new_state[value[0]][value[1]]=n
        actionnn=dict(actionn)
        del actionnn[key]
        vn=minimax(n*-1,new_state, actionnn)
        if(num==1):

            vp=[vn[0],key]
            num=0
        else:
            if(n==-1):
                if(vp[0]<vn[0]):

                    vp = [vn[0], key]

            else:
                if (vp[0] > vn[0]):

                    vp = [vn[0], key]

    return vp

def copy(old_list):
    new_list=[]
    for v in old_list:
        new_list.append(v[:])


    return new_list



class tabla:

    def __init__(self,state,actions):
        self.state=state
        self.actions=actions

        self.ventana=tk.Tk()


        #self.ventana.geometry('300x200')
        #ttk.Button(ca, text='Salir', command=(lambda x:co())).pack()
        self.listaBotones=[]
        boton1 = Button(self.ventana, text="H",command=lambda :self.cambia(0))
        boton2 = Button(self.ventana, text="H",command=lambda :self.cambia(1))
        boton3 = Button(self.ventana, text="H",command=lambda :self.cambia(2))
        boton4 = Button(self.ventana, text="H",command=lambda :self.cambia(3))
        boton5 = Button(self.ventana, text="H",command=lambda :self.cambia(4))
        boton6 = Button(self.ventana, text="H",command=lambda :self.cambia(5))
        boton7 = Button(self.ventana, text="H",command=lambda :self.cambia(6))
        boton8 = Button(self.ventana, text="H",command=lambda :self.cambia(7))
        boton9 = Button(self.ventana, text="H",command=lambda :self.cambia(8))
        boton1.grid(row=3, column=3)
        boton2.grid(row=3, column=2)
        boton3.grid(row=3, column=1)
        boton4.grid(row=2, column=3)
        boton5.grid(row=2, column=2)
        boton6.grid(row=2, column=1)
        boton7.grid(row=1, column=3)
        boton8.grid(row=1, column=2)
        boton9.grid(row=1, column=1)
        self.listaBotones.append(boton1)
        self.listaBotones.append(boton2)
        self.listaBotones.append(boton3)
        self.listaBotones.append(boton4)
        self.listaBotones.append(boton5)
        self.listaBotones.append(boton6)
        self.listaBotones.append(boton7)
        self.listaBotones.append(boton8)
        self.listaBotones.append(boton9)


        self.ventana.mainloop()

    def cambia(self,num):
        if(not str(num+1) in self.actions):return
        self.listaBotones[num].config(text="X")
        act = self.actions[str(num+1)]
        self.state[act[0]][act[1]] = 1
        del self.actions[str(num+1)]
        if (isFinal(self.state)):
            if (valida(self.state) == 0):
                label=Label(self.ventana,text="Empate")
                label.grid(row=5,column=6)
                return ;
            else:
                label = Label(self.ventana, text="Ganaste")
                label.grid(row=5, column=6)
                return;

        valu = minimax(-1, copy(self.state), dict(self.actions))[1]
        self.listaBotones[int(valu)-1].config(text="O")
        act = self.actions[valu]
        self.state[act[0]][act[1]] = -1
        del self.actions[valu]
        if (isFinal(self.state)):
            if (valida(self.state) == 0):
                label = Label(self.ventana, text="Empate")
                label.grid(row=5, column=6)


            else:
                label = Label(self.ventana, text="Perdiste")
                label.grid(row=5, column=6)



tablero=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
 ]
actions ={
    "1": [2, 0],
    "2": [2, 1],
    "3": [2, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [0, 0],
    "8": [0, 1],
    "9": [0, 2],
}

tabla(tablero, actions)


