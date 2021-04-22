import webbrowser
from tkinter import *

#Quando se usa somente com espaço, representa que não há um nome para a tela
root = Tk( )

root.title('Abrir o browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com.br')

mygoogle = Button(root, text='Abrir o google', command=google).pack(pady=20)
root.mainloop()