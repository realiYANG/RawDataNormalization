import os
import shutil
import math
import os

from PyQt5.QtCore import Qt
from docxtpl import DocxTemplate
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QTextEdit, \
    QHBoxLayout, QMainWindow, QMessageBox, QComboBox, QTreeWidgetItem, QDialog, QDialogButtonBox, QTreeWidget
from pypinyin import pinyin, Style
from tqdm import tqdm

from CLASSES.DialogClass_裸眼常规_测井原图 import Dialog_裸眼常规_测井原图
from CLASSES.DialogClass_裸眼成像_测井原图 import Dialog_裸眼成像_测井原图
from CLASSES.DialogClass_套损检测_测井原图 import Dialog_套损检测_测井原图
from CLASSES.DialogClass_生产测井_测井原图 import Dialog_生产测井_测井原图
from CLASSES.DialogClass_固井质量_测井原图 import Dialog_固井质量_测井原图
from CLASSES.DialogClass_承包商测井_测井原图 import Dialog_承包商测井_测井原图

from CLASSES.DialogClass_裸眼常规_原始数据 import Dialog_裸眼常规_原始数据
from CLASSES.DialogClass_裸眼成像_原始数据 import Dialog_裸眼成像_原始数据
from CLASSES.DialogClass_套损检测_原始数据 import Dialog_套损检测_原始数据
from CLASSES.DialogClass_生产测井_原始数据 import Dialog_生产测井_原始数据
from CLASSES.DialogClass_固井质量_原始数据 import Dialog_固井质量_原始数据
from CLASSES.DialogClass_承包商测井_原始数据 import Dialog_承包商测井_原始数据
from ui_RawDataNormalization import Ui_MainWindow
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.setupUi(self)
        self.statusBar().showMessage('中油测井')
        self.initUI()

    def initUI(self):
        # 利用本地文件初始化信息
        info_data = {}
        with open('.\\tempFiles\\info.txt', 'r', encoding='GBK', errors='replace') as file:
            for line in file:
                line = line.strip()  # 去除行首尾的空白字符
                if line:
                    key, value = line.split('=')
                    info_data[key] = value

        self.lineEdit.setText(info_data['井名'])
        self.lineEdit_2.setText(info_data['测量井段'])
        self.lineEdit_3.setText(info_data['测井日期'])
        self.lineEdit_4.setText(info_data['通知单日期'])
        self.lineEdit_5.setText(info_data['管柱信息'])
        self.lineEdit_7.setText(info_data['测井小队'])
        self.lineEdit_8.setText(info_data['测井系列'])
        self.lineEdit_9.setText(info_data['移交人'])
        self.lineEdit_10.setText(info_data['接收人'])

        # # 全局变量
        # self.well_name = self.lineEdit.text()
        # self.measure_interval = self.lineEdit_2.text()
        # self.logging_date = self.lineEdit_3.text()
        # self.inform_sheet_date = self.lineEdit_4.text()
        # self.casing_info = self.lineEdit_5.text()
        # self.logging_team = self.lineEdit_7.text()
        # self.logging_series = self.lineEdit_8.text()
        # self.transferor = self.lineEdit_9.text()
        # self.reciever = self.lineEdit_10.text()

        # 获取当前工作目录
        current_directory = os.getcwd() + '\\' + self.lineEdit.text()
        self.lineEdit_6.setText(current_directory)

        # 初始化表格控件列数
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["测井原图的原文件名"])
        self.tableWidget.setColumnWidth(0, 500)

        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setHorizontalHeaderLabels(["测井原图的新文件名"])
        self.tableWidget_2.setColumnWidth(0, 500)

        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setHorizontalHeaderLabels(["刻度文件的原文件名"])
        self.tableWidget_3.setColumnWidth(0, 500)

        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setHorizontalHeaderLabels(["刻度文件的新文件名"])
        self.tableWidget_4.setColumnWidth(0, 500)

        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setHorizontalHeaderLabels(["相关文件的原文件名"])
        self.tableWidget_5.setColumnWidth(0, 500)

        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setHorizontalHeaderLabels(["相关文件的新文件名"])
        self.tableWidget_6.setColumnWidth(0, 500)

        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setHorizontalHeaderLabels(["原始数据的原文件名"])
        self.tableWidget_7.setColumnWidth(0, 500)

        self.tableWidget_8.setColumnCount(1)
        self.tableWidget_8.setHorizontalHeaderLabels(["原始数据的新文件名"])
        self.tableWidget_8.setColumnWidth(0, 500)

        # 信号与槽函数的连接
        self.lineEdit.textChanged.connect(self.on_linEdit_changed)
        self.originize_info_button.clicked.connect(self.originize_info)
        self.save_info_button.clicked.connect(self.save_info)
        self.clear_info_button.clicked.connect(self.clear_info)
        self.select_dir_button.clicked.connect(self.select_directory)
        self.create_dir_button.clicked.connect(self.create_directory)
        self.open_dir_button.clicked.connect(self.open_directory)
        self.refresh_button.clicked.connect(self.refresh_file_lists)
        self.auto_rename_button.clicked.connect(self.auto_rename)
        self.confirm_button.clicked.connect(self.confirm_rename)
        self.generate_file_list_button.clicked.connect(self.generate_file_list_docx)
        self.compress_and_rename_button.clicked.connect(self.compress_and_rename)

    def originize_info(self):
        self.lineEdit.setText('泸203H1-1')
        self.lineEdit_2.setText('1000-3000')
        self.lineEdit_3.setText('20240105')
        self.lineEdit_4.setText('20240101')
        self.lineEdit_5.setText('114.3mm套')
        self.lineEdit_7.setText('C2397')
        self.lineEdit_8.setText('Sondex')
        self.lineEdit_9.setText('宋超')
        self.lineEdit_10.setText('李海军')

    def clear_info(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')

    def save_info(self):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()
        DICT = {
            '井名': well_name,
            '测量井段': measure_interval,
            '测井日期': logging_date,
            '通知单日期': inform_sheet_date,
            '管柱信息': casing_info,
            '测井小队': logging_team,
            '测井系列': logging_series,
            '移交人': transferor,
            '接收人': reciever
        }

        # 打开文件以写入数据
        with open('.\\tempFiles\\info.txt', 'w') as file:
            for key, value in DICT.items():
                file.write(f"{key}={value}\n")
        # 弹出提示框
        QMessageBox.information(None, '提示', '已保存到本地')

    def on_linEdit_changed(self):
        # 获取当前工作目录
        current_directory = os.getcwd() + '\\' + self.lineEdit.text()
        self.lineEdit_6.setText(current_directory)
        if '井' in self.lineEdit.text():
            # 弹出提示框
            QMessageBox.information(None, '提示', '井名中不能带井字')
        else:
            pass

    def select_directory(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        self.lineEdit_6.setText(folder_path)
        # fnames = QFileDialog.getOpenFileNames(self, '打开文件', './')  # 注意这里返回值是元组
        # if fnames[0]:
        #     for fname in fnames[0]:
        #         self.lineEdit_6.setText(fname)

    def create_directory(self):
        if self.lineEdit.text() not in self.lineEdit_6.text():
            folder_path = self.lineEdit_6.text() + '\\' + self.lineEdit.text()
            self.lineEdit_6.setText(folder_path)
        else:
            folder_path = self.lineEdit_6.text()
            self.lineEdit_6.setText(folder_path)

        if folder_path != '':
            folders = ['测井原图', '刻度文件', '相关文件', '原始数据']
            for folder in folders:
                folder_path_to_create = os.path.join(folder_path, folder)
                if not os.path.exists(folder_path_to_create):
                    os.makedirs(folder_path_to_create)
                    print(f"已创建文件夹：{folder_path_to_create}")
                else:
                    print(f"文件夹已存在：{folder_path_to_create}")
            QMessageBox.information(None, "信息", "已新建")
        else:
            # 创建信息框
            QMessageBox.warning(None, "警告", "是否没有选定文件夹?")

    def open_directory(self):
        folder_path = self.lineEdit_6.text()
        if folder_path != '':
            try:
                os.startfile(folder_path)
            except FileNotFoundError as e:
                print(f"错误：{e}")
        else:
            # 创建信息框
            QMessageBox.warning(None, "警告", "是否没有选定文件夹?")

    def set_children_check_state(self, item, check_state):
        # 设置当前节点的复选框状态
        item.setCheckState(0, check_state)
        # 遍历所有子节点
        for i in range(item.childCount()):
            child = item.child(i)
            # 递归设置子节点的复选框状态
            self.set_children_check_state(child, check_state)

    def refresh_file_lists(self):
        folder_path = self.lineEdit_6.text()
        if not os.path.exists(folder_path):
            # 创建信息框
            QMessageBox.warning(None, "警告", "当前路径不存在，需要新建文件夹")
        else:
            folder_path_测井原图 = folder_path + '/测井原图'
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(["原文件名"])
            for file_or_folder in os.listdir(folder_path_测井原图):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                # print(self.tableWidget.rowCount())
                item = QtWidgets.QTableWidgetItem(file_or_folder)
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, item)

            folder_path_刻度文件 = folder_path + '/刻度文件'
            self.tableWidget_3.clear()
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.setHorizontalHeaderLabels(["原文件名"])
            for file_or_folder in os.listdir(folder_path_刻度文件):
                self.tableWidget_3.insertRow(self.tableWidget_3.rowCount())
                item = QtWidgets.QTableWidgetItem(file_or_folder)
                self.tableWidget_3.setItem(self.tableWidget_3.rowCount() - 1, 0, item)

            folder_path_相关文件 = folder_path + '/相关文件'
            self.tableWidget_5.clear()
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.setHorizontalHeaderLabels(["原文件名"])
            for file_or_folder in os.listdir(folder_path_相关文件):
                self.tableWidget_5.insertRow(self.tableWidget_5.rowCount())
                item = QtWidgets.QTableWidgetItem(file_or_folder)
                self.tableWidget_5.setItem(self.tableWidget_5.rowCount() - 1, 0, item)

            folder_path_原始数据 = folder_path + '/原始数据'
            self.tableWidget_7.clear()
            self.tableWidget_7.setRowCount(0)
            self.tableWidget_7.setHorizontalHeaderLabels(["原文件名"])
            for file_or_folder in os.listdir(folder_path_原始数据):
                self.tableWidget_7.insertRow(self.tableWidget_7.rowCount())
                item = QtWidgets.QTableWidgetItem(file_or_folder)
                self.tableWidget_7.setItem(self.tableWidget_7.rowCount() - 1, 0, item)

    def extract_hanzi_and_convert_to_pinyin(self, text):
        hanzi_list = []
        for char in text:
            if '\u4e00' <= char <= '\u9fff':  # 判断字符是否为汉字
                hanzi_list.append(char)
        hanzi_text = ''.join(hanzi_list)
        pinyin_list = pinyin(hanzi_text, style=Style.NORMAL)
        pinyin_str = ''.join([item[0] for item in pinyin_list])
        return pinyin_str

    def auto_rename(self):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()

        # 测井原图
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(["新文件名", "类型"])
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
            old_name = self.tableWidget.item(i, 0).text()
            # TODO
            combo_box = QComboBox()
            combo_box.addItems([" ", "主测", "重复", "主测+重复", "验证", "对比", "上测", "下测", "上测+下测"])
            combo_box.currentIndexChanged.connect(self.handle_selection_cejingyuantu)
            self.tableWidget_2.setCellWidget(i, 1, combo_box)

            new_name = old_name.replace(' ', '').replace(well_name + '井', well_name)
            new_name = new_name.replace('（', '(').replace('）', ')')
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(i, 0, item)

        # 刻度文件
        self.tableWidget_4.clear()
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setHorizontalHeaderLabels(["新文件名", "类型"])
        for i in range(self.tableWidget_3.rowCount()):
            self.tableWidget_4.insertRow(self.tableWidget_4.rowCount())
            old_name = self.tableWidget_3.item(i, 0).text()
            new_name = old_name.replace(' ', '').replace(well_name + '井', well_name)
            new_name = new_name.replace('（', '(').replace('）', ')')
            if '20' not in new_name:
                new_name = new_name + '_' + logging_date
            pinyin_result1 = self.extract_hanzi_and_convert_to_pinyin(well_name)
            # print(pinyin_result1)
            pinyin_result2 = self.extract_hanzi_and_convert_to_pinyin(new_name)
            # print(pinyin_result2)
            if pinyin_result1 not in pinyin_result2:
                new_name = well_name + '_' + new_name
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_4.setItem(i, 0, item)

        # 相关文件
        self.tableWidget_6.clear()
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setHorizontalHeaderLabels(["新文件名", "类型"])
        for i in range(self.tableWidget_5.rowCount()):
            self.tableWidget_6.insertRow(self.tableWidget_6.rowCount())
            old_name = self.tableWidget_5.item(i, 0).text()
            # TODO
            combo_box = QComboBox()
            combo_box.addItems([" ", "通知单", "计划书", "收集登记表", "验收记录表", "已自动命名"])
            combo_box.currentIndexChanged.connect(self.handle_selection_xiangguanwenjian)
            self.tableWidget_6.setCellWidget(i, 1, combo_box)

            new_name = old_name.replace(' ', '').replace(well_name + '井', well_name).replace(well_name + '_',
                                                                                              well_name)
            new_name = new_name.replace('（', '(').replace('）', ')')
            if '通知单' in new_name:
                old_name = self.tableWidget_5.item(i, 0).text()
                new_name = well_name + '测井通知单' + '_' + inform_sheet_date + '.' + old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_6.setItem(i, 0, item)
                # self.tableWidget_6.removeCellWidget(i, 1)
                # item = QtWidgets.QTableWidgetItem('通知单已命名')
                # self.tableWidget_6.setItem(i, 1, item)
                combo_box.setCurrentIndex(5)
            elif '计划书' in new_name:
                old_name = self.tableWidget_5.item(i, 0).text()
                new_name = well_name + 'QHSE测井作业计划书' + '_' + logging_date + '.' + old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_6.setItem(i, 0, item)
                # self.tableWidget_6.removeCellWidget(i, 1)
                # item = QtWidgets.QTableWidgetItem('通知单已命名')
                # self.tableWidget_6.setItem(i, 1, item)
                combo_box.setCurrentIndex(5)
            elif '资料收集' in new_name:
                old_name = self.tableWidget_5.item(i, 0).text()
                new_name = well_name + '原始资料收集登记表' + '_' + logging_date + '.' + old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_6.setItem(i, 0, item)
                # self.tableWidget_6.removeCellWidget(i, 1)
                # item = QtWidgets.QTableWidgetItem('通知单已命名')
                # self.tableWidget_6.setItem(i, 1, item)
                combo_box.setCurrentIndex(5)
            elif '资料验收' in new_name:
                old_name = self.tableWidget_5.item(i, 0).text()
                new_name = well_name + '测井资料验收记录表' + '_' + logging_date + '.' + old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_6.setItem(i, 0, item)
                # self.tableWidget_6.removeCellWidget(i, 1)
                # item = QtWidgets.QTableWidgetItem('通知单已命名')
                # self.tableWidget_6.setItem(i, 1, item)
                combo_box.setCurrentIndex(5)
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_6.setItem(i, 0, item)

        # 原始数据
        self.tableWidget_8.clear()
        self.tableWidget_8.setColumnCount(2)
        self.tableWidget_8.setHorizontalHeaderLabels(["新文件名", "类型"])
        for i in range(self.tableWidget_7.rowCount()):
            self.tableWidget_8.insertRow(self.tableWidget_8.rowCount())
            old_name = self.tableWidget_7.item(i, 0).text()
            # TODO
            combo_box = QComboBox()
            combo_box.addItems([" ", "主测", "重复", "主测+重复", "验证", "对比", "上测", "下测", "上测+下测"])
            combo_box.currentIndexChanged.connect(self.handle_selection_yuanshishuju)
            self.tableWidget_8.setCellWidget(i, 1, combo_box)

            new_name = old_name.replace(' ', '').replace(well_name + '井', well_name)
            new_name = new_name.replace('（', '(').replace('）', ')')
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_8.setItem(i, 0, item)

    def handle_selection_cejingyuantu(self, index):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()

        if index == 1:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)

        elif index == 2:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 3:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 4:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 5:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 6:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 7:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        elif index == 8:
            combo_box = self.sender()
            row = self.tableWidget_2.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_测井原图(self)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_测井原图(self)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_测井原图(self)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_测井原图(self)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_测井原图(self)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_测井原图(self)

            if dialog.exec_() == QDialog.Accepted:
                lst = []
                with open('.\\tempFiles\\save.txt', 'r') as file:
                    for line in file:
                        lst.append(line.strip())
                lst = list(set(lst))
                selected_items_text = '+'.join(lst)
                self.lineEdit_11.setText(selected_items_text)

            new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '.' + \
                       old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_2.setItem(row, 0, item)
            # self.tableWidget_2.removeCellWidget(row, 1)
        else:
            pass

    def handle_selection_keduwenjian(self, index):
        pass

    def handle_selection_xiangguanwenjian(self, index):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()

        if index == 1:
            combo_box = self.sender()
            row = self.tableWidget_6.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_5.item(row, 0).text()
            new_name = well_name + '测井通知单' + '_' + inform_sheet_date + '.' + old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_6.setItem(row, 0, item)
            # self.tableWidget_6.removeCellWidget(row, 1)
        elif index == 2:
            combo_box = self.sender()
            row = self.tableWidget_6.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_5.item(row, 0).text()
            new_name = well_name + 'QHSE测井作业计划书' + '_' + logging_date + '.' + old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_6.setItem(row, 0, item)
            # self.tableWidget_6.removeCellWidget(row, 1)
        elif index == 3:
            combo_box = self.sender()
            row = self.tableWidget_6.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_5.item(row, 0).text()
            new_name = well_name + '原始资料收集登记表' + '_' + logging_date + '.' + old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_6.setItem(row, 0, item)
            # self.tableWidget_6.removeCellWidget(row, 1)
        elif index == 4:
            combo_box = self.sender()
            row = self.tableWidget_6.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_5.item(row, 0).text()
            new_name = well_name + '测井资料验收记录表' + '_' + logging_date + '.' + old_name.split('.')[-1]
            item = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget_6.setItem(row, 0, item)
            # self.tableWidget_6.removeCellWidget(row, 1)
        else:
            pass

    def handle_selection_yuanshishuju(self, index):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()

        if index == 1:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                new_name = new_name.replace('_VDL', '')  # 常规VDL不需要后缀
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 2:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 3:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '主测+重复' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 4:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '验证' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 5:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '对比' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 6:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 7:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        elif index == 8:
            combo_box = self.sender()
            row = self.tableWidget_8.indexAt(combo_box.pos()).row()
            old_name = self.tableWidget_7.item(row, 0).text()
            if self.radioButton.isChecked():
                dialog = Dialog_裸眼常规_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_2.isChecked():
                dialog = Dialog_裸眼成像_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_3.isChecked():
                dialog = Dialog_套损检测_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '套损' + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_4.isChecked():
                dialog = Dialog_生产测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '产出剖面' + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_5.isChecked():
                dialog = Dialog_固井质量_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + '固井' + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '_' + selected_items_text + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
            elif self.radioButton_6.isChecked():
                dialog = Dialog_承包商测井_原始数据(self)
                if dialog.exec_() == QDialog.Accepted:
                    lst = []
                    with open('.\\tempFiles\\save.txt', 'r') as file:
                        for line in file:
                            lst.append(line.strip())
                    lst = list(set(lst))
                    selected_items_text = '+'.join(lst)
                    self.lineEdit_11.setText(selected_items_text)
                new_name = well_name + '_' + selected_items_text + '_' + measure_interval + '_' + '上测+下测' + '_' + logging_date + '.' + \
                           old_name.split('.')[-1]
                item = QtWidgets.QTableWidgetItem(new_name)
                self.tableWidget_8.setItem(row, 0, item)
                # self.tableWidget_8.removeCellWidget(row, 1)
        else:
            pass

    def confirm_rename(self):
        folder_path = self.lineEdit_6.text()

        # 测井原图
        folder_path_测井原图 = folder_path + '/测井原图'
        for i in range(self.tableWidget.rowCount()):
            old_name = self.tableWidget.item(i, 0).text()
            new_name = self.tableWidget_2.item(i, 0).text()
            # 检查新文件名是否与原文件名相同
            if old_name == new_name:
                print("错误：新文件名与原文件名相同！")
                continue
            # 检查目标文件是否存在
            if os.path.exists(os.path.join(folder_path_测井原图, new_name)):
                print("错误：目标文件已存在！")
                continue
            # 重命名文件
            try:
                os.rename(os.path.join(folder_path_测井原图, old_name), os.path.join(folder_path_测井原图, new_name))
                print('重命名成功')
            except FileNotFoundError as e:
                print(f"错误：{e}")

        # 刻度文件
        folder_path_刻度文件 = folder_path + '/刻度文件'
        for i in range(self.tableWidget_3.rowCount()):
            old_name = self.tableWidget_3.item(i, 0).text()
            new_name = self.tableWidget_4.item(i, 0).text()
            # 检查新文件名是否与原文件名相同
            if old_name == new_name:
                print("错误：新文件名与原文件名相同！")
                continue
            # 检查目标文件是否存在
            if os.path.exists(os.path.join(folder_path_刻度文件, new_name)):
                print("错误：目标文件已存在！")
                continue
            # 重命名文件
            try:
                os.rename(os.path.join(folder_path_刻度文件, old_name), os.path.join(folder_path_刻度文件, new_name))
                print('重命名成功')
            except FileNotFoundError as e:
                print(f"错误：{e}")

        # 相关文件
        folder_path_相关文件 = folder_path + '/相关文件'
        for i in range(self.tableWidget_5.rowCount()):
            old_name = self.tableWidget_5.item(i, 0).text()
            new_name = self.tableWidget_6.item(i, 0).text()
            # 检查新文件名是否与原文件名相同
            if old_name == new_name:
                print("错误：新文件名与原文件名相同！")
                continue
            # 检查目标文件是否存在
            if os.path.exists(os.path.join(folder_path_相关文件, new_name)):
                print("错误：目标文件已存在！")
                continue
            # 重命名文件
            try:
                os.rename(os.path.join(folder_path_相关文件, old_name), os.path.join(folder_path_相关文件, new_name))
                print('重命名成功')
            except FileNotFoundError as e:
                print(f"错误：{e}")

        # 原始数据
        folder_path_原始数据 = folder_path + '/原始数据'
        for i in range(self.tableWidget_7.rowCount()):
            old_name = self.tableWidget_7.item(i, 0).text()
            new_name = self.tableWidget_8.item(i, 0).text()
            # 检查新文件名是否与原文件名相同
            if old_name == new_name:
                print("错误：新文件名与原文件名相同！")
                continue
            # 检查目标文件是否存在
            if os.path.exists(os.path.join(folder_path_原始数据, new_name)):
                print("错误：目标文件已存在！")
                continue
            # 重命名文件
            try:
                os.rename(os.path.join(folder_path_原始数据, old_name), os.path.join(folder_path_原始数据, new_name))
                print('重命名成功')
            except FileNotFoundError as e:
                print(f"错误：{e}")
        QMessageBox.information(self, '提示', '重命名完成')

    def generate_file_list_docx(self):
        folder_path = self.lineEdit_6.text()

        #################################################################
        # 指定要遍历的文件夹
        folder_path_测井原图 = folder_path + '/测井原图'

        # 创建一个空列表来存储文件信息
        files_list = []

        # 遍历文件夹
        for filename in os.listdir(folder_path_测井原图):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path_测井原图, filename)
            # 确保是一个文件而不是文件夹
            if os.path.isfile(file_path):
                # 获取文件大小，并转换为KB
                file_size_kb = os.path.getsize(file_path) / 1024
                file_size_kb = math.ceil(file_size_kb)
                # 将文件名和文件大小添加到列表中
                files_list.append((filename, str(round(file_size_kb, 2)), ''))

        label_count = len(files_list)
        label_list = list(range(1, label_count + 1))
        # label = 'label'
        # tbl_contents1 = [{label: element} for element in label_list]
        cols = 'cols'
        tbl_contents_raw = [{cols: element} for element in files_list]
        tbl_contents_测井原图 = [{'label': str(label_list[i]), 'cols': list(tbl_contents_raw[i]['cols'])} for i in
                                 range(min(len(label_list), len(tbl_contents_raw)))]
        # 打印列表
        print('————————————测井原图————————————')
        for file_info in files_list:
            print(file_info)

        #################################################################
        # 指定要遍历的文件夹
        folder_path_刻度文件 = folder_path + '/刻度文件'

        # 创建一个空列表来存储文件信息
        files_list = []

        # 遍历文件夹
        for filename in os.listdir(folder_path_刻度文件):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path_刻度文件, filename)
            # 确保是一个文件而不是文件夹
            if os.path.isfile(file_path):
                # 获取文件大小，并转换为KB
                file_size_kb = os.path.getsize(file_path) / 1024
                file_size_kb = math.ceil(file_size_kb)
                # 将文件名和文件大小添加到列表中
                files_list.append((filename, str(round(file_size_kb, 2)), ''))

        label_count = len(files_list)
        label_list = list(range(1, label_count + 1))
        # label = 'label'
        # tbl_contents1 = [{label: element} for element in label_list]
        cols = 'cols'
        tbl_contents_raw = [{cols: element} for element in files_list]
        tbl_contents_刻度文件 = [{'label': str(label_list[i]), 'cols': list(tbl_contents_raw[i]['cols'])} for i in
                                 range(min(len(label_list), len(tbl_contents_raw)))]
        # 打印列表
        print('————————————刻度文件————————————')
        for file_info in files_list:
            print(file_info)

        #################################################################
        # 指定要遍历的文件夹
        folder_path_相关文件 = folder_path + '/相关文件'

        # 创建一个空列表来存储文件信息
        files_list = []

        # 遍历文件夹
        for filename in os.listdir(folder_path_相关文件):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path_相关文件, filename)
            # 确保是一个文件而不是文件夹
            if os.path.isfile(file_path):
                # 获取文件大小，并转换为KB
                file_size_kb = os.path.getsize(file_path) / 1024
                file_size_kb = math.ceil(file_size_kb)
                # 将文件名和文件大小添加到列表中
                files_list.append((filename, str(round(file_size_kb, 2)), ''))

        label_count = len(files_list)
        label_list = list(range(1, label_count + 1))
        # label = 'label'
        # tbl_contents1 = [{label: element} for element in label_list]
        cols = 'cols'
        tbl_contents_raw = [{cols: element} for element in files_list]
        tbl_contents_相关文件 = [{'label': str(label_list[i]), 'cols': list(tbl_contents_raw[i]['cols'])} for i in
                                 range(min(len(label_list), len(tbl_contents_raw)))]
        # 打印列表
        print('————————————相关文件————————————')
        for file_info in files_list:
            print(file_info)

        #################################################################
        # 指定要遍历的文件夹
        folder_path_原始数据 = folder_path + '/原始数据'

        # 创建一个空列表来存储文件信息
        files_list = []

        # 遍历文件夹
        for filename in os.listdir(folder_path_原始数据):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path_原始数据, filename)
            # 确保是一个文件而不是文件夹
            if os.path.isfile(file_path):
                # 获取文件大小，并转换为KB
                file_size_kb = os.path.getsize(file_path) / 1024
                file_size_kb = math.ceil(file_size_kb)
                # 将文件名和文件大小添加到列表中
                files_list.append((filename, str(round(file_size_kb, 2)), ''))

        label_count = len(files_list)
        label_list = list(range(1, label_count + 1))
        # label = 'label'
        # tbl_contents1 = [{label: element} for element in label_list]
        cols = 'cols'
        tbl_contents_raw = [{cols: element} for element in files_list]
        tbl_contents_原始数据 = [{'label': str(label_list[i]), 'cols': list(tbl_contents_raw[i]['cols'])} for i in
                                 range(min(len(label_list), len(tbl_contents_raw)))]
        # 打印列表
        print('————————————原始数据————————————')
        for file_info in files_list:
            print(file_info)

        #################################################################
        #################################################################
        tpl = DocxTemplate('.\\tempFiles\\测井数据文件清单模板.docx')

        # 信息补充
        well_name = self.lineEdit.text()
        measure_depth = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        info_date = self.lineEdit_4.text()
        casing_size = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()
        transfer_date = self.lineEdit_3.text()  # 令移交日期等于测井日期

        folder_path = self.lineEdit_6.text()
        # 测井原图
        folder_path_测井原图 = folder_path + '/测井原图'
        folder_path_刻度文件 = folder_path + '/刻度文件'
        folder_path_相关文件 = folder_path + '/相关文件'
        folder_path_原始数据 = folder_path + '/原始数据'

        count_原始数据 = self.count_files(folder_path_原始数据)
        count_测井原图 = self.count_files(folder_path_测井原图)
        count_刻度文件 = self.count_files(folder_path_刻度文件)
        count_相关文件 = self.count_files(folder_path_相关文件)

        context = {
            'count_原始数据': count_原始数据,
            'count_测井原图': count_测井原图,
            'count_刻度文件': count_刻度文件,
            'count_相关文件': count_相关文件,

            'well_name': well_name,
            'logging_team': logging_team,
            'logging_series': logging_series,
            'logging_date': logging_date,
            'transferor': transferor,
            'transfer_date': transfer_date,
            'reciever': reciever,

            'tbl_contents_测井原图': tbl_contents_测井原图,
            'tbl_contents_刻度文件': tbl_contents_刻度文件,
            'tbl_contents_相关文件': tbl_contents_相关文件,
            'tbl_contents_原始数据': tbl_contents_原始数据
        }
        tpl.render(context)
        tpl.save(folder_path + '/' + well_name + '测井数据文件清单' + '_' + logging_date + '.docx')
        # 弹出提示框
        QMessageBox.information(None, '提示', '测井数据文件清单已生成')

    def count_files(self, folder_path):
        file_list = os.listdir(folder_path)
        file_count = len(file_list)
        return file_count

    def compress_and_rename(self):
        well_name = self.lineEdit.text()
        measure_interval = self.lineEdit_2.text()
        logging_date = self.lineEdit_3.text()
        inform_sheet_date = self.lineEdit_4.text()
        casing_info = self.lineEdit_5.text()
        logging_team = self.lineEdit_7.text()
        logging_series = self.lineEdit_8.text()
        transferor = self.lineEdit_9.text()
        reciever = self.lineEdit_10.text()

        folder_path = self.lineEdit_6.text()
        folder_path_测井原图 = folder_path + '/测井原图'
        folder_path_刻度文件 = folder_path + '/刻度文件'
        folder_path_相关文件 = folder_path + '/相关文件'
        folder_path_原始数据 = folder_path + '/原始数据'

        if self.radioButton.isChecked():
            # dialog = Dialog_裸眼常规_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '常规' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '常规' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '常规' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '常规' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'
        elif self.radioButton_2.isChecked():
            # dialog = Dialog_裸眼成像_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[成像项目]' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[成像项目]' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[成像项目]' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[成像项目]' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'
        elif self.radioButton_3.isChecked():
            # dialog = Dialog_套损检测_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '套损' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '套损' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '套损' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '套损' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'
        elif self.radioButton_4.isChecked():
            # dialog = Dialog_生产测井_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '生产测井' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '生产测井' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '生产测井' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '生产测井' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'
        elif self.radioButton_5.isChecked():
            # dialog = Dialog_固井质量_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '固井' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '固井' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '固井' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '固井' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'
        elif self.radioButton_6.isChecked():
            # dialog = Dialog_承包商测井_测井原图(self)
            archive_base_name_测井原图 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[承包商项目]' + '_' + logging_date + '_' + '原始' + '_' + '测井原图'
            archive_base_name_刻度文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[承包商项目]' + '_' + logging_date + '_' + '原始' + '_' + '刻度文件'
            archive_base_name_相关文件 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[承包商项目]' + '_' + logging_date + '_' + '原始' + '_' + '相关文件'
            archive_base_name_原始数据 = folder_path + '\\' + well_name + '压缩包' + '\\' + well_name + '_' + '[承包商项目]' + '_' + logging_date + '_' + '原始' + '_' + '原始数据'

        shutil.make_archive(archive_base_name_测井原图, 'zip', folder_path_测井原图)
        shutil.make_archive(archive_base_name_刻度文件, 'zip', folder_path_刻度文件)
        shutil.make_archive(archive_base_name_相关文件, 'zip', folder_path_相关文件)
        shutil.make_archive(archive_base_name_原始数据, 'zip', folder_path_原始数据)

        # 弹出提示框
        QMessageBox.information(None, '提示', '压缩包已生成')


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    window = Main_window()
    window.show()
    app.exec_()
