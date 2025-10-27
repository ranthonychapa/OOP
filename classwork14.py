#import matplotlib.pyplot as plt
#import numpy as np

#x = np.array(['c1', 'c2','c3','c4'])
#y = np.array([80,100,62,76])

#print(np.mean(y))
#print(np.median(y))
#print(np.std(y))

#plt.xlabel('courses')
#plt.ylabel('grades')

#plt.plot(x,y)
#plt.show()

#mylabels = ['a1','a2','a3','a4']
#plt.pie(y, labels = mylabels)
#plt.show()

#x = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
#y = [21,19,24,17,16,25,24,22,21,21]
#plt.scatter(x,y)
#plt.show()

import tkinter

root = tkinter.Tk()
root.resizable(False,False)
myCanvas = tkinter.Canvas(root, bg='white', height=500, width=800)
shape1 = myCanvas.create_oval(150,150,100,100, fill='blue')
#shape2 = myCanvas.create_rectangle(10,10,75,75, fill='red')

#myCanvas.pack()
#root.mainloop()
def move_shape():
    global xx, yy

    myCanvas.move(shape1, xx, yy)
    