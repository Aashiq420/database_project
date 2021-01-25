from tkinter import *
from tkinter  import messagebox as mb
import mysql.connector

def verify():
    mydb = mysql.connector.connect(
    host='localhost',
    user='lifechoices', 
    password='@Lifechoices1234',
    database='dentistry',
    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    usr = 'aashiq'#username.get()
    psw = 'letmein'#password.get()
    sql = "select * from Login where username = %s and password=%s"
    mycursor.execute(sql,[(usr),(psw)])
    result = mycursor.fetchall()
    if result:
        for i in result:
            logged()
            root.destroy()
            break
    else:
        mb.showerror("Login fail","Error somewhere")

def logged():
    mb.showinfo("Success", "You have successfully logged in")

    #new tk window
    main = Tk()
    main.title("Databases")
    main.geometry("550x200")
    
    #tk widgets
    dentist_lbl = Label(main, text="Table of Dentists:", anchor='w')
    dcode = Label(main, text="Dentist code\n___________", borderwidth=2, relief="ridge", anchor='w')
    dname = Label(main, text="Name\n___________", borderwidth=2, relief="ridge", anchor='w')
    dsname = Label(main, text="Surname\n__________", borderwidth=2, relief="ridge", anchor='w')
    contact = Label(main, text="Contact no.\n___________", borderwidth=2, relief="ridge", anchor='w')
    pracno = Label(main, text="Practice no.\n___________", borderwidth=2, relief="ridge", anchor='w')
  
    #tk place
    dentist_lbl.place(x=5,y=15)
    dcode.place(x=5,y=50)
    dname.place(x=105,y=50)
    dsname.place(x=215,y=50)
    contact.place(x=305,y=50)
    pracno.place(x=405,y=50)

    #connect to db
    mydb = mysql.connector.connect(
    host='localhost',
    user='lifechoices', 
    password='@Lifechoices1234',
    database='dentistry',
    auth_plugin='mysql_native_password')

    #display dentist data
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Dentists')
    for i in mycursor:
        counter=1
        data = str(i)
        data = data[1:-1]
        data = data.split(',')
        for j in data:
            j = j.replace("'",'')

            if counter==1:
                dcode['text']+="\n"+j
                counter+=1

            elif counter==2:
                dname['text']+="\n"+j
                counter+=1
    
            elif counter==3:
                dsname['text']+="\n"+j
                counter+=1

            elif counter==4:
                contact['text']+="\n"+j
                counter+=1

            elif counter==5:
                j = j[:-2]
                pracno['text']+="\n"+j
                counter+=1

def register():
    pass




#tkinter init
root = Tk()
root.title("Databases")
root.geometry("300x200")

# Tkinter widgets
user_lbl = Label(root, text="Username:")
pswrd_lbl = Label(root, text="Password:")
username = Entry(root)
password = Entry(root, show="*")
login_btn = Button(root, text="Login", command=verify)
reg_btn = Button(root, text="Register", command=register)

#tkinter placements
user_lbl.place(x=5,y=10)
pswrd_lbl.place(x=5,y=55)
username.place(x=80,y=10)
password.place(x=80,y=55)
login_btn.place(x=5,y=100)
reg_btn.place(x=100,y=100)





root.mainloop()