from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
import configparser

class Citizen:
    count=0
    __name=""
    __age=0
    __place_reg=""

    def __init__ (self):
        Citizen.count+=1
        self_name=""
        self_age=0
        self_place_reg=""
        
    def __init__ (self,name="",age=0,place_reg=""):
        Citizen.count+=1
        try:
            self.__name=name
            self.__age=age
            self.__place_reg=place_reg
        except ValueError as e:
            print (e)

    def __del__(self):
        
        Citizen.count-=1
        

    def set_name(self, name):
        self.__name=name

    def set_age(self, age):
        self.__age=age

    def set_place_reg(self, place_reg):
        self.__place_reg=place_reg

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_place_reg(self):
        return self.__place_reg

    def read(self):
        try:
            self.__name=str(input("Enter Name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {}".format(self.__name,self.__age,self.__place_reg))
    def show_str(self):
        return "Name {} Age {} Place of Registration {}".format(self.__name,self.__age,self.__place_reg)
    
    def copy(self):
        x=(self.__name,self.__age,self.__place_reg)
        return x


class Worker(Citizen):
    __place_work=""
    __speciality=""
 
    def __init__ (self):
        super(Citizen,self).__init__()
        self.__place_work=""
        self.__speciality=""
        
    def __init__ (self,name="",age=0,place_reg="",place_work="",speciality=""):
        
        try:
            self.__name=name
            self.__age=age
            self.__place_reg=place_reg
            self.__place_work=place_work
            self.__speciality=speciality
        except ValueError as e:
            print (e)

    def set_place_work(self, place_work):
        self.__place_work=place_work
        
    def get_place_work(self):
        return self.__place_work

    def set_speciality(self, speciality):
        self.__speciality=speciality
        
    def get_speciality(self):
        return self.__speciality

    def read(self):
        try:
            self.__name=str(input("Enter Name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
            self.__place_work=str(input("Enter Place of Work \n"))
            self.__speciality=str(input("Enter Speciality \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {} Place of Work {} Speciality {}".format(self.__name,self.__age,self.__place_reg,self.__place_work, self.__speciality))
    def show_str(self):
        return "Name {} Age {} Place of Registration {} Place of Work {} Speciality {}".format(self.__name,self.__age,self.__place_reg,self.__place_work, self.__speciality)

    def copy(self):
        x=(self.__name,self.__age,self.__place_reg,self.__place_work, self.__speciality,"w")
        return x

class Schoolchild(Citizen):
    __place_study=""
    __class=""

    def __init__ (self):
        super(Citizen,self).__init__()
        self.__place_study=""
        self.__class=""
        
    def __init__ (self,name="",age=0,place_reg="",place_study="",cl=""):

    
        try:
            self.__name=name
            self.__age=age
            self.__place_reg=place_reg
            self.__place_study=place_study
            self.__class=cl
        except ValueError as e:
            print (e)

    def set_place_study(self, place_study):
        self.__place_study=place_study
        
    def get_place_study(self):
        return self.__place_study

    def set_class(self, cl):
        self.__class=cl
        
    def get_class(self):
        return self.__class

    def read(self):
        try:
            self.__name=str(input("Enter Name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
            self.__place_study=str(input("Enter Place of Study \n"))
            self.__class=str(input("Enter Class \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {} Place of Study {} Class {}".format(self.__name,self.__age,self.__place_reg,self.__place_study,self.__class))
    def show_str(self):
        return "Name {} Age {} Place of Registration {} Place of Study {} Class {}".format(self.__name,self.__age,self.__place_reg,self.__place_study,self.__class)

    def copy(self):
        x=(self.__name,self.__age,self.__place_reg,self.__place_study,self.__class,"s")
        return x
   
def compare_name(inp):
        return inp[0]
def compare_age(inp):
        return inp[1]

class Window0:
    
    def __init__(self,master):
        master.protocol('WM_DELETE_WINDOW',self.close)
        frame_top=Frame(master)
        frame_top.pack()
        frame1=Frame(master)
        frame1.pack(side=TOP,fill=BOTH)
        
        self.name = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        
        self.label1=Label(frame_top, text='Database')
        self.label1.grid(row=0,column=0,sticky=E)
        self.label2=Label(frame_top, text='User')
        self.label2.grid(row=1,column=0,sticky=E)
        self.label3=Label(frame_top, text='Password')
        self.label3.grid(row=2,column=0,sticky=E)

        self.txt1=Entry(frame_top, textvariable=self.name)
        self.txt1.grid(row=0,column=1)
        self.txt2=Entry(frame_top, textvariable=self.user)
        self.txt2.grid(row=1,column=1)
        self.txt3=Entry(frame_top, textvariable=self.password)
        self.txt3.grid(row=2,column=1)
        
        self.btn1=Button(frame1,text="Login", command=self.login)
        self.btn1.pack(fill=BOTH)
        self.btn1_1=Button(frame1,text="Login with file", command=self.login1)
        self.btn1_1.pack(fill=BOTH)
        self.btn1_2=Button(frame1,text="Save login file", command=self.save)
        self.btn1_2.pack(fill=BOTH)
       

    
    def login(self):
        name1=self.name.get()
        user1=self.user.get()
        password1=self.user.get()
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=name1,
                user=user1,
                password=password1)
            if conn.is_connected: 
                global root
                root.destroy()
                root = Tk()
                Window1_1(root,[name1,password1,password1])
                root.mainloop()
        except Error as e:
            messagebox.showinfo("Error",e)
        
    def save(self):
        filename=askopenfilename()
        if ( not filename ):
           return
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "name", self.name.get())
        config.set("Settings", "user", self.user.get())
        config.set("Settings", "password", self.user.get()) 
        with open(filename, "w") as config_file:
            config.write(config_file)
            
    def login1(self):
        filename=askopenfilename()
        if ( not filename ):
           return
        config = configparser.ConfigParser()
        config.read(filename)
        name1=config.get("Settings", "name")
        user1=config.get("Settings", "user")
        password1=config.get("Settings", "password")
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=name1,
                user=user1,
                password=password1)
            if conn.is_connected: 
                global root
                root.destroy()
                root = Tk()
                Window1_1(root,[name1,password1,password1])
                root.mainloop()
        except Error as e:
            messagebox.showinfo("Error",e)


    @staticmethod
    def close():
        global root
        root.destroy() 

class Window1_1(Window0):
    array=[]
    def __init__(self,master,connects):
        master.protocol('WM_DELETE_WINDOW',self.close)
        self.connects=connects
        frame_top=Frame(master)
        frame_top.pack()
        frame1=Frame(master)
        frame1.pack(side=TOP,fill=BOTH)
        frame_top1=Frame(master)
        frame_top1.pack()
        frame2=Frame(master)
        frame2.pack(side=TOP,fill=BOTH)
       
        self.name = StringVar()
        self.age = StringVar()
        self.placeofregistratione = StringVar()
        
        self.label1=Label(frame_top, text='Name')
        self.label1.grid(row=0,column=0,sticky=E)
        self.label2=Label(frame_top, text='Age')
        self.label2.grid(row=1,column=0,sticky=E)
        self.label3=Label(frame_top, text='Place of Registratione')
        self.label3.grid(row=2,column=0,sticky=E)

        self.txt1=Entry(frame_top, textvariable=self.name)
        self.txt1.grid(row=0,column=1)
        self.txt2=Entry(frame_top, textvariable=self.age)
        self.txt2.grid(row=1,column=1)
        self.txt3=Entry(frame_top, textvariable=self.placeofregistratione)
        self.txt3.grid(row=2,column=1)

        self.btn1=Button(frame1,text="Add", command=self.add)
        self.btn1.pack(fill=X)
        self.btn3=Button(frame1,text="Show", command=self.show)
        self.btn3.pack(fill=X)

        self.label4=Label(frame_top1, text='Id')
        self.label4.grid(row=0,column=0,sticky=E)
        self.txt4=Entry(frame_top1)
        self.txt4.grid(row=0,column=1)
        self.btn4=Button(frame2,text="Delete by id", command=self.delete)
        self.btn4.pack(fill=X)
        
        self.btn2=Button(frame2,text="Close", command=self.close)
        self.btn2.pack(fill=X)
        self.btn5=Button(frame2,text="Create table", command=self.createTable)
        self.btn5.pack(fill=X)

    
    @staticmethod
    def close():
        global root
        root.destroy()

    def add(self):
         try:
            conn=mysql.connector.connect(
                host='localhost',
                database=self.connects[0],
                user=self.connects[1],
                password=self.connects[2])
            if conn.is_connected: 
                mycursor = conn.cursor()
                sql = "INSERT INTO citizens (name,age, placeofregistratione) VALUES (%s, %s, %s)"
                val = (self.name.get(), self.age.get(),self.placeofregistratione.get())
                mycursor.execute(sql, val)
            conn.commit()
         except Error as e:
            messagebox.showinfo("Error",e)

    def delete(self):
         try:
            conn=mysql.connector.connect(
                host='localhost',
                database=self.connects[0],
                user=self.connects[1],
                password=self.connects[2])
            if conn.is_connected: 
                mycursor = conn.cursor()
                sql = "DELETE FROM citizens WHERE id={}".format(self.txt4.get())
                mycursor.execute(sql)
            conn.commit()
         except Error as e:
            messagebox.showinfo("Error",e)
            
    def show(self):
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=self.connects[0],
                user=self.connects[1],
                password=self.connects[2])
            if conn.is_connected: 
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM citizens")
                myresult = mycursor.fetchall()
                for x in myresult:
                    temp=Citizen(name=x[1],age=x[2],place_reg=x[3])
                    print("Id {}".format(x[0]))
                    temp.show()
        except Error as e:
            messagebox.showinfo("Error",e)

    def createTable(self):
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=self.connects[0],
                user=self.connects[1],
                password=self.connects[2])
            if conn.is_connected: 
                mycursor = conn.cursor()
                mycursor.execute('''CREATE TABLE `citizens` (
 `id` int(7) NOT NULL,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `placeofregistratione` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;''')

                mycursor.execute('''ALTER TABLE `citizens`
  ADD PRIMARY KEY (`id`);''')
                mycursor.execute('''ALTER TABLE `citizens`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT;''')
            conn.commit()
        except Error as e:
            messagebox.showinfo("Error",e)
        
    
if __name__ == "__main__":
    root = Tk()
    Window0(root)
    root.mainloop()
