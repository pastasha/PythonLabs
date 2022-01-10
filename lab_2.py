class Brigadir:
    c=0
    __name=""
    __count_buildings=0
    __building=""

    def __init__ (self):
        Brigadir.c+=1
        print(Brigadir.c)

    def __init__ (self,name="",count_buildings=0,building=""):
        Brigadir.c+=1
        print(Brigadir.c)
        try:
            self.__name=name
            self.__count_buildings=count_buildings
            self.__building=building
        except ValueError as e:
            print (e)

    def set_name(self, name):
        self.__name=name

    def set_count_buildings(self, count_buildings):
        self.__count_buildings=count_buildings

    def set_building(self, building):
        self.__building=building

    def get_name(self):
        return self.__name

    def get_count_buildings(self):
        return self.__count_buildings

    def get_building(self):
        return self.__building

    def read(self):
        try:
            self.__name=str(input("Enter name: \n"))
            self.__count_buildings=int(input("Enter Count buildings \n"))
            self.__building=str(input("Enter Building \n"))
        except ValueError:
            print("Error")

    def show(self):
        print("Name {} Count buildings {} Building {}".format(self.__name,self.__count_buildings,self.__building))

if __name__ == "__main__":
    var1 = Brigadir()
    var2 = Brigadir()
    var1.read()
    var2.read()
    var1.show()
    var2.show()
    var3= Brigadir('Man',20,'Shop')
    var3.show()