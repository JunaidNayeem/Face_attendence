# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:12:49 2020

@author: AI & ML
"""


from PyQt5 import  QtWidgets,uic,QtGui
import sqlite3 as sql
from datetime import datetime,timedelta


from dbms import Student,Employee


def gotostudentlogin():
    homePage.close()
    studentLoginPage.show()

def gotofacultylogin():
    homePage.close()
    facultyLoginPage.phoneEnter.setText('')
    facultyLoginPage.passwordEnter.setText('')
    facultyLoginPage.show()
def gotoadminlogin():
    homePage.close()
    adminLogin.show()
    

def backfromfaclogin():
    facultyLoginPage.close()
    homePage.show()

def backfromstudentlogin():
    studentLoginPage.close()
    homePage.show()
def backfromadminLogin():
    adminLogin.close()
    homePage.show()
    
def gotoadmindashboard():
    name=adminLogin.N.text()
    passwrd=adminLogin.PASS.text()
    
    e=Employee()
    ret=e.fetch_faculty(name,passwrd)
    
    if ret['Etype']=='Admin':
         adminLogin.close()
         admin.show()
    else:
        adminLogin.N.setText('')
        adminLogin.PASS.setText('')
def adminAdd():
    admin.close()
    add.show()
def addFac():
    frid=add.rid.text()
    frname=add.rname.text()
    frphone=add.rphone.text()
    frpass=add.rpass.text()
    frtype=add.rtype.text()
    e=Employee()
    
    e.register_faculty(frid,frname,frphone,frpass,frtype)
    add.close()
    admin.show()
def backfromadd():
    add.close()
    admin.show()

def adminRemove():
    admin.close()
    remove.show()
def removeFac():
    frid=remove.rid.text()
    frtype=remove.rtype.text()
    if frtype=='Admin':
        remove.close()
        admin.show()

    e=Employee()
    e.remove_faculty(frid) 
    remove.close()
    admin.show()
def backfromremove():
    remove.close()
    admin.show()

    
def gotoemployeedashboard():
    
    Ephone = facultyLoginPage.phoneEnter.text()
    Epassword = facultyLoginPage.passwordEnter.text()
    
    e = Employee()
    ret = e.fetch_faculty(Ephone,Epassword)
    
    if ret['Etype']=='Faculty':
        facultyLoginPage.close()
        facultyDashboard.show()
    else:
        facultyLoginPage.phoneEnter.setText('')
        facultyLoginPage.passwordEnter.setText('')

def backtofacultylogin():
    facultyLoginPage.phoneEnter.setText('')
    facultyLoginPage.passwordEnter.setText('')
    facultyDashboard.close()
    facultyLoginPage.show()


def gotostudentregister():
    facultyDashboard.close()
    studentRegisterPage.show()

def backfromstudentregister():
    studentRegisterPage.close()
    facultyDashboard.show()
def backfromadminlogin():
    adminLogin.close()
    homePage.show()
def backfromAdmin():
    admin.close()
    adminLogin.show()
    

    
def capturedata():
    
    Sid = studentRegisterPage.rollEnter.text()
    Sname = studentRegisterPage.nameEnter.text()
    Sclass_id = studentRegisterPage.classEnter.text()
    Sphone_no = studentRegisterPage.phoneEnter.text()
    Spassword = studentRegisterPage.passwordEnter.text()
    URL = studentRegisterPage.urlEnter.text()
    s = Student()
    s.register(URL, Sid, Sname, Sclass_id, Sphone_no, Spassword)

    
    

class student_gui:
    
    def gotostudentdashboard(self):
        
        phone = studentLoginPage.phoneEnter.text()
        password = studentLoginPage.passwordEnter.text()
        
        s = Student()
        ret = s.fetch_student(phone,password)
        if ret is not False:        
            studentLoginPage.close()
            studentDashboard.welcomeLabel.setText('Welcome '+ret['Sname'])
            self.logged_in_id = ret["Sid"]
            self.logged_in_name = ret["Sname"]
            studentDashboard.show()
        else:
            studentLoginPage.phoneEnter.setText("")
            studentLoginPage.passwordEnter.setText("")
            
    def viewattendence(self):
        start = datetime.strptime(studentDashboard.startDate.text(),"%d-%m-%Y").strftime("%d-%m-%y")
        stop = datetime.strptime(studentDashboard.endDate.text(),"%d-%m-%Y").strftime("%d-%m-%y")
        s = Student()
        df = s.fetch_student_attendence(self.logged_in_id,start,stop)
        viewAttendence.tableWidget.setRowCount(0) # initially no rows in table
        
        viewAttendence.tableWidget.setColumnCount(len(df.keys())) # add number of columns as per the df
        viewAttendence.tableWidget.setHorizontalHeaderLabels(df.keys()) # put their labels
        for i in range(len(list(df.keys()))):
            # insert the data as row items
            row_num = 0
            for data in df[list(df.keys())[i]]:
                if i == 0:
                    viewAttendence.tableWidget.insertRow(viewAttendence.tableWidget.rowCount())
                    row_num = viewAttendence.tableWidget.rowCount()-1
                viewAttendence.tableWidget.setItem(row_num , i, QtWidgets.QTableWidgetItem(str(data)))
                if str(data)=="A":
                    item1 = QtWidgets.QTableWidgetItem()
                    item1.setBackground(QtGui.QColor(255, 153, 153))
                    item1.setText("A")
                    viewAttendence.tableWidget.setItem(row_num, i ,item1)
                elif str(data)=="P":
                    item1 = QtWidgets.QTableWidgetItem()
                    item1.setBackground(QtGui.QColor(187, 255, 153))
                    item1.setText("P")
                    viewAttendence.tableWidget.setItem(row_num, i ,item1)
                row_num += 1
                
        viewAttendence.show()
    
    def studentlogout(self):
        self.logged_in_id = None
        self.logged_in_name = None
        studentDashboard.close()
        studentLoginPage.show()
 
    
app = QtWidgets.QApplication([])

homePage = uic.loadUi('Uifiles/FrontPage.ui')
studentLoginPage = uic.loadUi('Uifiles/student_login.ui')
facultyLoginPage = uic.loadUi("Uifiles/faculty_login.ui")
facultyDashboard = uic.loadUi("Uifiles/faculty_dashboard.ui")
studentRegisterPage = uic.loadUi("Uifiles/student_register.ui")
studentDashboard = uic.loadUi("Uifiles/studentDashboard.ui")
viewAttendence = uic.loadUi('Uifiles/view_attendence.ui')
adminLogin=uic.loadUi("UiFiles/admin_login.ui")
admin=uic.loadUi("UiFiles/admin.ui")
add=uic.loadUi('UiFiles/addFaculty.ui')
remove=uic.loadUi('UiFiles/removeFaculty.ui')
 




sgui = student_gui()

homePage.show()
homePage.studentLoginBut.clicked.connect(gotostudentlogin)
homePage.facultyLoginBut.clicked.connect(gotofacultylogin)
homePage.adminLoginBut.clicked.connect(gotoadminlogin)


adminLogin.admin_loginBut.clicked.connect(gotoadmindashboard)
adminLogin.adminBackBt.clicked.connect(backfromadminLogin)

admin.back.clicked.connect(backfromAdmin)
admin.adf.clicked.connect(adminAdd)
admin.rmf.clicked.connect(adminRemove)
add.b.clicked.connect(addFac)
add.addBack.clicked.connect(backfromadd)
remove.R.clicked.connect(removeFac)
remove.removeback.clicked.connect(backfromremove)


facultyLoginPage.backBut.clicked.connect(backfromfaclogin)
facultyLoginPage.loginBut.clicked.connect(gotoemployeedashboard)


studentLoginPage.backBut.clicked.connect(backfromstudentlogin)
studentLoginPage.loginBut.clicked.connect(sgui.gotostudentdashboard)

studentDashboard.logoutBut.clicked.connect(sgui.studentlogout)
studentDashboard.viewBut.clicked.connect(sgui.viewattendence)

facultyDashboard.backBut.clicked.connect(backtofacultylogin)
facultyDashboard.registerStudentBut.clicked.connect(gotostudentregister)
facultyDashboard.viewAttendenceBut.clicked.connect(gotostudentlogin)


studentRegisterPage.backBut.clicked.connect(backfromstudentregister)
studentRegisterPage.captureBut.clicked.connect(capturedata)

app.exec()

del app