#Aashiq Adams 
#Python+Databases end of module project
#Lifechoices Online
import sys
import os
from tkinter import *
from tkinter  import messagebox as mb
import mysql.connector
from datetime import *

#Functions
#verify logout
def verify_logout():
    mydb = mysql.connector.connect(
    host='localhost',
    user='lifechoices', 
    password='@Lifechoices1234',
    database='lifechoicesonline',
    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()
    usr = username.get()
    psw = password.get()
    sql = "select * from users where username = %s and password=%s"
    mycursor.execute(sql,[(usr),(psw)])
    result = mycursor.fetchall()
    if result:    
        mb.showinfo("Successful","Logout Successful")
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        now = datetime.now()
        time = now.strftime("%H:%M %p")
        typ = 'user'     
        log_sql = "update time_log set type=%s, logout_time=%s where log_username=%s"
        try:
            mycursor.execute(log_sql,[(typ),(time),(usr)])
            mydb.commit()
            restart()
        except:
            mb.showerror('Error','Error in time_log')
    else:
        mb.showerror("Login fail","Error somewhere")
#add user to admin
def make_admin():
     #exit make admin menu
    def exit_adm():
        new.destroy()
    def make_admin_action():
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        try:
            user_id = int(admin_id.get())
        except:
            mb.showerror("Error","Only enter a number for the id")
        sql = "insert into admin_users(full_name, username, password) select full_name, username, password from users where id=%s"
        try:
            mycursor.execute(sql,[(user_id)])
            mydb.commit()
            mb.showinfo("Success","Successfully made user id="+str(user_id)+" an admin")
            new.destroy()
        except:
            mb.showerror("Error","Error in MySQL connection")
     
    #remove user window
    new = Tk()
    new.title("Make user Admin")
    new.geometry("320x100")

    #widgets
    id_lbl = Label(new, text="Enter ID of user to add to Admin:")
    admin_id = Entry(new, width=10)
    admin_btn = Button(new, text="Make admin", command=make_admin_action)
    exit_btn = Button(new, text="Exit",command=exit_adm)

    #placements
    id_lbl.place(x=5,y=5)
    admin_id.place(x=230,y=5)
    admin_btn.place(x=15,y=40)
    exit_btn.place(x=135,y=40)

    new.mainloop()
#Add user func
def add_user():
    #exit add menu
    def exit_add():
        add.destroy()
        admin_window(usr)
    #create user function
    def create():
        #create database/table if not exist
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists lifechoicesonline")
        mycursor.execute("create table if not exists users(id int(11) not null auto_increment, full_name varchar(60) default null, username varchar(50) default null, password varchar(20) default null, primary key(id))")
        #code to add user to database
        f = fname.get()
        u = uname.get()
        p = passw.get()

        if f=='' or u=='' or p=='':
            mb.showerror("Error","Do not leave any fields empty")
            add.destroy()
            add_user()
        else:
            mydb = mysql.connector.connect(
            host='localhost',
            user='lifechoices', 
            password='@Lifechoices1234',
            database='lifechoicesonline',
            auth_plugin='mysql_native_password')

            try:
                mycursor = mydb.cursor()
                sql = "insert into users(full_name, username, password) values(%s,%s,%s)"
                mycursor.execute(sql,[(f),(u),(p)])
                mydb.commit()
            except:
                mb.showerror("Error","Error connecting to database")
            mb.showinfo("Success","Username: "+u+" has been added to the database")
            add.destroy()

    #new tkinter window
    add = Tk()
    add.title("Add user by admin")
    add.geometry("235x200")

    #widgets
    head_lbl = Label(add)
    fname_lbl = Label(add, text="Full Name:")
    uname_lbl = Label(add, text="Username:")
    passw_lbl = Label(add, text="Password:")
    fname = Entry(add)
    uname = Entry(add)
    passw = Entry(add)
    create_btn = Button(add, text="Add User", command=create)
    exit_btn = Button(add, text="Exit",command=exit_add)

    #placements
    fname_lbl.place(x=5,y=5)
    uname_lbl.place(x=5,y=45)
    passw_lbl.place(x=5,y=85)
    fname.place(x=5,y=25)
    uname.place(x=5,y=65)
    passw.place(x=5,y=105)
    create_btn.place(x=5, y=130)
    exit_btn.place(x=125,y=130)


    add.mainloop()
#remove user
def remove_user():
    #exit remove screen
    def exit_rmv():
        rmv.destroy()
    #action of removing
    def remove_action():
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        user_id = remove_id.get()
        sql = "delete from users where id = %s"
        try:
            mycursor.execute(sql,[(user_id)])
            mydb.commit()
            mb.showinfo("Success","Successfully removed user with id="+user_id)
            rmv.destroy()
        except:
            mb.showerror("Error","Error connecting to MySql")
    #remove user window
    rmv = Tk()
    rmv.title("Remove user")
    rmv.geometry("320x100")

    #widgets
    id_lbl = Label(rmv, text="Enter ID of user to be removed:")
    remove_id = Entry(rmv, width=10)
    remove_btn = Button(rmv, text="Remove user", command=remove_action)
    exit_btn = Button(rmv, text="Exit", command=exit_rmv)

    #placements
    id_lbl.place(x=5,y=5)
    remove_id.place(x=220,y=5)
    remove_btn.place(x=15,y=40)
    exit_btn.place(x=145,y=40)

    rmv.mainloop()
#restart function
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    username['text']=''
    password['text']=''
#login verify function
def verify():
    #create database/table if not exists
    mydb = mysql.connector.connect(
    host='localhost',
    user='lifechoices', 
    password='@Lifechoices1234',
    database='lifechoicesonline',
    auth_plugin='mysql_native_password')

    #create database/table if not exists
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists lifechoicesonline")
    mycursor.execute("create table if not exists users(id int(11) not null auto_increment, full_name varchar(60) default null, username varchar(50) default null, password varchar(20) default null, primary key(id))")
    mycursor.execute("create table if not exists time_log(log_id int(11) not null auto_increment, type varchar(15) default null, log_username varchar(50) default null, login_time varchar(10) default null, logout_time varchar(10) default null, primary key(id))")

    #get string from entries
    usr = username.get()
    psw = password.get()
    #check fields empty
    if usr=='' or psw =='':
        mb.showwarning("Warning","Please do not leave fields empty")
        restart()
    #check password length
    if len(psw)>20:
        mb.showwarning("Warning","Too many characters for password")
        restart()

    sql = "select * from users where username = %s and password=%s"
    mycursor.execute(sql,[(usr),(psw)])
    result = mycursor.fetchall()
    if result:    
        mb.showinfo("Successful","Login Successful")

        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        now = datetime.now()
        time = now.strftime("%H:%M %p")
        typ = 'user'
        
        log_sql="insert into time_log(type,log_username,login_time,logout_time) values(%s,%s,%s,'<null>')"
        try:
            mycursor.execute(log_sql,[(typ),(usr),(time)])
            mydb.commit()
            restart()
        except:
            mb.showerror('Error','Error in time_log')

    else:
        mb.showerror("Login fail","Error somewhere")
#register new user function
def register():
    #create user function
    def create():
        #create database/table if not exist
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists lifechoicesonline")
        mycursor.execute("create table if not exists users(id int(11) not null auto_increment, full_name varchar(60) default null, username varchar(50) default null, password varchar(20) default null, primary key(id))")
        #code to add user to database
        f = fname.get()
        u = uname.get()
        p = passw.get()
        if f=='' or u=='' or p=='':
            mb.showerror("Error","Do not leave any fields empty")
            reg.destroy()
            register()
        else:
            mydb = mysql.connector.connect(
            host='localhost',
            user='lifechoices', 
            password='@Lifechoices1234',
            database='lifechoicesonline',
            auth_plugin='mysql_native_password')

            try:
                mycursor = mydb.cursor()
                sql = "insert into users(full_name, username, password) values(%s,%s,%s)"
                mycursor.execute(sql,[(f),(u),(p)])
                mydb.commit()
            except:
                mb.showerror("Error","Error connecting to database")
                register()
            mb.showinfo("Success","Username: "+u+" has been added to the database")
            reg.destroy()

    #new tkinter window
    reg = Tk()
    reg.title("Register")
    reg.geometry("200x200")

    #widgets
    fname_lbl = Label(reg, text="Full Name:")
    uname_lbl = Label(reg, text="Username:")
    passw_lbl = Label(reg, text="Password:")
    fname = Entry(reg)
    uname = Entry(reg)
    passw = Entry(reg)

    create_btn = Button(reg, text="Create User", command=create)
    exit_btn = Button(reg, text="Exit", command=restart)

    #placements
    fname_lbl.place(x=5,y=5)
    uname_lbl.place(x=5,y=45)
    passw_lbl.place(x=5,y=85)
    fname.place(x=5,y=25)
    uname.place(x=5,y=65)
    passw.place(x=5,y=105)
    create_btn.place(x=5, y=130)
    exit_btn.place(x=125,y=130)


    reg.mainloop()
#admin window
def admin_window(usr):
    #clear log
    def clear_log():
        #connect to db
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        try:
            mycursor.execute("delete from time_log")
        except:
            mb.showerror("Error","Error clearing time log")      
    #remove admin
    def remove_admin():
        main.destroy()
        def exit_rmv():
            rmv.destroy()
            admin_window(usr)
        #action of removing
        def remove_action():
            mydb = mysql.connector.connect(
            host='localhost',
            user='lifechoices', 
            password='@Lifechoices1234',
            database='lifechoicesonline',
            auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()
            user_id = remove_id.get()
            sql = "delete from admin_users where id = %s"
            try:
                mycursor.execute(sql,[(user_id)])
                mydb.commit()
                mb.showinfo("Success","Successfully removed admin with id="+user_id)
            except:
                mb.showerror("Error","Error connecting to MySql")
        #remove user window
        rmv = Tk()
        rmv.title("Remove admin")
        rmv.geometry("320x100")

        #widgets
        id_lbl = Label(rmv, text="Enter ID of admin to be removed:")
        remove_id = Entry(rmv, width=10)
        remove_btn = Button(rmv, text="Remove admin", command=remove_action)
        exit_btn = Button(rmv, text="Exit", command=exit_rmv)

        #placements
        id_lbl.place(x=5,y=5)
        remove_id.place(x=225,y=5)
        remove_btn.place(x=15,y=40)
        exit_btn.place(x=145,y=40)

        rmv.mainloop()
    #display users
    def show_users():
        main.destroy()
        #exit admin
        def exit_user():
            disp.destroy()
            admin_window(usr)
        #new window
        disp = Tk()
        disp.geometry("735x300")
        disp.title("Lifechoicesonline users")
        #connect to db
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        #display dentist data
        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from users')
        res = mycursor
        r=2
        #make display table
        if res:
            for a in res:
                for b in range(len(a)):
                    e = Entry(disp, width=20)
                    e.grid(row=r,column=b)
                    e.insert(END, a[b])
                r+=1

        id_lbl = Label(disp,text="User id")
        fn_lbl = Label(disp,text="Full name")
        un_lbl = Label(disp,text="Username")
        pw_lbl = Label(disp,text="Password")
        exit_btn = Button(disp, text="Exit",command=exit_user)

        exit_btn.grid(row=0,column=4)
        id_lbl.grid(row=0,column=0)
        fn_lbl.grid(row=0,column=1)
        un_lbl.grid(row=0,column=2)
        pw_lbl.grid(row=0,column=3)


        disp.mainloop()
    #display admins
    def show_admin():
        main.destroy()
        def exit_admin():
            disp.destroy()
            admin_window(usr)
        disp = Tk()
        disp.geometry("735x300")
        disp.title("Lifechoicesonline admins")
        #connect to db
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        #display dentist data
        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from admin_users')
        res = mycursor
        r=2
        if res:
            for a in res:
                for b in range(len(a)):
                    e = Entry(disp, width=20)
                    e.grid(row=r,column=b)
                    e.insert(END, a[b])
                r+=1

        id_lbl = Label(disp,text="User id")
        fn_lbl = Label(disp,text="Full name")
        un_lbl = Label(disp,text="Username")
        pw_lbl = Label(disp,text="Password")
        exit_btn = Button(disp, text="Exit",command=exit_admin)

        exit_btn.grid(row=0,column=4)
        id_lbl.grid(row=0,column=0)
        fn_lbl.grid(row=0,column=1)
        un_lbl.grid(row=0,column=2)
        pw_lbl.grid(row=0,column=3)


        disp.mainloop()
    #display time log
    def show_log():
        #exit time log window
        def exit_log():
            disp.destroy()

        #time log window
        disp = Tk()
        disp.geometry("700x300")
        disp.title("Lifechoicesonline time log")
        #connect to db
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from time_log')
        res = mycursor
        r=2
        if res:
            for a in res:
                for b in range(len(a)):
                    e = Entry(disp, width=15)
                    e.grid(row=r,column=b)
                    e.insert(END, a[b])
                r+=1

        id_lbl = Label(disp,text="Log id")
        type_lbl = Label(disp,text="Type")
        un_lbl = Label(disp,text="Username")
        li_lbl = Label(disp,text="Login time")
        lo_lbl = Label(disp,text="Logout time")
        exit_btn = Button(disp, text="Exit",command=exit_log)

        exit_btn.grid(row=0,column=5)
        id_lbl.grid(row=0,column=0)
        type_lbl.grid(row=0,column=1)
        un_lbl.grid(row=0,column=2)
        li_lbl.grid(row=0,column=3)
        lo_lbl.grid(row=0,column=4)


        disp.mainloop()
    #admin logout
    def admin_logout():
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        now = datetime.now()
        time = now.strftime("%H:%M %p")
        typ = 'admin'
        
        log_sql="update time_log set logout_time=%s where log_username=%s"
        try:
            mycursor.execute(log_sql,[(time),(usr)])
            mydb.commit()
            mb.showinfo("Logged out","Successfully logged out of admin account")
            main.destroy()
            admin_login()
        except:
            mb.showerror('Error','Error in time_log')
        

    main = Tk()
    main.title("Admin Menu")
    main.geometry("495x200")

    #button widgets
    heading_lbl = Label(main, text="Admin Menu", font=('',20,'bold'))
    add_btn = Button(main, text="Add user", command=add_user)
    remove_btn = Button(main, text="Remove user", command=remove_user)
    make_admin_btn = Button(main, text="Make user admin", command=make_admin)
    remove_admin_btn = Button(main, text="Remove admin", command=remove_admin)
    display_users_btn = Button(main, text="Display users", command=show_users)
    display_admin_btn = Button(main, text="Display admin users", command=show_admin)
    display_log_btn = Button(main, text="Display time log", command=show_log)
    admin_logout_btn = Button(main, text="Logout", command=admin_logout)
    clear_btn = Button(main, text="Clear time log",command=clear_log)



    #button placements
    heading_lbl.place(x=20,y=5)
    add_btn.place(x=5,y=50)
    remove_btn.place(x=95,y=50)
    make_admin_btn.place(x=215,y=50)
    remove_admin_btn.place(x=360,y=50)
    display_users_btn.place(x=5,y=90)
    display_admin_btn.place(x=128,y=90)
    display_log_btn.place(x=294,y=90)
    admin_logout_btn.place(x=5, y=150)
    clear_btn.place(x=125,y=150)

    main.mainloop()
#admin login function
def admin_login():
    try:
        root.destroy()
    except:
        pass
    #admin login verify
    def admin_verify():
        #create database/table if not exists
        #use username='admin' and password='admin' as default
        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        try:
            mycursor.execute("create database if not exists lifechoicesonline")
            mycursor.execute("create table if not exists admin_users(id int(11) not null auto_increment, full_name varchar(60) default null, username varchar(50) default null, password varchar(20) default null, primary key(id))")
            mycursor.execute("create table if not exists time_log(log_id int(11) not null auto_increment, type varchar(15) default null, log_username varchar(50) default null, login_time varchar(10) default null, logout_time varchar(10) default null, primary key(id))")
            mycursor.execute("insert into admin_users(full_name,username,password) values('admin','admin','admin')")
        except:
            mb.showerror("Error","Error creating default table")

        mydb = mysql.connector.connect(
        host='localhost',
        user='lifechoices', 
        password='@Lifechoices1234',
        database='lifechoicesonline',
        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        usr = username.get()
        psw = password.get()
        sql = "select * from admin_users where username = %s and password=%s"
        mycursor.execute(sql,[(usr),(psw)])
        result = mycursor.fetchall()
        if result:    
            mb.showinfo("Successful","Login Successful on Admin account")
            mydb = mysql.connector.connect(
            host='localhost',
            user='lifechoices', 
            password='@Lifechoices1234',
            database='lifechoicesonline',
            auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()

            now = datetime.now()
            time = now.strftime("%H:%M %p")
            typ = 'admin'
            
            log_sql="insert into time_log(type,log_username,login_time,logout_time) values(%s,%s,%s,'<null>')"
            try:
                mycursor.execute(log_sql,[(typ),(usr),(time)])
                mydb.commit()
            except:
                mb.showerror('Error','Error in time_log')
            admin.destroy()
            admin_window(usr)
            
            
        else:
            mb.showerror("Login fail","Login error. Contact receptionist")

    #admin login window
    admin = Tk()
    admin.title("Admin Login")
    admin.geometry("350x250")

    #widgets
    user_lbl = Label(admin, text="Username:")
    pswrd_lbl = Label(admin, text="Password:")
    username = Entry(admin)
    password = Entry(admin, show="*")
    login_btn = Button(admin, text="Login", command=admin_verify)
    norm_user_btn = Button(admin, text="Go Back", command=restart)

    #create canvas for icon image and put image on canvas
    icon_canvas = Canvas(admin, width=500, height=100)
    icon_canvas.grid()
    icon = PhotoImage(file="lco.png")
    icon_canvas.create_image(30, 5, anchor=NW, image=icon)

    #show and hide password
    def show_hide():
        if password['show']=='*':
            password['show']=''
        elif password['show']=='':
            password['show']='*'

    eye = PhotoImage(file = "eyefinal.png") 
    view_pass_btn = Button(admin, image=eye, command=show_hide)


    #tkinter placements
    user_lbl.place(x=5,y=105)
    pswrd_lbl.place(x=5,y=145)
    username.place(x=80,y=105)
    password.place(x=80,y=145)
    login_btn.place(x=80,y=190)
    norm_user_btn.place(x=175,y=190)
    view_pass_btn.place(x=250,y=142)

    admin.mainloop()

#tkinter init main program
root = Tk()
root.title("Login")
root.geometry("350x250")

#Tkinter widgets
user_lbl = Label(root, text="Username:")
pswrd_lbl = Label(root, text="Password:")
username = Entry(root)
password = Entry(root, show="*")
login_btn = Button(root, text="Login", command=verify)
logout_btn = Button(root, text='Logout', command=verify_logout)
reg_btn = Button(root, text="Register", command=register)
adm_lbl = Label(root, text="Press <Ctrl+a> for Admin login")

#create canvas for icon image and put image on canvas
icon_canvas = Canvas(root, width=500, height=100)
icon_canvas.grid()
icon = PhotoImage(file="lco.png")
icon_canvas.create_image(30, 5, anchor=NW, image=icon)

#show and hide password
def show_hide():
    if password['show']=='*':
        password['show']=''
    elif password['show']=='':
        password['show']='*'

eye = PhotoImage(file = "eyefinal.png") 
view_pass_btn = Button(root, image=eye, command=show_hide)

#open admin window on ctrl+a
root.bind('<Control-a>',lambda x:admin_login())

#tkinter placements
user_lbl.place(x=5,y=110)
pswrd_lbl.place(x=5,y=145)
username.place(x=80,y=110)
password.place(x=80,y=145)
login_btn.place(x=80,y=180)
logout_btn.place(x=165,y=180)
reg_btn.place(x=250,y=180)
view_pass_btn.place(x=250,y=142)
adm_lbl.place(x=15,y=225)

root.mainloop()