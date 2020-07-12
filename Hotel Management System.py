from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time
import random
from datetime import datetime, timedelta
import hoteldatabase
import sqlite3

con = sqlite3.connect('booking.db')
cur = con.cursor()
con.commit()

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1200x700')

        MainFrame = Frame(self.root)
        MainFrame.grid()
        TopFrame = Frame(MainFrame, bd=10, width=1000, height=550, relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, padx=2, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=5, width=800, height=600, relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=760, height=50, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=760, height=500, padx=3, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)  
        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=600, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3, column=0)

        BottomFrame = Frame(MainFrame, bd=10, width=1200, height=150, padx=4, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)

        global hd
        CustID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address = StringVar()
        DOB = StringVar()
        PostalCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        Gender = StringVar()
        CheckIn = StringVar()
        CheckOut = StringVar()
        TypeOfId = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExt = StringVar()
        NoOfDays = StringVar()
        Paidtax = StringVar()
        Subtotal = StringVar()
        TotalCost = StringVar()

        CheckIn.set(time.strftime("%d/%m/%Y"))
        CheckOut.set(time.strftime("%d/%m/%Y"))

        x = random.randint(1190, 8746)
        randomRef = str(x)
        CustID.set('Hotel'+randomRef)
        def iExit():
            iExit = tkinter.messagebox.askyesno('Hotel Management System', 'Do you want to exit?')
            if iExit > 0:
                root.destroy()
            return

        def Reset():
            Meal.set('')
            RoomType.set('')
            RoomNo.set('')
            RoomExt.set('')
            TotalCost.set('')
            TypeOfId.set('')
            NoOfDays.set('')
            
            self.txtFirstName.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtPostalCode.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtNationality.delete(0, END)
            self.txtGender.delete(0, END)            
            self.txtPaidtax.delete(0, END)
            self.txtSubtotal.delete(0, END)
            self.txtTotalCost.delete(0, END)

            CheckIn.set(time.strftime("%d/%m/%Y"))
            CheckOut.set(time.strftime("%d/%m/%Y"))

            x = random.randint(1190, 8746)
            randomRef = str(x)
            CustID.set('Hotel'+randomRef)

        def addHotel():
            hoteldatabase.addHotelRec(CustID.get(), FirstName.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(), TypeOfId.get(), CheckIn.get(), CheckOut.get())
            lsthotel.delete(0, END)
            lsthotel.insert(END, (CustID.get(), FirstName.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(), TypeOfId.get(), CheckIn.get(), CheckOut.get()))
            
        def showData():
            lsthotel.delete(0, END)
            for row in hoteldatabase.displayHotelRec():
                lsthotel.insert(END, row, str(''))

        def HotelRecord():
            global hd
            searchHdb = lsthotel.curselection()[0]
            hd = lsthotel.get(searchHdb)
            print(hd)

            self.txtCustID.delete(0, END)
            self.txtCustID.insert(END, hd[1])
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(END, hd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, hd[3])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, hd[4])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, hd[5])
            self.txtNationality.delete(0, END)
            self.txtNationality.insert(END, hd[7])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, hd[8])
            self.txtCheckIn.delete(0, END)
            self.txtCheckIn.insert(END, hd[9])
            self.txtCheckOut.delete(0, END)
            self.txtCheckOut.insert(END, hd[10])

            
            
        def deleteData():
            hd = 0
            if len(CustID.get()) != 0:
                hoteldatabase.deleteHotelRec(hd[0])
                Reset()
                showData()

        def searchDatabase():
            lsthotel.delete(0, END)
            if row in hoteldatabase.searchHotelRec(CustID.get(), FirstName.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(),
                                                   Nationality.get(), TypeOfId.get(), CheckIn.get(), CheckOut.get()):
                lst.insert(END, row, str(''))

        def update():
            hd = 0
            if len(CustID.get()) != 0:
                hoteldatabase.deleteHotelRec(hd[0])
            if len(CustID.get()) != 0:
                hoteldatabase.addHotelRec(CustID.get(), FirstName.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(), TypeOfId.get(), CheckIn.get(), CheckOut.get())
                lsthotel.delete(0, END)
                lsthotel.insert(END, (CustID.get(), FirstName.get(), Surname.get(), Address.get(), Gender.get(), Mobile.get(), Nationality.get(), TypeOfId.get(), CheckIn.get(), CheckOut.get()))

        def TotalAndAddData():
            addHotel()
            InDate = CheckIn.get()
            OutDate = CheckOut.get()
            InDate = datetime.strptime(InDate, '%d/%m/%Y')
            OutDate = datetime.strptime(OutDate, '%d/%m/%Y')
            NoOfDays.set(abs((OutDate - InDate).days))

            if Meal.get() == 'Breakfast' and RoomType.get() == 'Single':
                q1 = float(17)
                q2 = float(34)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Breakfast' and RoomType.get() == 'Double':
                q1 = float(34)
                q2 = float(50)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Breakfast' and RoomType.get() == 'Family':
                q1 = float(51)
                q2 = float(66)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Lunch' and RoomType.get() == 'Single':
                q1 = float(20)
                q2 = float(40)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Lunch' and RoomType.get() == 'Double':
                q1 = float(40)
                q2 = float(80)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Lunch' and RoomType.get() == 'Family':
                q1 = float(60)
                q2 = float(120)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Dinner' and RoomType.get() == 'Single':
                q1 = float(25)
                q2 = float(50)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Dinner' and RoomType.get() == 'Double':
                q1 = float(35)
                q2 = float(70)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
            elif Meal.get() == 'Dinner' and RoomType.get() == 'Family':
                q1 = float(40)
                q2 = float(90)
                q3 = float(NoOfDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'Rs.'+str('%.2f'%((q5)*0.09))
                ST = 'Rs.'+str('%.2f'%((q5)))
                TT = 'Rs.'+str('%.2f'%(q5 + ((q5)*0.09)))
                Paidtax.set(Tax)
                Subtotal.set(ST)
                TotalCost.set(TT)
                    
#------------------------------------Widget------------------------------------------------------

        self.lblCustID = Label(LeftFrame, text='Customer ref: ', font=('arial 10 bold'), padx=1)
        self.lblCustID.grid(row=0, column=0, sticky=W)
        self.txtCustID = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=CustID)
        self.txtCustID.grid(row=0, column=1, pady=3, padx=30)

        self.lblFirstName = Label(LeftFrame, text='First Name: ', font=('arial 10 bold'), padx=1)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=FirstName)
        self.txtFirstName.grid(row=1, column=1, pady=3, padx=30)

        self.lblSurname = Label(LeftFrame, text='Surname: ', font=('arial 10 bold'), padx=1)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Surname)
        self.txtSurname.grid(row=2, column=1, pady=3, padx=30)

        self.lblAddress = Label(LeftFrame, text='Address: ', font=('arial 10 bold'), padx=1)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Address)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=30)

        self.lblDOB = Label(LeftFrame, text='DOB: ', font=('arial 10 bold'), padx=1)
        self.lblDOB.grid(row=4, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=DOB)
        self.txtDOB.grid(row=4, column=1, pady=3, padx=30)

        self.lblPostalCode = Label(LeftFrame, text='Postal Code: ', font=('arial 10 bold'), padx=1)
        self.lblPostalCode.grid(row=5, column=0, sticky=W)
        self.txtPostalCode = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=PostalCode)
        self.txtPostalCode.grid(row=5, column=1, pady=3, padx=30)

        self.lblMobile = Label(LeftFrame, text='Mobile: ', font=('arial 10 bold'), padx=1)
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Mobile)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=30)

        self.lblEmail = Label(LeftFrame, text='Email: ', font=('arial 10 bold'), padx=1)
        self.lblEmail.grid(row=7, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Email)
        self.txtEmail.grid(row=7, column=1, pady=3, padx=30)

        self.lblNationality = Label(LeftFrame, text='Nationality: ', font=('arial 10 bold'), padx=1)
        self.lblNationality.grid(row=8, column=0, sticky=W)
        self.txtNationality = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Nationality)
        self.txtNationality.grid(row=8, column=1, pady=3, padx=30)

        self.lblGender = Label(LeftFrame, text='Gender: ', font=('arial 10 bold'), padx=1)
        self.lblGender.grid(row=9, column=0, sticky=W)
        self.txtGender = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=Gender)
        self.txtGender.grid(row=9, column=1, pady=3, padx=30)

        self.lblCheckIn = Label(LeftFrame, text='Check In: ', font=('arial 10 bold'), padx=1)
        self.lblCheckIn.grid(row=10, column=0, sticky=W)
        self.txtCheckIn = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=CheckIn)
        self.txtCheckIn.grid(row=10, column=1, pady=3, padx=30)

        self.lblCheckOut = Label(LeftFrame, text='Check Out: ', font=('arial 10 bold'), padx=1)
        self.lblCheckOut.grid(row=11, column=0, sticky=W)
        self.txtCheckOut = Entry(LeftFrame, font=('arial 10 bold'), width=20, textvariable=CheckOut)
        self.txtCheckOut.grid(row=11, column=1, pady=3, padx=30)

        self.lblTypeOfId = Label(LeftFrame, text='Type of ID: ', font=('arial 10 bold'), padx=2, pady=2)
        self.lblTypeOfId.grid(row=12, column=0, sticky=W)
        self.txtTypeOfId = ttk.Combobox(LeftFrame, state='readonly', font=('arial 10 bold'), width=20, textvariable=TypeOfId)
        self.txtTypeOfId ['values'] = (' ', 'Passport', 'Pilot Licence', 'Driving', 'Student ID')
        self.txtTypeOfId.current(0)
        self.txtTypeOfId.grid(row=12, column=1, pady=3, padx=2)

        self.lblMeal = Label(LeftFrame, text='Meal: ', font=('arial 10 bold'), padx=2, pady=2)
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.txtMeal = ttk.Combobox(LeftFrame, state='readonly', font=('arial 10 bold'), width=20, textvariable=Meal)
        self.txtMeal['values'] = (' ', 'Breakfast', 'Lunch', 'Dinner')
        self.txtMeal.current(0)
        self.txtMeal.grid(row=13, column=1, pady=3, padx=2)

        self.lblRoomType = Label(LeftFrame, text='Room Type: ', font=('arial 10 bold'), padx=2, pady=2)
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.txtRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial 10 bold'), width=20, textvariable=RoomType)
        self.txtRoomType['values'] = (' ', 'Single', 'Double', 'Family')
        self.txtRoomType.current(0)
        self.txtRoomType.grid(row=14, column=1, pady=3, padx=2)

        self.lblRoomNo = Label(LeftFrame, text='Room No: ', font=('arial 10 bold'), padx=2, pady=2)
        self.lblRoomNo.grid(row=15, column=0, sticky=W)
        self.txtRoomNo = ttk.Combobox(LeftFrame, state='readonly', font=('arial 10 bold'), width=20, textvariable=RoomNo)
        self.txtRoomNo['values'] = (' ', '001', '002', '003', '004', '005', '006')
        self.txtRoomNo.current(0)
        self.txtRoomNo.grid(row=15, column=1, pady=3, padx=2)

        self.lblRoomExt = Label(LeftFrame, text='Room Ext No: ', font=('arial 10 bold'), padx=2, pady=2)
        self.lblRoomExt.grid(row=16, column=0, sticky=W)
        self.txtRoomExt = ttk.Combobox(LeftFrame, state='readonly', font=('arial 10 bold'), width=20, textvariable=RoomExt)
        self.txtRoomExt['values'] = (' ', '101', '102', '103', '104', '105', '106')
        self.txtRoomExt.current(0)
        self.txtRoomExt.grid(row=16, column=1, pady=3, padx=2)
#----------------------------------------Widget-----------------------------------------------------
        self.CustID = Label(RightFrame1, font=('arial 10 bold'), padx=2, pady=2,
                            text=('Customer Ref\tFirstName\tSurname\tAddress \t DOB\tMobile\tGender\tNationality\tCheck In\t Check Out'))
        self.CustID.grid(row=0, column=0, columnspan=17)

        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=0, sticky='ns')
        lsthotel = Listbox(RightFrame2, width=110, height=14, font=('arial 10 bold'), yscrollcommand=scrollbar.set)
        lsthotel.bind('<<ListboxSelect>>', HotelRecord)
        lsthotel.grid(row=0, column=0, padx=7, sticky='nsew')
        scrollbar.config(command=lsthotel.xview)
#----------------------------------------Widget-----------------------------------------------------
        self.lblNoOfDays = Label(RightFrame3, text='No of Days: ', font=('arial 11 bold'), padx=2, pady=2, bd=7)
        self.lblNoOfDays.grid(row=0, column=0, sticky=W)
        self.txtNoOfDays = Entry(RightFrame3, font=('arial 11 bold'), width=76, justify=LEFT, textvariable=NoOfDays)
        self.txtNoOfDays.grid(row=0, column=1, padx=30)

        self.lblPaidtax = Label(RightFrame3, text='Paid tax: ', font=('arial 11 bold'), padx=2, pady=2, bd=7)
        self.lblPaidtax.grid(row=1, column=0, sticky=W)
        self.txtPaidtax = Entry(RightFrame3, font=('arial 11 bold'), width=76, justify=LEFT, textvariable=Paidtax)
        self.txtPaidtax.grid(row=1, column=1, padx=30)

        self.lblSubtotal = Label(RightFrame3, text='Subtotal: ', font=('arial 11 bold'), padx=2, pady=2, bd=7)
        self.lblSubtotal.grid(row=2, column=0, sticky=W)
        self.txtSubtotal = Entry(RightFrame3, font=('arial 11 bold'), width=76, justify=LEFT, textvariable=Subtotal)
        self.txtSubtotal.grid(row=2, column=1, padx=30)

        self.lblTotalCost = Label(RightFrame3, text='Total Cost: ', font=('arial 11 bold'), padx=2, pady=2, bd=7)
        self.lblTotalCost.grid(row=3, column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3, font=('arial 11 bold'), width=76, justify=LEFT, textvariable=TotalCost)
        self.txtTotalCost.grid(row=3, column=1, padx=30)
#----------------------------------------Widget-----------------------------------------------------
        self.btnTotalAndAdd = Button(BottomFrame, text='Add New/Total', font=('arial 10 bold'), width=18, height=2, pady=0, bd=2, command=TotalAndAddData)
        self.btnTotalAndAdd.grid(row=0, column=0, padx=4)
        
        self.btnTotalAndAdd = Button(BottomFrame, text='Display', font=('arial 10 bold'), width=18, height=2, pady=0, bd=2, command=showData)
        self.btnTotalAndAdd.grid(row=0, column=1, padx=4)

        self.btnTotalAndAdd = Button(BottomFrame, text='Update', font=('arial 10 bold'), width=18, height=2, pady=1, bd=2, command=update)
        self.btnTotalAndAdd.grid(row=0, column=2, padx=4)

        self.btnTotalAndAdd = Button(BottomFrame, text='Delete', font=('arial 10 bold'), width=18, height=2, pady=1, bd=2, command=deleteData)
        self.btnTotalAndAdd.grid(row=0, column=3, padx=4)

        self.btnTotalAndAdd = Button(BottomFrame, text='Search', font=('arial 10 bold'), width=18, height=2, pady=1, bd=2, command=searchDatabase)
        self.btnTotalAndAdd.grid(row=0, column=4, padx=4)

        self.btnTotalAndAdd = Button(BottomFrame, text='Reset', font=('arial 10 bold'), width=18, height=2, pady=1, bd=2, command=Reset)
        self.btnTotalAndAdd.grid(row=0, column=5, padx=4)

        self.btnTotalAndAdd = Button(BottomFrame, text='Exit', font=('arial 10 bold'), width=18, height=2, pady=1, bd=2, command=iExit)
        self.btnTotalAndAdd.grid(row=0, column=6, padx=4)

root = Tk()
a = Hotel(root)
root.resizable(False, False)
root.mainloop()
