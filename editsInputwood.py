from PyQt5 import  QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mySQL import database
db = database()

class UI_editsInputwood(QWidget):
    def __init__(self, inputdata , input_id):
        super().__init__()
        self.setWindowTitle("แก้ไขข้อมูล")
        self.setWindowIcon(QIcon('icons/edit.png'))
        self.setGeometry(909, 250, 650, 550)
        strdate = inputdata[0]
        self.dt = tuple([int(x) for x in strdate[:10].split('-')])
        self.inputWooddate = self.dt
        self.inputWoodid = inputdata[1]
        self.inputWoodcode = inputdata[1]
        self.inputWoodtype = inputdata[2]
        self.inputWoodthick = inputdata[3]
        self.inputWoodtwide = inputdata[4]
        self.inputWoodtlong = inputdata[5]
        self.inputWoodquantity = inputdata[6]
        self.inputWoodvolume = inputdata[7]
        self.inputWoodsupplier = inputdata[8]
        self.check = input_id

        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.layout()

# Display
    def display(self):
        # TOP
        self.imgEditInputWood = QLabel()
        self.img = QPixmap('icons/forklift02.png')
        self.imgEditInputWood.setPixmap(self.img)
        self.imgEditInputWood.setAlignment(Qt.AlignCenter)
        self.title_txt = QLabel("แก้ไขข้อมูลรับไม้เข้า")
        self.title_txt.setFont(QFont('Arial', 12))
        self.title_txt.setAlignment(Qt.AlignCenter)

        # Info
        self.dateEditInputWood_txt = QLabel("วันที่รับไม้เข้า: ")
        self.dateEditInputWood = QDateEdit(self)
        self.dateEditInputWood.setDateTime(QtCore.QDateTime(QtCore.QDate(self.inputWooddate[0], self.inputWooddate[1], self.inputWooddate[2])))
        self.dateEditInputWood.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEditInputWood.setDisplayFormat('yyyy-MM-dd')
        self.dateEditInputWood.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEditInputWood.setCalendarPopup(True)
        self.dateEditInputWood.setReadOnly(True)

        # self.woodidEntry = QLineEdit(self)
        # self.woodidEntry.setText(self.inputWoodid)
        # self.woodidEntry.setReadOnly(True)
        self.woodcodeEntry = QLineEdit(self)
        self.woodcodeEntry.setText(self.inputWoodcode)


        self.woodtypeCombobox = QComboBox()
        self.woodtypeCombobox.addItems([str(self.inputWoodtype)])
       # Type
        Type = db.sqlType()
        for data_type in Type:
            self.woodtypeCombobox.addItems([str(data_type)])
        self.woodtypeCombobox.setEditable(True)
        # Thick
        self.thickCombobox = QComboBox()
        self.thickCombobox.addItems([str(self.inputWoodthick)])
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.thickCombobox.addItems([str(data_thick)])
        self.thickCombobox.setEditable(True)

        # Wide
        self.wideCombobox = QComboBox()
        self.wideCombobox.addItem(self.inputWoodtwide)
        Wide = db.sqlWide()
        for data_wide in Wide:
            self.wideCombobox.addItems([str(data_wide)])
        self.wideCombobox.setEditable(True)
        # Longs
        self.longCombobox = QComboBox()
        self.longCombobox.addItem(self.inputWoodtlong)
        Long = db.sqlLong()
        for data_long in Long:
            self.longCombobox.addItems([str(data_long)])
        self.longCombobox.setEditable(True)

        self.woodquantityEntry = QLineEdit(self)
        self.woodquantityEntry.setText(self.inputWoodquantity)
        self.volomeEntry = QLineEdit()
        self.volomeEntry.setText(self.inputWoodvolume)
        self.volomeEntry.setReadOnly(True)
        self.supplierEntry = QLineEdit()
        self.supplierEntry.setText(self.inputWoodsupplier)
        self.supplierEntry.setReadOnly(True)

        # Btn
        self.updateBtn = QPushButton("แก้ไขข้อมูล")
        self.updateBtn.setStyleSheet("""
              QPushButton {
                  background-color: #008CBA;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid #008CBA;
                  color: black;
              }
          """)

        self.updateBtn.clicked.connect(self.funcbtnhandleUpdateInfo)
        self.cancelBtn = QPushButton("ยกเลิก")
        self.cancelBtn.setStyleSheet("""
              QPushButton {
                  background-color: red;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid red;
                  color: black;
              }
          """)

        self.cancelBtn.clicked.connect(self.funcbtnhandleCancelInfo)

# Layout
    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.midLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.btnbox = QHBoxLayout()

        self.text = QWidget()
        self.middleFrame = QGroupBox()
        self.bottomFrame = QFrame()

        # Top
        self.topLayout.addWidget(self.title_txt)
        self.text.setLayout(self.topLayout)

        # Middle
        self.midLayout.addWidget(self.imgEditInputWood)
        self.middleFrame.setLayout(self.midLayout)

        # Bottom
        self.bottomLayout.addRow(QLabel("วันที่รับไม้เข้า: "), self.dateEditInputWood)
        # self.bottomLayout.addRow(QLabel("รหัสไม้: "), self.woodidEntry)
        self.bottomLayout.addRow(QLabel("โค้ดไม้: "), self.woodcodeEntry)
        self.bottomLayout.addRow(QLabel("ประเภทไม้: "), self.woodtypeCombobox)
        self.bottomLayout.addRow(QLabel("หนา: "), self.thickCombobox)
        self.bottomLayout.addRow(QLabel("กว้าง: "), self.wideCombobox)
        self.bottomLayout.addRow(QLabel("ยาว: "), self.longCombobox)
        self.bottomLayout.addRow(QLabel("จำนวน: "), self.woodquantityEntry)
        self.bottomLayout.addRow(QLabel("ปริมาตร: "), self.volomeEntry)
        self.bottomLayout.addRow(QLabel("Supplier: "), self.supplierEntry)
        self.bottomFrame.setLayout(self.bottomLayout)

        # Btn
        self.btnbox.addStretch()
        self.btnbox.addWidget(self.updateBtn)
        self.btnbox.addWidget(self.cancelBtn)

        # All Layout
        self.mainLayout.addWidget(self.text)
        # self.mainLayout.addWidget(self.middleFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.mainLayout.addLayout(self.btnbox)
        self.setLayout(self.mainLayout)

# Update
    def funcbtnhandleUpdateInfo(self):
        check = self.check
        date = self.dateEditInputWood.text()
        # id = self.woodidEntry.text()
        code = self.woodcodeEntry.text()
        g_type = self.get_type()
        g_thick = self.get_thick()
        g_wide = self.get_wide()
        g_long = self.get_long()
        quantity = int(self.woodquantityEntry.text())
        volume = float(self.volomeEntry.text())
        supplier = self.supplierEntry.text()

        check_size = db.size()
        totem = False

        if (g_type == 'Fail' or g_thick == 'Fail' or g_wide == 'Fail' or g_long == 'Fail' ):
            msg = QMessageBox()
            msg.setWindowTitle("แก้ไขข้อมูล")
            msg.setText("ไม่พบฐานข้อมูล กรุณากรอกใหม่อีกครั้งค่ะ")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif (date and code and g_type and g_thick and g_wide and g_long  and quantity and volume and supplier !=""):
            for i in check_size:
                if (g_thick == i[1] and g_wide == i[2] and g_long == i[3]):
                    print(i, ">>", g_thick, "+", g_wide, "+", g_long)
                    db.updatedataInput(check,date,code,g_type,g_thick,g_wide,g_long,quantity,volume,supplier)
                    msg = QMessageBox()
                    msg.setWindowTitle("แก้ไขข้อมูล")
                    msg.setText("ยืนยันการแก้ไขข้อมูล")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    # msg.setDefaultButton(QMessageBox.Ignore)
                    msg.buttonClicked.connect(self.funcbtnhandleCancelInfo)
                    msg.exec_()
                    totem = True
                    break
            if totem == False:
                msg = QMessageBox()
                msg.setWindowTitle("แก้ไขข้อมูล")
                msg.setText("ไม่พบฐานข้อมูล กรุณากรอกใหม่อีกครั้งค่ะ")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

# get_value
    def get_type(self):
        sql_type = db.sqlType()
        mylist = len(sql_type) - 1
        value_type = self.woodtypeCombobox.currentText()
        totem = False
        i = 0
        while True:
            if (value_type  == sql_type[i]):
                return value_type
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return "Fail"

    def get_thick(self):
        sql_thick  = db.sqlThick()
        mylist = len(sql_thick) - 1
        value_thick = int(self.thickCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_thick  == sql_thick[i]):
                return  value_thick
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return "Fail"

    def get_wide(self):
        sql_wide  = db.sqlWide()
        mylist = len(sql_wide) - 1
        value_wide = int(self.wideCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_wide  == sql_wide[i]):
                return  value_wide
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return "Fail"

    def get_long(self):
        sql_long  = db.sqlLong()
        mylist = len(sql_long) - 1
        value_long = int(self.longCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_long  == sql_long[i]):
                return  value_long
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return "Fail"

    def checkSize(self):
       pass

# Cancel
    def funcbtnhandleCancelInfo(self):
        self.close()