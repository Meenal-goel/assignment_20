#1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *
root = Tk()
root.title("GUI DICT")
root.geometry('100x100')
mylist=[]
mydict = {'meenal':3597458214,'riya':6589741256,'anshul':1258749611,'gauri':1458752369,'rohit':1452,'shilpam':1254,'edward':254123,'gaurav':1458752369,'chetana':1452,'satvik':1254,'adam':254123}
for k,v in mydict.items():
    mylist.append(k)

sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)


mylist1 = Listbox(root,yscrollcommand = sb.set)
for ele in range(len(mylist)):
    mylist1.insert(END,str(mylist[ele]))
    
mylist1.pack(side = LEFT , fill =Y)
sb.configure(command = mylist1.yview)

root.mainloop()

#2.In the same tkinter file as created above, create a function to insert items into the dictionary.

from tkinter import *
root = Tk()
root.title("GUI DICT")
root.geometry('500x300')

def fun():
    k = e1.get()
    v = e2.get()
    mydict[k] = v
    kL.configure(text = k)
    vL.configure(text = v)
    
mydict = {}

lbL1 = Label(root, text = 'NAME')
lbL1.grid(row = 0,column = 0)
lbL2 = Label(root,text = 'MOBILE NO.')
lbL2.grid(row =1,column =0)

e1 = Entry(root)
e1.grid(row =0,column =1)
e2 = Entry(root)
e2.grid(row =1,column = 1)

addB =Button(root, text = 'ADD IT',command =fun)
addB.grid(row =2,column=1)

kL = Label(root)
kL.grid(row =3,column =0)

vL = Label(root)
vL.grid(row = 3,column =1)

def scroll():
    mylist =[]
    root = Tk()
    for k,v in mydict.items():
        mylist.append(k)

    sb = Scrollbar(root)
    sb.pack(side = RIGHT, fill = Y)


    mylist1 = Listbox(root,yscrollcommand = sb.set)
    for ele in range(len(mylist)):
        mylist1.insert(END,str(mylist[ele]))
    
    mylist1.pack(side = LEFT , fill =Y)
    sb.configure(command = mylist1.yview)

aB =Button(root, text = 'SCROLL KEY',command =scroll)
aB.grid(row =2,column=2)


root.mainloop()
