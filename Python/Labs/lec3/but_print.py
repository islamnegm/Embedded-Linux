from tkinter import *
def ButtonPressed():
   ButtonPressed.counter+=1
   print("islam negm  = ",ButtonPressed.counter) 
ButtonPressed.counter = 0 

window_1 = Tk()
window_1.title("Hello ")
lable1=Label(window_1,text="label1")
lable1.pack(side=TOP)
window_1.geometry('1000x500')
b1=Button(window_1,text="negm",bd='5',command=ButtonPressed)
b2 = Button(window_1,text="islam",bd='5',command=window_1.destroy)
b3=  Button(window_1,text="hello")
b4=  Button(window_1,text="nem")

b1.pack(side=TOP)
b2.pack(side=RIGHT)
b3.pack(side=LEFT)
b4.pack(side=BOTTOM)
lable1.pack(side=BOTTOM)
window_1.mainloop()