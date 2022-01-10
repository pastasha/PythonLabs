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
            self.__name=str(input("Enter name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {}".format(self.__name,self.__age,self.__place_reg))

class Worker(Citizen):
    __place_work=""
 
    def __init__ (self):
        super(Citizen,self).__init__()
        self._place_work=""
        
    def __init__ (self,name="",age=0,place_reg="",place_work=""):
        Citizen.__init__(self,name,age,place_reg)
        try:
            self.__place_work=place_work
        except ValueError as e:
            print (e)

    def set_place_work(self, place_work):
        self.__place_work=place_work
        
    def get_place_work(self):
        return self.__place_work

    def read(self):
        try:
            self.__name=str(input("Enter name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
            self.__place_work=str(input("Enter Place of Work \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {} Place of Work {}".format(self.__name,self.__age,self.__place_reg,self.__place_work))

class Schoolchild(Citizen):
    __place_study=""

    def __init__ (self):
        super(Citizen,self).__init__()
        self.__place_study=""
        
    def __init__ (self,name="",age=0,place_reg="",place_study=""):
        Citizen.__init__(self,name,age,place_reg)
        try:
            self.__place_study=place_study
        except ValueError as e:
            print (e)

    def set_place_study(self, place_study):
        self.__place_study=place_study
        
    def get_place_study(self):
        return self.__place_study

    def read(self):
        try:
            self.__name=str(input("Enter name: \n"))
            self.__age=int(input("Enter Age \n"))
            self.__place_reg=str(input("Enter Place of Registration \n"))
            self.__place_study=str(input("Enter Place of Study \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Age {} Place of Registration {} Place of Study {}".format(self.__name,self.__age,self.__place_reg,self.__place_study))


if __name__ == "__main__":
    var1 = Citizen()
    var2 = Worker()
    var3 = Schoolchild()
    var1.read()
    var2.read()
    var3.read()
    var1.show()
    var2.show()
    var3.show()
    del(var1)
    del(var2)
    del(var3)