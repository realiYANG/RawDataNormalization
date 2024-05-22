from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QDialogButtonBox


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("选择项目")
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(['>>>>>>>>>>>>>>>>>>>>>>>>>'])
        self.treeWidget.setSelectionMode(QTreeWidget.MultiSelection)

        self.cejingxiangmu_list = []

        # 连接根节点的点击信号
        self.treeWidget.itemClicked.connect(self.print_selected_items)
        self.treeWidget.itemChanged.connect(self.handle_item_changed)
        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['裸眼常规'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["GR"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["CAL"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        child_item3 = QTreeWidgetItem(root_item, ["DEV"])
        child_item3.setFlags(child_item3.flags() | Qt.ItemIsUserCheckable)
        child_item3.setCheckState(0, Qt.Unchecked)

        child_item4 = QTreeWidgetItem(root_item, ["DAZ"])
        child_item4.setFlags(child_item4.flags() | Qt.ItemIsUserCheckable)
        child_item4.setCheckState(0, Qt.Unchecked)

        child_item5 = QTreeWidgetItem(root_item, ["PE"])
        child_item5.setFlags(child_item5.flags() | Qt.ItemIsUserCheckable)
        child_item5.setCheckState(0, Qt.Unchecked)

        child_item6 = QTreeWidgetItem(root_item, ["AC"])
        child_item6.setFlags(child_item6.flags() | Qt.ItemIsUserCheckable)
        child_item6.setCheckState(0, Qt.Unchecked)

        child_item7 = QTreeWidgetItem(root_item, ["CNL"])
        child_item7.setFlags(child_item7.flags() | Qt.ItemIsUserCheckable)
        child_item7.setCheckState(0, Qt.Unchecked)

        child_item8 = QTreeWidgetItem(root_item, ["DEN"])
        child_item8.setFlags(child_item7.flags() | Qt.ItemIsUserCheckable)
        child_item8.setCheckState(0, Qt.Unchecked)

        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['裸眼成像'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["MIRL_核磁"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["FMI_电成像"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        child_item3 = QTreeWidgetItem(root_item, ["XMAC"])
        child_item3.setFlags(child_item3.flags() | Qt.ItemIsUserCheckable)
        child_item3.setCheckState(0, Qt.Unchecked)

        child_item4 = QTreeWidgetItem(root_item, ["HDIL"])
        child_item4.setFlags(child_item4.flags() | Qt.ItemIsUserCheckable)
        child_item4.setCheckState(0, Qt.Unchecked)

        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['套损检测'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["MIT24电缆"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["MIT24连油存储式"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        child_item3 = QTreeWidgetItem(root_item, ["MIT24格威电缆"])
        child_item3.setFlags(child_item3.flags() | Qt.ItemIsUserCheckable)
        child_item3.setCheckState(0, Qt.Unchecked)

        child_item4 = QTreeWidgetItem(root_item, ["MIT24格威连油存储式"])
        child_item4.setFlags(child_item4.flags() | Qt.ItemIsUserCheckable)
        child_item4.setCheckState(0, Qt.Unchecked)

        child_item5 = QTreeWidgetItem(root_item, ["MIT40电缆"])
        child_item5.setFlags(child_item5.flags() | Qt.ItemIsUserCheckable)
        child_item5.setCheckState(0, Qt.Unchecked)

        child_item6 = QTreeWidgetItem(root_item, ["MIT40连油存储式"])
        child_item6.setFlags(child_item6.flags() | Qt.ItemIsUserCheckable)
        child_item6.setCheckState(0, Qt.Unchecked)

        child_item7 = QTreeWidgetItem(root_item, ["MIT40格威电缆"])
        child_item7.setFlags(child_item7.flags() | Qt.ItemIsUserCheckable)
        child_item7.setCheckState(0, Qt.Unchecked)

        child_item8 = QTreeWidgetItem(root_item, ["MIT40格威连油存储式"])
        child_item8.setFlags(child_item8.flags() | Qt.ItemIsUserCheckable)
        child_item8.setCheckState(0, Qt.Unchecked)

        child_item9 = QTreeWidgetItem(root_item, ["MIT60电缆"])
        child_item9.setFlags(child_item9.flags() | Qt.ItemIsUserCheckable)
        child_item9.setCheckState(0, Qt.Unchecked)

        child_item10 = QTreeWidgetItem(root_item, ["MIT60连油存储式"])
        child_item10.setFlags(child_item10.flags() | Qt.ItemIsUserCheckable)
        child_item10.setCheckState(0, Qt.Unchecked)

        child_item11 = QTreeWidgetItem(root_item, ["MIT60格威电缆"])
        child_item11.setFlags(child_item11.flags() | Qt.ItemIsUserCheckable)
        child_item11.setCheckState(0, Qt.Unchecked)

        child_item12 = QTreeWidgetItem(root_item, ["MIT60格威连油存储式"])
        child_item12.setFlags(child_item12.flags() | Qt.ItemIsUserCheckable)
        child_item12.setCheckState(0, Qt.Unchecked)

        child_item13 = QTreeWidgetItem(root_item, ["MID-K电缆"])
        child_item13.setFlags(child_item13.flags() | Qt.ItemIsUserCheckable)
        child_item13.setCheckState(0, Qt.Unchecked)

        child_item14 = QTreeWidgetItem(root_item, ["MID-S电缆"])
        child_item14.setFlags(child_item14.flags() | Qt.ItemIsUserCheckable)
        child_item14.setCheckState(0, Qt.Unchecked)

        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['固井质量'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["VDL"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["MCET存储式"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        child_item3 = QTreeWidgetItem(root_item, ["RBT"])
        child_item3.setFlags(child_item3.flags() | Qt.ItemIsUserCheckable)
        child_item3.setCheckState(0, Qt.Unchecked)

        child_item4 = QTreeWidgetItem(root_item, ["SBT"])
        child_item4.setFlags(child_item4.flags() | Qt.ItemIsUserCheckable)
        child_item4.setCheckState(0, Qt.Unchecked)

        child_item5 = QTreeWidgetItem(root_item, ["CAST-I"])
        child_item5.setFlags(child_item5.flags() | Qt.ItemIsUserCheckable)
        child_item5.setCheckState(0, Qt.Unchecked)

        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['生产测井'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["PLT"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["MAPS"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        ####################################################################
        # 添加根节点
        root_item = QTreeWidgetItem(self.treeWidget, ['承包商项目'])
        root_item.setFlags(root_item.flags() & ~Qt.ItemIsUserCheckable)
        # root_item.setCheckState(0, Qt.Unchecked)
        # 添加子节点
        child_item1 = QTreeWidgetItem(root_item, ["光纤测井"])
        child_item1.setFlags(child_item1.flags() | Qt.ItemIsUserCheckable)
        child_item1.setCheckState(0, Qt.Unchecked)

        child_item2 = QTreeWidgetItem(root_item, ["微地震"])
        child_item2.setFlags(child_item2.flags() | Qt.ItemIsUserCheckable)
        child_item2.setCheckState(0, Qt.Unchecked)

        child_item3 = QTreeWidgetItem(root_item, ["PNNPlus"])
        child_item3.setFlags(child_item3.flags() | Qt.ItemIsUserCheckable)
        child_item3.setCheckState(0, Qt.Unchecked)

        # 将树形控件添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.treeWidget)

        # 添加确认按钮
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def print_selected_items(self):
        # 遍历所有项目，检查复选框状态
        for index in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(index)
            self.check_item(item)
    def check_item(self, item):
        if item.checkState(0) == Qt.Checked:
            self.cejingxiangmu_list.append(item.text(0))
        # print('测井项目: ' + str(self.cejingxiangmu_list))
        with open('save.txt', 'w') as file:
            for item_temp in self.cejingxiangmu_list:
                file.write(str(item_temp) + '\n')

        # 递归检查子项目
        for i in range(item.childCount()):
            child = item.child(i)
            self.check_item(child)

    def handle_item_changed(self, item, column):
        self.cejingxiangmu_list = []
        if column == 0:  # Only react to changes in the first column (where checkboxes are)
            if item.checkState(column) == Qt.Checked:
                # Uncheck all sibling items when the current item is checked
                self.uncheck_siblings(item)

    def uncheck_siblings(self, item):
        parent = item.parent()
        if parent is None:  # If the item has no parent, it's a root item; do nothing
            return

        child_count = parent.childCount()
        for i in range(child_count):
            sibling = parent.child(i)
            if sibling != item and sibling.flags() & Qt.ItemIsUserCheckable:
                sibling.setCheckState(0, Qt.Unchecked)  # Uncheck the sibling