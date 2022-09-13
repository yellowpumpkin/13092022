from PyQt5 import QtCore , QtWidgets
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import *

import resizeWood
import inputWood
import withdrawWood
import saleWood
import main
import cuttingWood

class  UI_Heatwood (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heat")
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.display()
        self.displayTable()
        self.layouts()
        self.funcFetchDataHeatWood()

# Tool Bar
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # ตัดไม้
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # แปลงไม้
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.addResize.triggered.connect(self.funcResize)
        self.tb.addSeparator()
        # อบไม้
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()
        # ขาย
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()

# Display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget((self.wg))

        self.dateText = QLabel("วันที่รับไม้เข้า : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        self.succeed = QRadioButton(" เรียบร้อย ")
        self.inprogress = QRadioButton(" กำลังอบ ")
        self.all = QRadioButton(" ทั้งหมด ")

# Table
    def displayTable(self):
        self.heatTable = QTableWidget()

        self.heatTable.setColumnCount(9)
        self.heatTable.setHorizontalHeaderItem(0, QTableWidgetItem("โค๊ดไม้"))
        self.heatTable.setHorizontalHeaderItem(1, QTableWidgetItem("หนา"))
        self.heatTable.setHorizontalHeaderItem(2, QTableWidgetItem("กว้าง"))
        self.heatTable.setHorizontalHeaderItem(3, QTableWidgetItem("ยาว"))
        self.heatTable.setHorizontalHeaderItem(4, QTableWidgetItem("ปริมาตร(m^3) "))
        self.heatTable.setHorizontalHeaderItem(5, QTableWidgetItem("จำนวนเบิก"))
        self.heatTable.setHorizontalHeaderItem(6, QTableWidgetItem("วันที่เบิก"))
        self.heatTable.setHorizontalHeaderItem(7, QTableWidgetItem("สถานะ"))
        self.heatTable.setHorizontalHeaderItem(8, QTableWidgetItem("จัดการ"))
        self.heatTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

# Layouts
    def layouts(self):

        self.mainLayout = QVBoxLayout()
        self.mainLeftLayout = QHBoxLayout()
        self.mainRightLayout = QHBoxLayout()
        self.rightTopLayout = QVBoxLayout()
        self.rightMiddleLayout = QVBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()

        self.sizeGropBox = QGroupBox("Search")
        self.statusGropBox = QGroupBox("Status")

        # Left Top
        self.leftTopLayout.addWidget(self.dateText)
        self.leftTopLayout.addWidget(self.date)
        self.sizeGropBox.setLayout(self.leftTopLayout)

        self.rightTopLayout.addWidget(self.succeed)
        self.rightTopLayout.addWidget(self.inprogress)
        self.rightTopLayout.addWidget(self.all)
        self.statusGropBox.setLayout(self.rightTopLayout)

        # Table
        self.mainLeftLayout.addWidget(self.heatTable)

        # All Layout
        self.mainRightLayout.addWidget(self.sizeGropBox)
        self.mainRightLayout.addWidget(self.statusGropBox)
        self.mainLayout.addLayout(self.mainRightLayout)
        self.mainLayout.addLayout(self.mainLeftLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

# Display
    def funcFetchDataHeatWood(self):
        pass
        # for i in reversed(range(self.heatTable.rowCount())):
        #     self.heatTable.removeRow(i)
        # query = db.dataTableHeat()
        # for row_data in query:
        #     row_number = self.heatTable.rowCount()
        #     self.heatTable.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.heatTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        #     self.btn_edit = QPushButton('Edit')
        #     self.btn_edit.setStyleSheet("""
        #                 QPushButton {
        #                     color:  black;
        #                     border-style: solid;
        #                     border-width: 3px;
        #                     border-color:  #008CBA;
        #                     border-radius: 12px
        #                 }
        #                 QPushButton:hover{
        #                     background-color: #008CBA;
        #                     color: white;
        #                 }
        #             """)
        #     # self.btn_edit.clicked.connect()
        #     self.heatTable.setCellWidget(row_number, 8, self.btn_edit)
        # self.heatTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


# Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

# Function Input
    def funcInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

# Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.close()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

# Function Heat
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()

# Function Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()

# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Heatwood()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#    main()