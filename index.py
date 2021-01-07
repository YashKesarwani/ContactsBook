from tkinter import *
import os
import time
from database import *


def error():
    global screen2
    screen2=Toplevel(screen1)
    screen2.title('Failure')
    screen2.geometry("220x150")
    screen2['bg']='orange'
    Label(screen2,text='',bg='orange').pack()
    Label(screen2,text="First Name, Email and Mobile number are required fields",bg='white',fg='red'
    ,font=("Calibri",12),wraplength=200,justify='center').pack()
    Label(screen2,text='',bg='orange').pack()
    Button(screen2,text='Ok',command=screen2.destroy,width='10').pack()

def email_error():
    global screen2
    screen2=Toplevel(screen1)
    screen2.title('Failure')
    screen2.geometry('300x200')
    screen2['bg']='orange'
    Label(screen2,text='',bg='orange').pack()
    Label(screen2,text='Email ID already registered',bg='white',fg='red',font=('Calibri',12)).pack()
    Label(screen2,text="Try another Email ID",bg='white',fg='red',font=("Calibri",12)).pack()
    Label(screen2,text="",bg="orange").pack()
    Button(screen2,text="Ok",command=screen2.destroy,width='10').pack()


def success():
    screen1.destroy()
    global screen3
    screen3=Toplevel(screen)
    screen3.title('Success')
    screen3.geometry('200x100')
    screen3['bg']='orange'
    Label(screen3,text="",bg='orange').pack()
    Label(screen3,text="Contact Saved",bg='white',fg="green",font=("Calibri",12)).pack()
    Label(screen3,text="",bg="orange").pack()
    Button(screen3,text="Ok",command=screen3.destroy,width='10').pack()

def success2():
    screen4.destroy()
    screen3.destroy()
    global screen5
    screen5=Toplevel(screen)
    screen5.title('Success')
    screen5.geometry('200x100')
    screen5['bg']='orange'
    Label(screen5,text="",bg='orange').pack()
    Label(screen5,text="Contact Saved",bg='white',fg="green",font=("Calibri",12)).pack()
    Label(screen5,text="",bg="orange").pack()
    Button(screen5,text="Ok",command=screen5.destroy,width='10').pack()


def addNumber():
    fName_info=fName.get()
    lName_info=lName.get()
    mobile_info=mobile.get()
    mobile2_info=mobile2.get()
    email_info=email.get()
    group_info=group.get()
    if fName_info=="" or mobile_info=="" or email_info=="":
        error()
    else:
        d=(email_info,)
        result=searchEmail(d)
        if result!=0:
            if mobile2_info=="":
                mobile2_info='NULL'
            elif lName_info=="":
                lName_info='NULL'
            elif len(group_info)==0:
                group_info='NULL'
                print("ok")
            data=(fName_info,lName_info,mobile_info,mobile2_info,email_info,group_info)
            addToDB(data)
            success()
        else:
            email_error()

def addContact():
    global screen1
    screen1=Toplevel(screen)
    screen1.title('Add Contact')
    screen1.geometry('300x450')
    screen1['bg']='orange'

    global fName
    global lName
    global mobile
    global mobile2
    global email
    global group
    fName=StringVar()
    lName=StringVar()
    mobile=IntVar()
    mobile2=IntVar()
    email=StringVar()
    group=StringVar()
    Label(screen1,text='',bg='orange').pack()
    
    Label(screen1,text='First Name *',bg='orange').pack()
    Entry(screen1,textvariable=fName).pack()
    Label(screen1,text='',bg='orange').pack()

    Label(screen1,text='Last Name',bg='orange').pack()
    Entry(screen1,textvariable=lName).pack()
    Label(screen1,text='',bg='orange').pack()

    Label(screen1,text='Mobile *',bg='orange').pack()
    Entry(screen1,textvariable=mobile).pack()
    Label(screen1,text='',bg='orange').pack()

    Label(screen1,text='Mobile 2',bg='orange').pack()
    Entry(screen1,textvariable=mobile2).pack()
    Label(screen1,text='',bg='orange').pack()

    Label(screen1,text='Email *',bg='orange').pack()
    Entry(screen1,textvariable=email).pack()
    Label(screen1,text='',bg='orange').pack()

    Label(screen1,text='Group',bg='orange').pack()
    Entry(screen1,textvariable=group).pack()
    Label(screen1,text='',bg='orange').pack()
    Button(screen1,text='Save',width='10',height='1',command=addNumber).pack()

def sel(event):
    x=lbox.curselection()[0]
    f=lbox.get(x)
    name1.set(f)

def viewContact():
    global screen3
    screen3=Toplevel(screen)
    screen3.title('View Contacts')
    screen3.geometry('260x450')
    screen3['bg']='orange'

    data=getAllContacts()
    names=[]
    for d in data:
        if d[2]=='NULL':
            names.append(d[1])
        else:
            names.append(d[1]+" "+d[2])
    
    Label(screen3,text="Contacts List",bg="green",fg='white',width="260",height="2", font=("Calibri",13)).pack()
    Label(screen3,text="",bg='orange').pack()
    global lbox
    lbox=Listbox(screen3,width='260')
    lbox.pack()
    scrollbar=Scrollbar(screen3)
    scrollbar.pack(side=RIGHT,fill=Y)
    for name in names:
        lbox.insert(END,name)
    lbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lbox.yview)
    Label(screen3,text='',bg='orange').pack()
    lbox.bind("<<ListboxSelect>>",sel)
    global name1
    name1=StringVar()
    
    Label(screen3,text="Enter/Select file name",bg='orange').pack()
    Entry(screen3,textvariable=name1).pack()
    Label(screen3,text="",bg='orange').pack()
    Button(screen3,text="View Details",command=viewDetail,width='10').pack()
    Button(screen3,text="Edit",command=editDetail,width='10').pack()
    Button(screen3,text="Delete",command=deleteRecord,width='10').pack()
    Button(screen3,text="Back",command=screen3.destroy,width='10').pack()

def viewDetail():
    name=name1.get()
    global screen4
    screen4=Toplevel(screen3)
    screen4.title(name)
    screen4.geometry('250x550')
    screen4['bg']='orange'

    data=getRecord(name)
    Label(screen4,text='Contact Details',fg='white',bg='green',width='200',height='2',font=('Calibri',12)).pack()
    Label(screen4,text='',bg='orange').pack()
    Label(screen4,text='Name',bg='orange',fg='white').pack()
    T1=Text(screen4,height=2,wrap=WORD)
    T1.pack()
    if data[0][2]!='NULL':
        name2=data[0][1]+" "+data[0][2]
    else:
        name2=data[0][1]
    T1.insert(END,name2)
    Label(screen4,text='',bg='orange').pack()
    
    Label(screen4,text='Mobile',bg='orange',fg='white').pack()
    T2=Text(screen4,height=2,wrap=WORD)
    T2.pack()
    T2.insert(END,data[0][3])
    Label(screen4,text='',bg='orange').pack()
    if data[0][4]!='NULL':
        Label(screen4,text='Mobile 2',bg='orange',fg='white').pack()
        T3=Text(screen4,height=2,wrap=WORD)
        T3.pack()
        T3.insert(END,data[0][4])
        Label(screen4,text='',bg='orange').pack()

    Label(screen4,text='Email',bg='orange',fg='white').pack()
    T4=Text(screen4,height=2,wrap=WORD)
    T4.pack()
    T4.insert(END,data[0][5])
    Label(screen4,text='',bg='orange').pack()

    if data[0][6]!='NULL':
        Label(screen4,text='Group',bg='orange',fg='white').pack()
        T5=Text(screen4,height=2,wrap=WORD)
        T5.pack()
        T5.insert(END,data[0][6])
        Label(screen4,text='',bg='orange').pack()

    Button(screen4,text='Close',width='10',command=screen4.destroy).pack()

def editDetail():
    global screen4
    screen4=Toplevel(screen3)
    screen4.title('Edit Contact')
    screen4.geometry('300x450')
    screen4['bg']='orange'

    name=name1.get()
    global fName
    global lName
    global mobile
    global mobile2
    global email
    global group
    fName=StringVar()
    lName=StringVar()
    mobile=IntVar()
    mobile2=IntVar()
    email=StringVar()
    group=StringVar()
    Label(screen4,text='',bg='orange').pack()
    
    data=getRecord(name)
    Label(screen4,text='First Name *',bg='orange').pack()
    E1=Entry(screen4,textvariable=fName)
    E1.pack()
    E1.insert(END,data[0][1])
    Label(screen4,text='',bg='orange').pack()

    if data[0][2]!='NULL':
        Label(screen4,text='Last Name',bg='orange').pack()
        E2=Entry(screen4,textvariable=lName)
        E2.pack()
        E2.insert(END,data[0][2])
        Label(screen4,text='',bg='orange').pack()

    Label(screen4,text='Mobile *',bg='orange').pack()
    E3=Entry(screen4,textvariable=mobile)
    E3.pack()
    E3.insert(END,data[0][3])
    Label(screen4,text='',bg='orange').pack()

    if data[0][4]!='NULL':
        Label(screen4,text='Mobile 2',bg='orange').pack()
        E4=Entry(screen4,textvariable=mobile2)
        E4.pack()
        E4.insert(END,data[0][4])
        Label(screen4,text='',bg='orange').pack()

    Label(screen4,text='Email *',bg='orange').pack()
    E5=Entry(screen4,textvariable=email)
    E5.pack()
    E5.insert(END,data[0][5])
    Label(screen4,text='',bg='orange').pack()

    if data[0][6]!='NULL':
        Label(screen4,text='Group',bg='orange').pack()
        E6=Entry(screen4,textvariable=group)
        E6.pack()
        E6.insert(END,data[0][6])
        Label(screen4,text='',bg='orange').pack()

    global uid
    uid=data[0][0]
    Button(screen4,text='Save',width='10',height='1',command=editNumber).pack()
    Button(screen4,text='Close',width='10',height='1',command=screen4.destroy).pack()

def editNumber():
    fName_info=fName.get()
    lName_info=lName.get()
    mobile_info=mobile.get()
    mobile2_info=mobile2.get()
    email_info=email.get()
    group_info=group.get()
    id=int(uid)
    if fName_info=="" or mobile_info=="" or email_info=="":
        error()
    else:
        d=(email_info,)
        result=searchEmail(d)
        if result==0:
            if mobile2_info=="":
                mobile2_info='NULL'
            elif lName_info=="":
                lName_info='NULL'
            elif len(group_info)==0:
                group_info='NULL'
                print("ok")
            data=(fName_info,lName_info,mobile_info,mobile2_info,email_info,group_info,id)
            editInDB(data)
            success2()


def deleteRecord():
    name=name1.get()
    screen4=Toplevel(screen3)
    screen4.title(name)
    screen4.geometry('200x200')
    screen4['bg']='orange'

    data=deleteNumber(name)
    if data==1:
        Label(screen4,text="",bg='orange').pack()
        Label(screen4,text="Contact Deleted",bg='white',fg="green",font=("Calibri",12)).pack()
        Label(screen4,text="",bg="orange").pack()
        Button(screen4,text="Ok",command=screen4.destroy,width='10').pack()
    time.sleep(5)
    screen3.destroy()


def main_screen():
    global screen 
    screen=Tk()
    screen.geometry("350x450")
    screen.title("Contact Book")
    screen['bg']='orange'

    #Create table in the database
    createTable()
    Label(text='Contact Book', bg='white', fg='black',width='300',height='2',font=('Calibri',13)).pack()
    Label(text='',bg='orange').pack()
    Button(text='Add Contact',width='30',height='2',command=addContact).pack()
    Label(text='',bg='orange').pack()
    Button(text='View Contact',width='30',height='2',command=viewContact).pack()
    Label(text='',bg='orange').pack()
    Button(text='Exit',width='30',height='2',command=screen.destroy).pack()
    
    screen.mainloop()

main_screen()
