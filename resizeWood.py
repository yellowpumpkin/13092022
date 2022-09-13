
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import heatWood
import inputWood
import withdrawWood
import saleWood
import cuttingWood
import main

class  UI_Resizewood (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resize")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450, 50,1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.display()
        self.displayTable()
        self.layouts()

#Tool Bar
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
        # Cutting
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.tb.addSeparator()
        # Heat
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.addHeat.triggered.connect(self.funcHeat)
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()
        # Sale
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()

# Display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget((self.wg))
        self.resizeText = QLabel("resize windowwwwwwwwwwwwww")

# Table
    def displayTable(self):
        self.resizeTable = QTableWidget()
        self.resizeTable.setRowCount(100)
        self.resizeTable.setColumnCount(9)
        self.resizeTable.setHorizontalHeaderItem(0,QTableWidgetItem("Wood ID"))
        self.resizeTable.setHorizontalHeaderItem(1, QTableWidgetItem("Code"))
        self.resizeTable.setHorizontalHeaderItem(2, QTableWidgetItem("Type"))
        self.resizeTable.setHorizontalHeaderItem(3, QTableWidgetItem("Thick"))
        self.resizeTable.setHorizontalHeaderItem(4, QTableWidgetItem("Wide"))
        self.resizeTable.setHorizontalHeaderItem(5, QTableWidgetItem("Long"))
        self.resizeTable.setHorizontalHeaderItem(6, QTableWidgetItem("Pack"))
        self.resizeTable.setHorizontalHeaderItem(7, QTableWidgetItem("Quantity/Pack"))
        self.resizeTable.setHorizontalHeaderItem(8, QTableWidgetItem("Active"))

        self.resizeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

# Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.middleTopLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()
        self.sizeGropBox = QGroupBox("")

        #
        self.leftTopLayout.addWidget(self.resizeText)
        self.sizeGropBox.setLayout(self.leftTopLayout)

        # Table
        self.mainTableLayout.addWidget(self.resizeTable)

        # All Layout
        self.leftTopLayout.addWidget(self.sizeGropBox)
        self.mainLayout.addLayout(self.leftTopLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

# Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

# Function AddProduct
    def funcInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

# Function Cut
    def funcCut (self):
        self.newCut=cuttingWood.UI_Cutwood()
        self.close()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

# Function Heat
    def funcHeat(self):
        self.newHeat=heatWood.UI_Heatwood()
        self.close()

# Function Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()

# Main
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Resizewood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()
