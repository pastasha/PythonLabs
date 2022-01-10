import mysql.connector
from mysql.connector import Error
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QWidget,QTableWidget, QTableWidgetItem,QMessageBox
from PyQt5.QtCore import QSize, Qt
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        
        self.lbl1 = QLabel('Database', self)
        self.lbl1.setGeometry(10, 0, 150, 30)
        self.lbl2 = QLabel('Name', self)
        self.lbl2.setGeometry(10, 40, 150, 30)
        self.lbl3 = QLabel('Password', self)
        self.lbl3.setGeometry(10, 80, 150, 30)
        self.txtName=QTextEdit(self)
        self.txtName.setGeometry(150, 0,150,30)
        self.txtUser=QTextEdit(self)
        self.txtUser.setGeometry(150, 40,150,30)
        self.txtPassword=QTextEdit(self)
        self.txtPassword.setGeometry(150, 80,150,30) 
        self.but1 = QPushButton('Login ', self)
        self.but1.setGeometry(50, 120, 200, 30)
        self.but1.clicked.connect(self.login)

    def login(self):
        name1=self.txtName.toPlainText()
        user1=self.txtUser.toPlainText()
        password1=self.txtPassword.toPlainText()
        
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=name1,
                user=user1,
                password=password1)
            if conn.is_connected: 
                self.window=Window1([name1,user1,password1])
                self.window.show()
                self.close()
        except Error as e:
            ms=QMessageBox()
            ms.setWindowTitle("Error")
            ms.setText(str(e))
            ms.exec()
        
class Window1(QMainWindow):
    def __init__(self,connects):
        super().__init__()
        self.resize(700, 250)
        self.connects=connects
        self.lbl1 = QLabel('Name', self)
        self.lbl1.setGeometry(10, 0, 150, 30)
        self.lbl2 = QLabel('Age', self)
        self.lbl2.setGeometry(10, 40, 150, 30)
        self.lbl3 = QLabel('Place of Registration', self)
        self.lbl3.setGeometry(10, 80, 150, 30)
        self.txtName=QTextEdit(self)
        self.txtName.setGeometry(150, 0,150,30)
        self.txtAge=QTextEdit(self)
        self.txtAge.setGeometry(150, 40,150,30)
        self.txtPlace=QTextEdit(self)
        self.txtPlace.setGeometry(150, 80,150,30) 
        self.but1 = QPushButton('add ', self)
        self.but1.setGeometry(50, 120, 200, 30)
        self.but1.clicked.connect(self.add)
        self.but2 = QPushButton('Show ', self)
        self.but2.setGeometry(50, 160, 200, 30)
        self.but2.clicked.connect(self.showw)
        self.but2 = QPushButton('Delete ', self)
        self.but2.setGeometry(50, 200, 200, 30)
        self.but2.clicked.connect(self.delete)
    
        self.table = QTableWidget(self) 
        self.table.setColumnCount(4)   
        self.table.setHorizontalHeaderLabels(["Id", "Name", "Age","Place of Registration"])
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.table.setGeometry(300,0, 500, 250)
        self.table.resizeColumnsToContents()

        self.showw()
       
        
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
                val = (self.txtName.toPlainText(), self.txtAge.toPlainText(),self.txtPlace.toPlainText())
                mycursor.execute(sql, val)
            conn.commit()
            self.showw()
        except Error as e:
            ms=QMessageBox()
            ms.setWindowTitle("Error")
            ms.setText(str(e))
            ms.exec()

    def delete(self):
        if self.table.currentRow()==-1:
            return
        item = self.table.item(self.table.currentRow(), 0);
        try:
            conn=mysql.connector.connect(
                host='localhost',
                database=self.connects[0],
                user=self.connects[1],
                password=self.connects[2])
            if conn.is_connected: 
                mycursor = conn.cursor()
                sql = "DELETE FROM citizens WHERE id={}".format(item.text())
                mycursor.execute(sql)
            conn.commit()
            self.showw()
        except Error as e:
            ms=QMessageBox()
            ms.setWindowTitle("Error")
            ms.setText(str(e))
            ms.exec()

            
    def showw(self):
        self.table.setRowCount(0);
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
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    self.table.setItem(rowPosition , 0, QTableWidgetItem(str(x[0])))
                    self.table.setItem(rowPosition , 1, QTableWidgetItem(x[1]))
                    self.table.setItem(rowPosition , 2, QTableWidgetItem(x[2]))
                    self.table.setItem(rowPosition , 3, QTableWidgetItem(x[3]))                
        except Error as e:
            ms=QMessageBox()
            ms.setWindowTitle("Error")
            ms.setText(str(e))
            ms.exec()

if __name__ == "__main__":
    app = QApplication([])
    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
