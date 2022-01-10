from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import pickle


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
    
class Registry():
    Citizens=[]
    def add_in_end(Citizens, c):
        x=Registry()
        x.Citizens.append(c.copy())

    def remove_from_end(Citizens):
        x=Registry()
        if len(x.Citizens)>0:
            x.Citizens.pop()

    def show(self):
        for temp in self.Citizens:
            if len(temp)==3: print("Name {} Age {} Place of Registration {}".format(temp[0],temp[1],temp[2]))
            else:
                if temp[5]=="w": print("Name {} Age {} Place of Registration {} Place of Work {} Speciality {}".format(temp[0],temp[1],temp[2],temp[3],temp[4]))
                if temp[5]=="s": print("Name {} Age {} Place of Registration {} Place of Study {} Class {}".format(temp[0],temp[1],temp[2],temp[3],temp[4]))

    def show_str(self):
        str=""
        for temp in self.Citizens:
            if len(temp)==3: str=str+ "Name {} Age {} Place of Registration {}".format(temp[0],temp[1],temp[2])+"\n"
            else:
                if temp[5]=="w": str=str + "Name {} Age {} Place of Registration {} Place of Work {} Speciality {}".format(temp[0],temp[1],temp[2],temp[3],temp[4])+"\n"
                if temp[5]=="s": str=str + "Name {} Age {} Place of Registration {} Place of Study {} Class {}".format(temp[0],temp[1],temp[2],temp[3],temp[4])+"\n"
        return str
            

    def sort_by_name(self):
        self.Citizens.sort(key=compare_name)

    def sort_by_age(self):
        self.Citizens.sort(key=compare_age)

class Window0:
    
    def __init__(self,master):
        master.protocol('WM_DELETE_WINDOW',self.close)
        master.geometry('300x310')
        frame =Frame(master)
        frame.pack(fill=X)

        self.btn1=Button(frame,text="add a Citizen", command=self.openCitizen)
        self.btn1.pack(fill=BOTH)
        self.btn1_1=Button(frame,text="add a Worker", command=self.openWorker)
        self.btn1_1.pack(fill=BOTH)
        self.btn1_2=Button(frame,text="add a Schoolchild", command=self.openSchool)
        self.btn1_2.pack(fill=BOTH)
        self.btn1_3=Button(frame,text="Show", command=self.show)
        self.btn1_3.pack(fill=BOTH)
        self.btn1_7=Button(frame,text="Remove end", command=self.remove)
        self.btn1_7.pack(fill=BOTH)
        self.btn1_4=Button(frame,text="Clear", command=self.clear)
        self.btn1_4.pack(fill=BOTH)
        self.btn1_5=Button(frame,text="Sort by name", command=self.sortn)
        self.btn1_5.pack(fill=BOTH)
        self.btn1_6=Button(frame,text="Sort by age", command=self.sorta)
        self.btn1_6.pack(fill=BOTH)
        self.btn1_8=Button(frame,text="Select file", command=self.select)
        self.btn1_8.pack(fill=BOTH)
        self.btn1_9=Button(frame,text="Create dump", command=self.dump)
        self.btn1_9.pack(fill=BOTH)
        self.btn1_10=Button(frame,text="Load dump", command=self.load)
        self.btn1_10.pack(fill=BOTH)

        
        self.btn2=Button(frame,text="Close", command=self.close)
        self.btn2.pack(fill=BOTH)

    @staticmethod
    def openCitizen():
        global root
        root.destroy()
        root = Tk()
        Window1_1(root)
        root.mainloop()
    @staticmethod
    def openWorker():
        global root
        root.destroy()
        root = Tk()
        Window1_2(root)
        root.mainloop()
    @staticmethod
    def openSchool():
        global root
        root.destroy()
        root = Tk()
        Window1_3(root)
        root.mainloop()

    @staticmethod
    def close():
        global root
        root.destroy()

    @staticmethod
    def show():
        print()
        r.show()

    @staticmethod
    def remove():
        r.remove_from_end()
       
    @staticmethod
    def clear():
        r.Citizens.clear()

        
    @staticmethod
    def sortn():
        r.sort_by_name()
        
    @staticmethod
    def sorta():
        r.sort_by_age()
    @staticmethod
    def select():
        filename=askopenfilename()
        global root
        root.destroy()
        root = Tk()
        Window2(root,filename)
        root.mainloop()
        
    def dump(self):
        with open('r.pickle','wb') as f:
            pickle.dump(r.Citizens,f)
    def load(self):
        with open('r.pickle','rb') as f:
            r.Citizens=pickle.load(f)

class Window2(Window0):
    file=""

    def __init__(self,master,filename):
        self.file=filename+""
        master.protocol('WM_DELETE_WINDOW',self.close)
        master.geometry('300x170')
        frame =Frame(master)
        frame.pack(fill=X)

        self.btn1=Button(frame,text="Write list", command=self.write)
        self.btn1.pack(fill=BOTH)
        self.btn1_1=Button(frame,text="Print list", command=self.print)
        self.btn1_1.pack(fill=BOTH)
        self.btn1_2=Button(frame,text="Clear file", command=self.clear)
        self.btn1_2.pack(fill=BOTH)       
        self.btn2=Button(frame,text="Close", command=self.close)
        self.btn2.pack(fill=BOTH)

        self.name = StringVar()
        
        self.label1=Label(frame, text='Name')
        self.label1.pack(fill=BOTH)
        self.txt1=Entry(frame, textvariable=self.name)
        self.txt1.pack(fill=BOTH)
        self.btn3=Button(frame,text="Change name", command=self.changename)
        self.btn3.pack(fill=BOTH)

    
    def write(self):
        fr=open(self.file+"",'w')
        fr.write(r.show_str()+"")
        fr.close()
        
    
    def print(self):
        fr=open(self.file+"",'r')
        text=fr.read()
        print(text)
        fr.close()
        
    
    def clear(self):
        fr=open(self.file+"",'w')
        fr.write("")
        fr.close()
        
    def changename(self):
        if self.name!="":
            fr=os.path.basename(self.file)
            newname=self.file.replace(os.path.splitext(fr)[0]+".txt",self.name.get()+".txt")
            os.rename(self.file,newname)

    @staticmethod
    def close():
        global root
        root.destroy()
        root = Tk()
        Window0(root)
        root.mainloop()



class Window1_1(Window0):
    array=[]
    def __init__(self,master):
        master.protocol('WM_DELETE_WINDOW',self.close)
        var1=StringVar()
        frame_top=Frame(master)
        frame_top.pack()
        frame1=Frame(master)
        frame1.pack(side=TOP,fill=BOTH)
       
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
        self.btn2=Button(frame1,text="back", command=self.back)
        self.btn2.pack(fill=X)

    @staticmethod
    def back():
        global root
        root.destroy()
        root = Tk()
        Window0(root)
        root.mainloop()
    @staticmethod
    def close():
        global root
        root.destroy()

    def add(self):
        
        temp=Citizen(name = self.name.get(),age = self.age.get(),place_reg = self.placeofregistratione.get())
        r.add_in_end(temp)

class Window1_2(Window0):
    array=[]
    def __init__(self,master):
        master.protocol('WM_DELETE_WINDOW',self.close)
        var1=StringVar()
        frame_top=Frame(master)
        frame_top.pack()
        frame1=Frame(master)
        frame1.pack(side=TOP,fill=BOTH)
       
        self.name = StringVar()
        self.age = StringVar()
        self.placeofregistratione = StringVar()
        self.place_work = StringVar()
        self.speciality = StringVar()
        
        self.label1=Label(frame_top, text='Name')
        self.label1.grid(row=0,column=0,sticky=E)
        self.label2=Label(frame_top, text='Age')
        self.label2.grid(row=1,column=0,sticky=E)
        self.label3=Label(frame_top, text='Place of Registratione')
        self.label3.grid(row=2,column=0,sticky=E)
        self.label4=Label(frame_top, text='Place of Work')
        self.label4.grid(row=3,column=0,sticky=E)
        self.label5=Label(frame_top, text='Speciality')
        self.label5.grid(row=4,column=0,sticky=E)

        self.txt1=Entry(frame_top, textvariable=self.name)
        self.txt1.grid(row=0,column=1)
        self.txt2=Entry(frame_top, textvariable=self.age)
        self.txt2.grid(row=1,column=1)
        self.txt3=Entry(frame_top, textvariable=self.placeofregistratione)
        self.txt3.grid(row=2,column=1)
        self.txt4=Entry(frame_top, textvariable=self.place_work)
        self.txt4.grid(row=3,column=1)
        self.txt5=Entry(frame_top, textvariable=self.speciality)
        self.txt5.grid(row=4,column=1)

        

        self.btn1=Button(frame1,text="Add", command=self.add)
        self.btn1.pack(fill=X)
        self.btn2=Button(frame1,text="back", command=self.back)
        self.btn2.pack(fill=X)

    @staticmethod
    def back():
        global root
        root.destroy()
        root = Tk()
        Window0(root)
        root.mainloop()
    @staticmethod
    def close():
        global root
        root.destroy()

    def add(self):
        
        temp=Worker(name = self.name.get(),age = self.age.get(),place_reg = self.placeofregistratione.get(),place_work=self.place_work.get(),speciality=self.speciality.get())
        
        r.add_in_end(temp)

class Window1_3(Window0):
    array=[]
    def __init__(self,master):
        master.protocol('WM_DELETE_WINDOW',self.close)
        var1=StringVar()
        frame_top=Frame(master)
        frame_top.pack()
        frame1=Frame(master)
        frame1.pack(side=TOP,fill=BOTH)
       
        self.name = StringVar()
        self.age = StringVar()
        self.placeofregistratione = StringVar()
        self.place_work = StringVar()
        self.speciality = StringVar()
        
        self.label1=Label(frame_top, text='Name')
        self.label1.grid(row=0,column=0,sticky=E)
        self.label2=Label(frame_top, text='Age')
        self.label2.grid(row=1,column=0,sticky=E)
        self.label3=Label(frame_top, text='Place of Registratione')
        self.label3.grid(row=2,column=0,sticky=E)
        self.label4=Label(frame_top, text='Place of Study')
        self.label4.grid(row=3,column=0,sticky=E)
        self.label5=Label(frame_top, text='Class')
        self.label5.grid(row=4,column=0,sticky=E)

        self.txt1=Entry(frame_top, textvariable=self.name)
        self.txt1.grid(row=0,column=1)
        self.txt2=Entry(frame_top, textvariable=self.age)
        self.txt2.grid(row=1,column=1)
        self.txt3=Entry(frame_top, textvariable=self.placeofregistratione)
        self.txt3.grid(row=2,column=1)
        self.txt4=Entry(frame_top, textvariable=self.place_work)
        self.txt4.grid(row=3,column=1)
        self.txt5=Entry(frame_top, textvariable=self.speciality)
        self.txt5.grid(row=4,column=1)

        

        self.btn1=Button(frame1,text="Add", command=self.add)
        self.btn1.pack(fill=X)
        self.btn2=Button(frame1,text="back", command=self.back)
        self.btn2.pack(fill=X)

    @staticmethod
    def back():
        global root
        root.destroy()
        root = Tk()
        Window0(root)
        root.mainloop()
    @staticmethod
    def close():
        global root
        root.destroy()

    def add(self):
        
        temp=Schoolchild(name = self.name.get(),age = self.age.get(),place_reg = self.placeofregistratione.get(),place_work=self.place_work.get(),speciality=self.speciality.get())
        
        r.add_in_end(temp)
        
    
if __name__ == "__main__":
    r=Registry()
    root = Tk()
    Window0(root)
    root.mainloop()
