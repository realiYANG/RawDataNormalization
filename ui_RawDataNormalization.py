# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RawDataNormalization.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1592, 920)
        MainWindow.setMinimumSize(QtCore.QSize(1592, 920))
        MainWindow.setSizeIncrement(QtCore.QSize(-1, 0))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 10, 841, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 90, 291, 431))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 271, 371))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 6, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 7, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(50, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setObjectName("label_10")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(310, 70, 1261, 791))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(550, 20, 691, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(11, 21, 511, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(554, 21, 681, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(11, 21, 511, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_6.setGeometry(QtCore.QRect(554, 21, 681, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_6.setFont(font)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(11, 21, 511, 731))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_8.setGeometry(QtCore.QRect(554, 21, 681, 731))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_8.setFont(font)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_7.setGeometry(QtCore.QRect(11, 21, 511, 731))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_7.setFont(font)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.originize_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.originize_info_button.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(False)
        font.setWeight(50)
        self.originize_info_button.setFont(font)
        self.originize_info_button.setObjectName("originize_info_button")
        self.save_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_info_button.setGeometry(QtCore.QRect(100, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(False)
        font.setWeight(50)
        self.save_info_button.setFont(font)
        self.save_info_button.setObjectName("save_info_button")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setObjectName("label_15")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 10, 295, 35))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.select_dir_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.select_dir_button.setFont(font)
        self.select_dir_button.setDefault(True)
        self.select_dir_button.setObjectName("select_dir_button")
        self.gridLayout_2.addWidget(self.select_dir_button, 0, 0, 1, 1)
        self.create_dir_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.create_dir_button.setFont(font)
        self.create_dir_button.setDefault(True)
        self.create_dir_button.setObjectName("create_dir_button")
        self.gridLayout_2.addWidget(self.create_dir_button, 0, 1, 1, 1)
        self.open_dir_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_dir_button.setFont(font)
        self.open_dir_button.setDefault(True)
        self.open_dir_button.setObjectName("open_dir_button")
        self.gridLayout_2.addWidget(self.open_dir_button, 0, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 530, 291, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(90, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_24.setTextFormat(QtCore.Qt.PlainText)
        self.label_24.setObjectName("label_24")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 50, 261, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_5.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_5.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_5.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_5.addWidget(self.radioButton_4, 2, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_5.addWidget(self.radioButton_6, 3, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_5.addWidget(self.radioButton_5, 3, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(1290, 10, 251, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_6.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 770, 295, 91))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.refresh_button = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.refresh_button.setFont(font)
        self.refresh_button.setDefault(True)
        self.refresh_button.setFlat(False)
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout_3.addWidget(self.refresh_button, 0, 0, 1, 1)
        self.auto_rename_button = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.auto_rename_button.setFont(font)
        self.auto_rename_button.setAutoDefault(False)
        self.auto_rename_button.setDefault(True)
        self.auto_rename_button.setObjectName("auto_rename_button")
        self.gridLayout_3.addWidget(self.auto_rename_button, 0, 1, 1, 2)
        self.confirm_button = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.confirm_button.setFont(font)
        self.confirm_button.setDefault(True)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout_3.addWidget(self.confirm_button, 0, 3, 1, 1)
        self.generate_file_list_button = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.generate_file_list_button.setFont(font)
        self.generate_file_list_button.setDefault(True)
        self.generate_file_list_button.setObjectName("generate_file_list_button")
        self.gridLayout_3.addWidget(self.generate_file_list_button, 1, 0, 1, 2)
        self.compress_and_rename_button = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.compress_and_rename_button.setFont(font)
        self.compress_and_rename_button.setDefault(True)
        self.compress_and_rename_button.setObjectName("compress_and_rename_button")
        self.gridLayout_3.addWidget(self.compress_and_rename_button, 1, 2, 1, 2)
        self.clear_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_info_button.setGeometry(QtCore.QRect(210, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(False)
        font.setWeight(50)
        self.clear_info_button.setFont(font)
        self.clear_info_button.setObjectName("clear_info_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1592, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "西南分公司测井原始资料文件命名工具"))
        self.label_3.setText(_translate("MainWindow", "测井日期"))
        self.label_5.setText(_translate("MainWindow", "管柱信息"))
        self.label_13.setText(_translate("MainWindow", "接收人"))
        self.label_11.setText(_translate("MainWindow", "作业小队"))
        self.label.setText(_translate("MainWindow", "井名(不含井)"))
        self.label_2.setText(_translate("MainWindow", "测量井段"))
        self.label_4.setText(_translate("MainWindow", "通知单日期"))
        self.label_12.setText(_translate("MainWindow", "移交人"))
        self.label_14.setText(_translate("MainWindow", "测井系列"))
        self.label_10.setText(_translate("MainWindow", "①测井信息补充"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "测井原图"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "刻度文件"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "相关文件"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "原始数据"))
        self.originize_info_button.setText(_translate("MainWindow", "示例信息"))
        self.save_info_button.setText(_translate("MainWindow", "保存到本地"))
        self.label_15.setText(_translate("MainWindow", "文件夹选项："))
        self.select_dir_button.setText(_translate("MainWindow", "③选择"))
        self.create_dir_button.setText(_translate("MainWindow", "④新建"))
        self.open_dir_button.setText(_translate("MainWindow", "⑤打开"))
        self.label_24.setText(_translate("MainWindow", "②项目分类"))
        self.radioButton.setText(_translate("MainWindow", "裸眼常规"))
        self.radioButton_3.setText(_translate("MainWindow", "套损测井"))
        self.radioButton_2.setText(_translate("MainWindow", "裸眼成像"))
        self.radioButton_4.setText(_translate("MainWindow", "生产测井"))
        self.radioButton_6.setText(_translate("MainWindow", "承包商项目"))
        self.radioButton_5.setText(_translate("MainWindow", "固井质量"))
        self.label_17.setText(_translate("MainWindow", "当前测井项目显示："))
        self.refresh_button.setText(_translate("MainWindow", "⑥读取"))
        self.auto_rename_button.setText(_translate("MainWindow", "⑦命名"))
        self.confirm_button.setText(_translate("MainWindow", "⑧确认"))
        self.generate_file_list_button.setText(_translate("MainWindow", "⑨生成数据清单"))
        self.compress_and_rename_button.setText(_translate("MainWindow", "⑩生成压缩包"))
        self.clear_info_button.setText(_translate("MainWindow", "清空补充信息"))
