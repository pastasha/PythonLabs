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
        print(Citizen.count)
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
        Citizen.__init__(self,name,age,place_reg)
        try:
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
        Citizen.__init__(self,name,age,place_reg)
        try:
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
        x.Citizens.pop()

    def show(self):
        for temp in self.Citizens:
            if len(temp)==3: print("Name {} Age {} Place of Registration {}".format(temp[0],temp[1],temp[2]))
            else:
                if temp[5]=="w": print("Name {} Age {} Place of Registration {} Place of Work {} Speciality {}".format(temp[0],temp[1],temp[2],temp[3],temp[4]))
                if temp[5]=="s": print("Name {} Age {} Place of Registration {} Place of Study {} Class {}".format(temp[0],temp[1],temp[2],temp[3],temp[4]))
            

    def sort_by_name(self):
        self.Citizens.sort(key=compare_name)

    def sort_by_age(self):
        self.Citizens.sort(key=compare_age)


    
if __name__ == "__main__":
    r=Registry()
    var1 = Citizen()
    var2 = Worker()
    var3 = Schoolchild()
    var1.read()
    var2.read()
    var3.read()
    r.add_in_end(var1)
    r.add_in_end(var2)
    r.add_in_end(var3)
    r.show()
    print("sort name")
    r.sort_by_name()
    r.show()
    print("sort age")
    r.sort_by_age()
    r.show()