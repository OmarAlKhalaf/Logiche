from os.path import exists
import tkinter as tk
window = tk.Tk()
window.geometry('500x400')
window.title('On/Off')


start = 0
def func():
    global start
    if start == 0:
        print('On')
        window.config(bg='red')
        start +=1 
    elif start == 1:
        print('Off')
        window.config(bg='blue')
        start -=1

window.config(bg='white')
button = tk.Button(window, text='Start', bg='white', command=func)
button.pack(pady = 20, padx = 20 )




window.mainloop()