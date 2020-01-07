import tkinter as tk
from controller import SelectController

list = []

def arrAppend():
    global list
    list.append(entry.get())
    tempStr = ""
    for i in list:
        tempStr+= i+"\n"
    label['text']=tempStr
    entry.delete(0,tk.END)

def choiceMenu():
    global list
    T = SelectController()
    result = T.choiceMenu(list)
    resultLb['text'] = result

window = tk.Tk()
window.title('lunch_picker')
window.geometry('300x250')
window.resizable(False,False)
entry = tk.Entry(window)
entry.pack()
inputBtn = tk.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="넣기", command=arrAppend)
inputBtn.pack()
label=tk.Label(window, text="", width=10, height=10)
label.pack()
outputBtn = tk.Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="뽑기",command=choiceMenu)
outputBtn.pack()
resultLb=tk.Label(window, text="", width=10, height=10)
resultLb.pack()
window.mainloop()
