from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Easy Ticket")
root.geometry("500x700")

#Creating variables
variables=["Soccer","Movie","Theater"]

sctcket= 40
mvietcket= 75
thtretkt= 100

tkvar = StringVar()



label1 = Label(root, text="Enter Your Cell Number")
label1.pack()
label1.place(x = 30, y = 200)

cellno=Entry(root, textvariable="")
cellno.pack()
cellno.place(x = 250, y = 200)

label2=Label(root, text="Select Category")
label2.pack()
label2.place(x = 30, y = 300)

cat = ttk.Combobox(root, textvariable=tkvar, value=variables)
cat.pack()
cat.place(x = 250, y = 300)
cat.config(width=20)

label3=Label(root, text="Number Of Tickets")
label3.pack()
label3.place(x = 30, y = 400)

nrtickets= Spinbox(root, from_=0, to=20, state="readonly")
nrtickets.pack()
nrtickets.place(x = 250, y = 400)

ans1=Label(root,)
ans1.pack()
ans1.place(x = 180, y = 550)

class clsTicketSales:


    def __init__(self, cellno, nrtickets,tprice):
        self.cellno=cellno
        self.nrtickets=nrtickets
        self.tprice=tprice
        return



def calc():

    tcketsale= clsTicketSales(cellno.get(),float(nrtickets.get()), cat.get())

    if cat.get() == "Soccer": 
        scprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Cell Number: " + str(cellno.get() + "\n" + "No. Of Tickets: " + str(nrtickets.get()) + "\n" + "Price: " +  "R" + str(scprice)))

    if cat.get() == "Movie":
        mvprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Cell Number: " + str(cellno.get() + "\n" + "No. Of Tickets: " + str(nrtickets.get()) + "\n" + "Price: " + "R" + str(mvprice)))

    if cat.get() == "Theater":
        thtrprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Cell Number: " + str(cellno.get() + "\n" + "No. Of Tickets: " + str(nrtickets.get()) + "\n" + "Price: " + "R" + str(thtrprice) ))

def clear():
    cellno.delete(0,END)
    cat.delete(0,END)

def exit():
    root.destroy()


calbtn= Button(root, text="Calculate", command=calc)
calbtn.pack()
calbtn.place(x = 30, y = 500)

calbtn= Button(root, text="CLear", command=clear)
calbtn.pack()
calbtn.place(x = 300, y = 500)

calbtn= Button(root, text="Exit Program", command=exit)
calbtn.pack()
calbtn.place(x = 35, y = 650)

root.mainloop()
